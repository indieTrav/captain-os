# GitHub Actions + Docker Deploy Checklist

End-to-end checklist for shipping a containerized app to a server via GitHub Actions. Work top to bottom — each section assumes the prior one is done.

---

## 1. Local Docker Setup

- [ ] `Dockerfile` in repo root (multi-stage build if compiled language)
- [ ] `.dockerignore` excludes `node_modules`, `.git`, `.env`, `dist/`, local artifacts
- [ ] `docker-compose.yml` if app needs multiple services (app + db + reverse proxy + cache)
- [ ] `docker-compose.prod.yml` (or override) if production differs from local
- [ ] Image builds cleanly: `docker build -t app:local .`
- [ ] Container runs cleanly: `docker run --rm -p 3000:3000 app:local`
- [ ] App reads config from environment variables, not hardcoded values
- [ ] Non-root user inside container (security)
- [ ] Healthcheck defined (`HEALTHCHECK` in Dockerfile or in compose)
- [ ] Image size is reasonable (slim/alpine base where possible)

---

## 2. Server / Host Prep

- [ ] Server provisioned (VPS, EC2, Hetzner, etc.) with sudo user
- [ ] Docker Engine installed on server
- [ ] Docker Compose plugin installed
- [ ] Deploy user created (non-root, in `docker` group)
- [ ] Deploy directory exists (e.g., `/opt/app/`) and owned by deploy user
- [ ] Firewall configured (ports 80, 443, 22 only — block everything else)
- [ ] SSH (Secure Shell) hardened: key auth only, password auth disabled, root login disabled
- [ ] Fail2ban or equivalent brute-force protection installed
- [ ] Automatic security updates enabled (`unattended-upgrades` on Ubuntu)
- [ ] Server hostname / DNS (Domain Name System) record pointing to it

---

## 3. Container Registry

Pick one and set up auth before writing the workflow.

- [ ] Registry chosen: GitHub Container Registry (ghcr.io), Docker Hub, or private registry
- [ ] If ghcr.io: confirm `packages: write` permission available in workflow
- [ ] If Docker Hub: access token created (not account password)
- [ ] Image naming convention decided (e.g., `ghcr.io/<owner>/<repo>:<sha>` and `:latest`)
- [ ] Registry login tested manually from your machine
- [ ] Old image cleanup policy considered (registries fill up fast)

---

## 4. SSH Deploy Key

- [ ] Generate dedicated deploy keypair: `ssh-keygen -t ed25519 -C "github-actions-deploy" -f deploy_key -N ""`
- [ ] Public key (`deploy_key.pub`) added to server's `~/.ssh/authorized_keys` for deploy user
- [ ] Private key (`deploy_key`) copied for GitHub secret (full content, including header/footer)
- [ ] Test the key works from your laptop: `ssh -i deploy_key deployuser@server`
- [ ] Delete local copy of the private key after adding it to GitHub secrets

---

## 5. `.github/workflows/deploy.yml`

- [ ] File exists at `.github/workflows/deploy.yml`
- [ ] Trigger defined (`push` to main, `workflow_dispatch` for manual, or tag-based)
- [ ] Concurrency group set so deploys don't stomp each other
- [ ] Permissions block minimal (`contents: read`, `packages: write` if pushing to ghcr)
- [ ] Steps included:
  - [ ] `actions/checkout@v4`
  - [ ] `docker/setup-buildx-action@v3` (enables build caching)
  - [ ] `docker/login-action@v3` for registry auth
  - [ ] `docker/build-push-action@v5` with `cache-from`/`cache-to` set to `type=gha`
  - [ ] SSH step (e.g., `appleboy/ssh-action`) to pull image + restart container on server
  - [ ] Post-deploy health check step (curl `/health` and fail the job if non-200)
- [ ] Image tagged with both `:latest` and `:${{ github.sha }}` for rollback
- [ ] Workflow runs on a pinned `ubuntu-latest` runner (or self-hosted if needed)

---

## 6. GitHub Secrets (Settings → Secrets and variables → Actions)

Repo-level secrets needed:

- [ ] `SSH_PRIVATE_KEY` — the deploy private key from step 4
- [ ] `SSH_HOST` — server IP or hostname
- [ ] `SSH_USER` — deploy username
- [ ] `SSH_PORT` — if non-standard (otherwise 22)
- [ ] Registry auth (only if not using built-in `GITHUB_TOKEN`):
  - [ ] `DOCKERHUB_USERNAME`
  - [ ] `DOCKERHUB_TOKEN`
- [ ] App runtime secrets (anything the container needs at start):
  - [ ] `DATABASE_URL`
  - [ ] `JWT_SECRET` / session secrets
  - [ ] Third-party API keys
- [ ] `.env.example` checked into repo so collaborators know what's required
- [ ] Real `.env` is `.gitignore`d (verify with `git check-ignore .env`)
- [ ] Production `.env` on server is owned by deploy user, mode `600`

---

## 7. Repo Permissions, Collaborators, Teams

GitHub repo settings:

- [ ] Default branch set to `main`
- [ ] Branch protection on `main`:
  - [ ] Require pull request before merging
  - [ ] Require at least 1 approval
  - [ ] Require status checks to pass (CI tests, lint)
  - [ ] Require branches to be up to date before merging
  - [ ] Restrict who can push to matching branches
- [ ] Actions permissions reviewed (Settings → Actions → General):
  - [ ] Allowed actions scoped (don't allow "all actions" if not needed)
  - [ ] Workflow permissions set to "read" by default, elevated per workflow
  - [ ] Fork PR workflows require approval (prevents secret exfiltration)
- [ ] Collaborator access set per person (Settings → Collaborators):
  - [ ] Read-only for stakeholders
  - [ ] Write for engineers
  - [ ] Admin only for owners
- [ ] Team permissions configured if org repo (Settings → Collaborators and teams):
  - [ ] One team = one access level
  - [ ] No personal accounts where a team would do
- [ ] CODEOWNERS file (`.github/CODEOWNERS`) for auto-review assignment
- [ ] Deploy keys reviewed (Settings → Deploy keys) — remove anything stale

---

## 8. Reverse Proxy + TLS

Skip if your platform handles this (Railway, Fly, Render). Required for raw VPS.

- [ ] Reverse proxy chosen: Caddy (auto-TLS), Traefik, or Nginx + Certbot
- [ ] Proxy config routes domain → container port
- [ ] TLS (Transport Layer Security) certificate auto-renews
- [ ] HTTP redirects to HTTPS
- [ ] Security headers set (HSTS, X-Frame-Options, etc.)
- [ ] Domain DNS A/AAAA record points at server
- [ ] Test cert: `curl -vI https://yourdomain.com` shows valid cert

---

## 9. Health, Logs, Rollback

- [ ] App exposes `/health` (or equivalent) returning 200 when healthy
- [ ] Workflow's post-deploy step hits `/health` and fails if it doesn't return 200
- [ ] Container logs accessible: `docker logs <container>` or shipped to log service
- [ ] Log rotation configured (containers can fill disk fast)
- [ ] Rollback path documented: `docker pull <image>:<previous-sha> && docker compose up -d`
- [ ] Previous N image tags kept in registry (don't auto-delete `:latest`-only)

---

## 10. First Deploy

- [ ] Push a trivial change to `main` to trigger the workflow
- [ ] Watch the run in the Actions tab — every step green
- [ ] SSH to server, confirm new image is running: `docker ps`
- [ ] Hit the live URL in a browser
- [ ] Check logs for startup errors: `docker logs <container> --tail 100`
- [ ] Trigger an intentional rollback to validate the rollback path works
- [ ] Document the deploy + rollback process in the repo README

---

## 11. Often-Missed Items

- [ ] `.gitignore` updated (no `.env`, no `*.pem`, no `deploy_key*`)
- [ ] Database backup strategy in place before first prod traffic
- [ ] Database migrations run as part of deploy (or as a separate gated step)
- [ ] Zero-downtime considered: blue/green, or at minimum `docker compose up -d` with healthcheck-gated restart
- [ ] Time zone on server set to UTC
- [ ] Server has swap configured (small VPS instances often don't by default)
- [ ] Uptime monitor pointed at `/health` (UptimeRobot, BetterStack, etc.)
- [ ] Error tracking wired up (Sentry, Highlight, etc.)
- [ ] Secrets rotation plan: who rotates what, how often
- [ ] Disaster recovery: can you redeploy from scratch on a new server in under an hour?

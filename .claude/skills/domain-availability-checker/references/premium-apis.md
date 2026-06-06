# RapidAPI Setup — Domain Availability Checker

## Domainr (recommended)

**Free tier:** 100 requests/month on free plan, paid plans available  
**RapidAPI listing:** rapidapi.com/domainr/api/domainr

### Setup

1. Sign up at rapidapi.com (free)
2. Search "Domainr" → click **Subscribe to Test** (free tier)
3. Go to the API page → **Code Snippets** → copy the `X-RapidAPI-Key` header value
4. Add to your `.env`:
   ```
   RAPID_API_KEY=your_key_here
   ```

### Response format

```json
{
  "status": [
    {
      "domain": "example.com",
      "zone": "com",
      "status": "undelegated inactive",
      "summary": "inactive"
    }
  ]
}
```

| `summary` value        | Meaning                                        |
| ---------------------- | ---------------------------------------------- |
| `inactive`             | Available to register                          |
| `undelegated inactive` | Available (TLD exists but domain unregistered) |
| `active`               | Registered / taken                             |
| `unknown`              | Cannot determine                               |

### Troubleshooting

**403 error:** API key is wrong or you haven't subscribed to Domainr on RapidAPI.  
**Empty response:** Domain TLD may not be supported by domainr.  
**Rate limit hit:** Upgrade your RapidAPI plan or reduce `--rate-limit`.

---

## Rate limits reference

| Method             | Free limit      | Notes                                  |
| ------------------ | --------------- | -------------------------------------- |
| whois CLI          | Unlimited       | Throttled by OS; 0.3s default is fine  |
| Domainr (RapidAPI) | 10 req/day free | Paid plans start at ~$10/mo for 1k/day |

from datetime import datetime, timezone

now = datetime.now(timezone.utc)
s = now.isoformat()
print(s)

parsed = datetime.fromisoformat(s)
print(parsed.tzinfo)

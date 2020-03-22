import redis
from datetime import timedelta

r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

r.get("Bahamas")


# setex: "SET" with expiration
r.setex("runner", timedelta(seconds=10), value="now you see me, now you don't")

r.ttl("runner")  # "Time To Live", in seconds

r.get("runner")  # Not expired yet


r.expire("runner", timedelta(seconds=3))  # Set new expire window

# Pause for a few seconds
r.get("runner")
r.exists("runner")  # Key & value are both gone (expired)


r.pttl("runner")  # Like ttl, but milliseconds

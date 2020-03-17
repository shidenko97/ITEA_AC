# pip install pymemcache
import json

from pymemcache.client import base

# Don't forget to run `memcached' before running this next line:
client = base.Client(("localhost", 11211))

# Once the client is instantiated, you can access the cache:
client.set("some_key", "some value")

# Retrieve previously set data again:
client.get("some_key")
# 'some value'


def do_some_query():
    # Replace with actual querying code to a database,
    # a remote REST API, etc.
    return 42


my_dict = {1: 2, 2: 3}
my_str = json.dumps(my_dict)

# Don't forget to run `memcached' before running this code
client = base.Client(("localhost", 11211))
result = client.get("some_key")

if result is None:
    # The cache is empty, need to get the value
    # from the canonical source:
    result = do_some_query()

    # Cache the result for next time:
    client.set("some_key", result)

# Whether we needed to update the cache or not,
# at this point you can work with the data
# stored in the `result` variable:
print(result)

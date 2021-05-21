from datetime import datetime
from cachetools import TTLCache, cached

time_cache = TTLCache(maxsize=200, ttl=300)

@cached(time_cache)
def get_time(uuid: str) -> str:
    now = datetime.now()
    return now.strftime("%X.%f")

# return function response    
print(get_time("key"))    

# return cached result    
print(get_time("key"))  

# remove expired items from the cache, these should then be re-requested    
time_cache.expire(time=500)

# return function response    
print(get_time("key"))

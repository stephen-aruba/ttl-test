#! .venv/bin/python3

from datetime import datetime

from operator import attrgetter
from cachetools import TTLCache, cachedmethod, cached


call_count = 0

time_cache = TTLCache(maxsize=200, ttl=300)


@cached(time_cache)
def get_time(uuid: str) -> str:
    global call_count

    call_count += 1
    now = datetime.now()

    return now.strftime("%X.%f")


class TTLTester:
    def __init__(self):
        self.cache = TTLCache(maxsize=200, ttl=300)  # TTL in seconds

    @cachedmethod(attrgetter("cache"))
    def get_time(self, uuid: str) -> str:
        global call_count

        call_count += 1
        now = datetime.now()

        return now.strftime("%X.%f")


def test_cache():
    """Test normal cache"""
    global call_count
    call_count = 0

    print("Start test_cache")

    # return method response
    print(get_time("key"))
    assert call_count == 1

    # return cached result
    print(get_time("key"))
    assert call_count == 1

    # remove expired items from the cache, these should then be re-requested
    time_cache.expire(time=500)  # time in seconds since start of test

    # return method response
    print(get_time("key"))
    assert call_count == 2


def test_method_cache():
    """Test class method cache"""
    global call_count
    call_count = 0

    ttt = TTLTester()

    print("Start test_method_cache")

    # return method response
    print(ttt.get_time("key"))
    assert call_count == 1

    # return cached result
    print(ttt.get_time("key"))
    assert call_count == 1

    # remove expired items from the cache, these should then be re-requested
    ttt.cache.expire(time=500)  # time in seconds since start of test

    # return method response
    print(ttt.get_time("key"))
    assert call_count == 2


if __name__ == "__main__":
    test_cache()
    test_method_cache()

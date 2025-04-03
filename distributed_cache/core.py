import functools
import pickle
import hashlib

from .redis_client import get_redis_client
from .registry import CacheRegistry

redis_client = get_redis_client()
registry = CacheRegistry(redis_client)

def cache(ttl=None):
    def decorator(func):
        func_name, func_hash = registry.register(func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key_raw = f"{func_name}:{func_hash}:{args}:{kwargs}"
            cache_key = hashlib.sha256(key_raw.encode()).hexdigest()

            cached = redis_client.get(cache_key)
            if cached:
                print(f"[CACHE HIT] Cache key: {cache_key}")
                return pickle.loads(cached)
            print(f"[CACHE MISS] Cache key: {cache_key}")
            result = func(*args, **kwargs)
            serialized = pickle.dumps(result)

            if ttl:
                redis_client.setex(cache_key, ttl, serialized)
            else:
                redis_client.set(cache_key, serialized)

            return result
        return wrapper
    return decorator

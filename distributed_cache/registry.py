import inspect
import hashlib

class CacheRegistry:
    def __init__(self, redis_client):
        self.redis = redis_client
        self.version_key = "cache:func_versions"

    def get_func_hash(self, func):
        source = inspect.getsource(func)
        return hashlib.sha256(source.encode()).hexdigest()[:8]

    def register(self, func):
        func_name = f"{func.__module__}.{func.__name__}"
        new_hash = self.get_func_hash(func)

        stored_hash = self.redis.hget(self.version_key, func_name)
        if stored_hash:
            stored_hash = stored_hash.decode()
            if stored_hash != new_hash:
                print(f"Function {func_name} has changed. Old hash: {stored_hash}, New hash: {new_hash}")
                self.clear_old_versions(func_name)
        self.redis.hset(self.version_key, func_name, new_hash)
        return func_name, new_hash

    def clear_old_versions(self, func_name):
        pattern = f"cache:{func_name}:*"
        for key in self.redis.scan_iter(pattern):
            self.redis.delete(key)

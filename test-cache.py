from distributed_cache import cache
import time

# Simulate a slow function (e.g., DB or API call)
@cache(ttl=120)  # cache for 120 seconds
def fetch_user_profile(user_id):
    print(f"[DB HIT] Fetching user profile for: {user_id}")
    time.sleep(2)  # simulate delay
    return {"user_id": user_id, "name": "Alice", "timestamp": time.time() , "data": "Function Version 3"}


def run_test():
    print("⏳ First call (should hit DB)...")
    user = fetch_user_profile("123")
    print("Result:", user)

    print("\n⚡ Second call (should hit cache)...")
    user = fetch_user_profile("123")
    print("Result:", user)

    print("\n⌛ Wait for cache to expire (10s)...")
    time.sleep(11)

    print("\n🔁 Third call (should hit DB again)...")
    user = fetch_user_profile("123")
    print("Result:", user)


if __name__ == "__main__":
    run_test()

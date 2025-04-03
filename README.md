Absolutely! Here's the **complete `README.md`** file for your **Distributed Redis Cache Decorator** project, ready to copy-paste:

---

### 📄 `README.md`

```markdown
# 🚀 Distributed Redis Cache Decorator (Python)

A plug-and-play Redis-backed caching decorator for Python services.  
Automatically detects function logic changes, supports distributed app instances, and manages cache lifecycle through a centralized Redis store.

---

## 🔧 Features

- ✅ Function-level caching with optional TTL
- ✅ Centralized Redis-based cache store
- ✅ Auto version tracking via function source hash
- ✅ Singleton Redis client for performance
- ✅ Works across multiple service instances (distributed systems)
- ✅ Automatically clears outdated cache on function change
- ✅ Easy integration into any Python project

---

## 📦 Installation

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/distributed_cache.git
cd distributed_cache
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Redis Configuration (Optional)

Set the following environment variables to configure your Redis connection:

```bash
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```

Defaults:
- Host: `localhost`
- Port: `6379`
- DB: `0`

---

## 🧪 Example Usage

```python
from distributed_cache import cache
import time

@cache(ttl=10)  # Cache result for 10 seconds
def get_user(user_id):
    print(f"[DB HIT] Fetching user {user_id}")
    time.sleep(2)
    return {"id": user_id, "name": "Alice"}
```

### 🧪 Test Script Example

Save this as `test_cache.py`:

```python
from distributed_cache import cache
import time

@cache(ttl=10)
def fetch_user_profile(user_id):
    print(f"[DB HIT] Fetching user profile for: {user_id}")
    time.sleep(2)
    return {"user_id": user_id, "name": "Alice", "timestamp": time.time()}

def run_test():
    print("⏳ First call (should hit DB)...")
    print(fetch_user_profile("123"))

    print("\n⚡ Second call (should hit cache)...")
    print(fetch_user_profile("123"))

    print("\n⌛ Waiting for cache to expire...")
    time.sleep(11)

    print("\n🔁 Third call (should hit DB again)...")
    print(fetch_user_profile("123"))

if __name__ == "__main__":
    run_test()
```

Run it:

```bash
python test_cache.py
```

---

## 📂 Project Structure

```
distributed_cache/
├── __init__.py          # Exports the decorator
├── core.py              # Cache decorator logic
├── registry.py          # Cache version tracker
├── redis_client.py      # Singleton Redis connection
├── requirements.txt
├── README.md
└── test_cache.py        # Example usage and test runner
```

---

## 🛠 How It Works

- The decorator hashes the source code of each function
- If the hash changes (e.g., logic updated), the decorator clears the old cache keys
- The result is cached with an optional TTL in a centralized Redis server
- Shared Redis = works across distributed service instances

---

## 📚 Future Enhancements

- [ ] Async support with `aioredis`
- [ ] CLI tool to inspect and purge caches
- [ ] JSON serialization option
- [ ] Cache key namespace configuration
- [ ] Integration with metrics/logging frameworks


---

## 📜 License

MIT License  
Feel free to use this in personal or commercial projects. Contributions welcome!


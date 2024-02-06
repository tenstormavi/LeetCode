import time


class Cache:

    def __init__(self, ttl, not_found_object=None):
        self.ttl = ttl
        self.cache = {}
        self.not_found_object = not_found_object

    def set(self, key, value):
        self.cache[key] = {'value': value, 'time': time.time()}

    def get(self, key):
        if key in self.cache:
            entry = self.cache[key]
            if time.time() - entry['time'] < self.ttl:
                return entry['value']
            else:
                del self.cache[key]
        return self.not_found_object


if __name__ == "__main__":
    cache = Cache(60, 'NOT_FOUND')

    # set a value in the cache
    cache.set('sample', 'testing')

    # get a value from the cache
    result = cache.get('sample')  # returns 'value'
    print(f"Found valid cache: {result}")

    # get a non-existent value from the cache
    result = cache.get('no_key')  # returns 'Object not found'
    print(result)

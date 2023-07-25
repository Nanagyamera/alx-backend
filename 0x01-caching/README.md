CACHE CLASSES

In this repository,is the  implementations of various cache classes that inherit from the BaseCaching class. Each cache class represents a different caching system with specific eviction policies.

BASECACHING

The BaseCaching class serves as the foundation for all the caching systems implemented in this repository. It provides common functionalities and data structures that are shared among the cache classes. The base class defines a dictionary called cache_data to store cached items. It also specifies abstract methods put and get, which must be implemented in the child classes.

BasicCache

The BasicCache class is a simple caching system that allows you to add and retrieve items from the cache. It doesn't have a limit on the number of items it can store. When using the put method, it adds the provided item to the cache_data dictionary with the given key. The get method retrieves items from the cache using the provided key.

FIFOCache

The FIFOCache class represents a caching system that uses the First-In-First-Out (FIFO) eviction policy. It inherits from BaseCaching and overrides the put and get methods. The put method adds items to the cache, and if the cache exceeds its maximum capacity (BaseCaching.MAX_ITEMS), it removes the first item that was put in the cache. The get method retrieves items from the cache while updating the order of recently accessed items based on the FIFO policy.

LIFOCache

The LIFOCache class is a caching system that follows the Last-In-First-Out (LIFO) eviction policy. It inherits from BaseCaching and overrides the put and get methods. The put method adds items to the cache, and if the cache exceeds its maximum capacity (BaseCaching.MAX_ITEMS), it removes the last item that was put in the cache. The get method retrieves items from the cache while updating the order of recently accessed items based on the LIFO policy.

LRUCache

The LRUCache class represents a caching system that uses the Least Recently Used (LRU) eviction policy. It inherits from BaseCaching and overrides the put and get methods. The put method adds items to the cache, and if the cache exceeds its maximum capacity (BaseCaching.MAX_ITEMS), it removes the least recently used item from the cache. The get method retrieves items from the cache while updating the order of recently accessed items based on the LRU policy.

MRUCache

The MRUCache class is a caching system that follows the Most Recently Used (MRU) eviction policy. It inherits from BaseCaching and overrides the put and get methods. The put method adds items to the cache, and if the cache exceeds its maximum capacity (BaseCaching.MAX_ITEMS), it removes the most recently used item from the cache. If multiple items have the same frequency of use, the LRU algorithm is used to choose the least recently used item. The get method retrieves items from the cache while updating the order of recently accessed items based on the MRU policy.

LFUCache
The LFUCache class represents a caching system that uses the Least Frequently Used (LFU) eviction policy. It inherits from BaseCaching and overrides the put and get methods. The put method adds items to the cache, and if the cache exceeds its maximum capacity (BaseCaching.MAX_ITEMS), it removes the least frequently used item from the cache. If multiple items have the same frequency of use, the LRU algorithm is used to choose the least recently used item among them. The get method retrieves items from the cache while updating the frequency of use for each item based on the LFU policy.

Usage
You can use these cache classes in your Python projects to implement various caching systems with different eviction policies. Import the desired class into your code and create an instance of it. You can then use the put and get methods to interact with the cache.

#### Code Design

The Router class uses an instance of the RouteTrie class to store the URL paths and their associated handlers. 

The split_path method splits the URL path into separate parts, add_handler uses the insert method of the RouteTrie class to insert the URL path and its handler into the RouteTrie. The lookup method splits the URL path into separate parts and uses the find method of the RouteTrie to find the handler for the URL path. If the handler is not found, None is returned.


#### Efficiency

Insert and find has time effiency of O(n) because they need to loop through the nodes from root to leaf.

The space effiency is O(n) where n is the number of character paths which split by '/'.

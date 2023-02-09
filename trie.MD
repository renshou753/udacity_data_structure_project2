#### Code Design

Trie is a perfect option here to build autocomplete feature. The Trie class has find and insert method, the insert method takes in a word and inserts it into the trie by adding each character as a child.

#### Efficiency

The time complexity for inserting is O(n) because the program has to iterate through the children nodes and add trie node if it does not exist yet. Time efficiency for find is also O(n) where n is the number of characters in prefix word.

The storage efficiency depends on the number of words the trie contains, on average O(n)

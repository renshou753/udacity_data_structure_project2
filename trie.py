import itertools

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def suffixes(self, prefix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        if self.is_word:
            suffixes.append(prefix)
        for k, node in self.children.items():
            suffixes += node.suffixes(prefix + k)
                
        
        return [s for s in suffixes if s]

    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for idx, char in enumerate(prefix):
            if char not in current_node.children:
                return None
            else:
                if idx == len(prefix)-1:
                    return current_node.children[char]
                else:
                    current_node = current_node.children[char]


word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.insert(word)

prefixNode = word_trie.find("goo")
if prefixNode:
    print()
else:
    print(" not found")



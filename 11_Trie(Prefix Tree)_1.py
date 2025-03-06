# Implement a Trie (Prefix Tree) with insert, search, and delete operations.

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Marks if this node ends a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """ Inserts a word into the Trie """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word):
        """ Returns True if word exists in Trie, else False """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        """ Returns True if any word in Trie starts with the given prefix """
        return self._find_node(prefix) is not None

    def delete(self, word):
        """ Deletes a word from the Trie """
        def _delete(node, word, depth):
            if depth == len(word):  # Base case: end of word
                if not node.is_end_of_word:
                    return False  # Word not found
                node.is_end_of_word = False
                return len(node.children) == 0  # Check if node has children

            char = word[depth]
            if char not in node.children:
                return False  # Word does not exist
            
            should_delete = _delete(node.children[char], word, depth + 1)

            # If True, delete the child node
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        _delete(self.root, word, 0)

    def _find_node(self, prefix):
        """ Helper function to find the node corresponding to a given prefix """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))  # True
print(trie.search("app"))    # True
print(trie.starts_with("ap")) # True
trie.delete("apple")
print(trie.search("apple"))  # False
print(trie.search("app"))    # True (since "app" still exists)
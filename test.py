class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class PatriciaTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
        return self._get_words_from_node(current_node, prefix)

    def _get_words_from_node(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self._get_words_from_node(child, prefix + char))
        return words

# Example usage
tree = PatriciaTree()
words = ['cat', 'car', 'cart', 'dog', 'door', 'catterpillar']
for word in words:
    tree.insert(word)

print(tree.search('ca')) # ['cat', 'car', 'cart']


#This code was almost entirely written by bing chat 

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

with open('words.txt', 'r') as f:
    lines = f.readlines()
    array = [line.strip() for line in lines]

for word in array:
    tree.insert(word)


import tkinter as tk

def update_label(event):
    text_in = text_box.get("1.0", tk.END).split()[-1]
    guesses = tree.search(text_in)[0:5]
    print(guesses)
    count_label.config(text=f"Guessed words: {guesses}")

root = tk.Tk()
root.title("Character Counter")

text_box = tk.Text(root)
text_box.pack()

count_label = tk.Label(root, text="Guessed Words: ")
count_label.pack()

text_box.bind("<KeyRelease>", update_label)

root.mainloop()






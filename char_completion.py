import re
import tkinter as tk

#This code was almost entirely written by bing chat 

class Node:
    def __init__(self, weight):
        self.children = {}
        self.weight = weight
        self.is_end_of_word = False

class PatriciaTree:
    def __init__(self):
        self.root = Node(0)

    def insert(self, word, weight):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node(weight)
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
            words.append((prefix, node))
        for char, child in node.children.items():
            words.extend(self._get_words_from_node(child, prefix + char))
        return words
    

tree = PatriciaTree()

with open('words.txt', 'r') as f:
    lines = f.readlines()
    array = [line.strip().split() for line in lines]

for pair in array:
    tree.insert(pair[0], int(pair[1]))

#Tkinter app main loop

def save_weights():
    array2 = [''.join([ele[0], ' ',str(tree.search(ele[0])[0][1].weight), '\n'] ) for ele in array]
    print("updating weights")
    with open('words.txt', 'w') as f:
        f.writelines(array2)
    root.after(5000, save_weights)

def update_label(event):
    raw_text = text_box.get("1.0", tk.END)
    if(len(raw_text) > 0):
        text_in = raw_text.split()[-1]
        guesses = sorted(tree.search(text_in), key=lambda x: x[1].weight, reverse=True)[0:5]
        print([guess[1].weight for guess in guesses])
        #complete text using tab
        if('\t' in raw_text):
            updated_text = re.sub("\w*\t", guesses[0][0].rstrip('\n')+' ', raw_text)
            text_box.delete(1.0, tk.END)
            text_box.insert(1.0, updated_text)
            text_box.delete('end-1c', 'end')
            guesses[0][1].weight += 1
            
        count_label.config(text=f"Guessed words: {[guess[0] for guess in guesses]}")

root = tk.Tk()
root.title("Word Guesser (tab to complete)")

text_box = tk.Text(root, width = 100, height = 10, wrap="none")
text_box.pack()

count_label = tk.Label(root, text="Guessed Words: ")
count_label.pack()

text_box.bind("<KeyRelease>", update_label)

root.after(5000, save_weights)

root.mainloop()








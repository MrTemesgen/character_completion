#resets weights for every word, don't run unless you want that.
with open('words.txt', 'r') as f:
    lines = f.readlines()
    array = [''.join([line.strip(), ' 0\n']) for line in lines]
with open('words.txt', 'w') as f:
    f.writelines(array)
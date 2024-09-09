ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for w in ca:
    word = word.replace(w, 'X')
        
print(len(word))
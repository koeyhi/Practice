N = int(input())

if N == 1:
    print(1)
else:
    layer = 1
    rooms = 1
    
    while N > rooms:
        rooms += 6*layer
        layer += 1

    print(layer)
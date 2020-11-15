def enqueue(fila, value):
    fila.append(value)
    
def dequeue(fila):
    return fila.pop(0)


n = int(raw_input())
fila = []

for i in range(n):
    line = raw_input()
    enqueue(fila, line)

for i in range(n):
    line = dequeue(fila)
    lineSplit = line.split(" ")
    resList = []
    while(len(lineSplit) != 0):
        res = ""
        for word in lineSplit:
            if len(word) > len(res):
                res = word
        
               
        resList.append(res)
        
        if res in lineSplit:
            lineSplit.pop(lineSplit.index(res))
    print(' '.join(resList))
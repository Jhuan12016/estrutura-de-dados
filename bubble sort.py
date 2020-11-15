
def bubbleSort(a, t):
    
    for j in range(t):
        for k in range(j, t, 1):
            if a[j] < a[k]:
                aux = a[j]
                a[j] = a[k]
                a[k] = aux

    return a
    
n = int(raw_input())

for i in range(n):
    
    t = int(raw_input())
    trains = list(map(int, raw_input().split()))
    
    x = []
    
    for j in range(t):
        x.append(trains[j])
        
    trainsSort = bubbleSort(x, t)
    
    ans = 0
    
    for i in range(t):
        if trains[i] == trainsSort[i]:
            ans += 1
    
    print(ans)
    
    
    


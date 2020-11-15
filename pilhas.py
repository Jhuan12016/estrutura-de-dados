n = int(raw_input())

for i in range(n):
    codes = raw_input()
    stack = []
    ans = 0
    top = -1
    for i in range(len(codes)):
        if codes[i] == '<':
            stack.append(codes[i])
            top += 1
        if codes[i] == '>':
            if top != -1:
                if stack[top] == '<':
                    stack.pop(top)
                    top -= 1
                    ans += 1
    
    print(ans)
                
            
    
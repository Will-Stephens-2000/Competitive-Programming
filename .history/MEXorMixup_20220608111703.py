# https://codeforces.com/problemset/problem/1567/B



for t in range(int(input())):
    a, b = map(int, input().split())
    ans = a

    currXor = a-1

    rem = currXor % 4

    if rem == 1:
        currXor = 1
    elif rem == 2:
        currXor +=1
    elif rem == 3:
        curXor = 0

    
    #currXor = bin(currXor)
    currXor = format(currXor, '01000b')
    b = format(b, '01000b')

    candidate = ""
    for i in range(len(b)):
        if currXor[i] == '1' and b[i] == '1':
            candidate += '1'
        elif currXor[i] != b[i]:
            candidate += '1'
        else:
            candidate += '0'


    if b > currXor:
        ans += 1
        if int(candidate, 2) == a:
            ans += 1
    elif b < currXor:
        ans += 2
        
    print(ans)
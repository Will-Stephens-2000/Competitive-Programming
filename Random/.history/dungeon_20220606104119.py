# https://codeforces.com/problemset/problem/1463/A

for t in range(int(input())):

    a, b, c = map(int, input().split())

    k = (a + b + c)

    if k % 9 != 0:
        print("NO")
        continue
    
    k = int(k/9)

    print ("YES" if min(a, b, c) >= k else "NO")

# https://codeforces.com/problemset/problem/43/A
negInf = -10000000000000000000000
goals = {}

n = int(input())

for i in range(n):
    team = input()

    goals[team] += 1

items = goals.items()

max = negInf
currTeam = None
for tuples in items:
    if tuples[1] > max:
        max = tuples[1]
        currTeam = tuples[0]

print(currTeam)
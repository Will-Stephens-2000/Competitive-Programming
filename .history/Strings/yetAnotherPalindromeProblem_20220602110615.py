# https://codeforces.com/problemset/problem/1324/B

def isPalindrome(nums):
    revNums = nums.reverse()

    for i in range(len(nums)):
        if nums[i] != revNums[i]:
            return False
    return True

T = int(input())

for i in range(T):
    n = int(input())
    nums = list(map(int, input().split()))

    flag = False



    if flag:
        print("YES")
    else:
        print("NO")


num_cases = int(input())

for i in range(num_cases):
    nums_list = list(map(int, input().split()))
    nums_list.sort()

    if sum(nums_list) % 2 == 1:
        print("NO")
    elif nums_list[0] == nums_list[1] and nums_list[1] == nums_list[2]:
        print("YES")
    elif nums_list[0] == nums_list[1] and nums_list[2] % 2 == 0:
        print("YES")
    elif nums_list[1] == nums_list[2] and nums_list[0] % 2 == 0:
        print("YES")
    elif (nums_list[0] + nums_list[1]) == nums_list[2]:
        print("YES")
    else:
        print("NO")

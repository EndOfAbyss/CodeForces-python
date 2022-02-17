
num_cases = int(input())

for i in range(num_cases):
    total_nums = int(input())
    num_list = list(map(int, input().split()))

    ordered = True
    
    for i in range(1, total_nums):
        if num_list[i] < num_list[i-1]:
            ordered = False
            break
    
    if ordered:
        print("NO")
    else:
        print("YES")

num_cases = int(input())

for i in range(num_cases):
    total_nums = int(input())
    nums_list = list(map(int, input().split()))

    nums_list.sort()

    max_min = nums_list[0] # Será el mayor minimo en cada iteración

    for i in range(1, len(nums_list)):
        possible_min = nums_list[i] - nums_list[i-1]
        max_min = min(max_min, possible_min)
        #if possible_min > max_min:
        #    max_min = possible_min
    
    print(max_min)


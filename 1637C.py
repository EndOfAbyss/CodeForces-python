
num_cases = int(input())

for i in range(num_cases):
    total_nums = int(input())
    nums_list = list(map(int, input().split()))

    exists_num_no_zero = False
    exists_num_no_one = False
    exists_num_no_zero_no_one = False

    result = 0

    for num in nums_list[1:-1]:
        if num != 0:
            exists_num_no_zero = True
        if num != 1:
            exists_num_no_one = True
        if num != 0 and num != 1:
            exists_num_no_zero_no_one = True

        if num % 2 == 0:
            result += int(num / 2)
        else:            
            if num > 1:
                result += int((num - 1) / 2)
            
            result += 1

    if not exists_num_no_zero:
        print(0)
    elif not exists_num_no_one:
        print(-1)
    elif not exists_num_no_zero_no_one:
        print(-1)
    else:
        if total_nums == 3:
            if nums_list[1] % 2 == 0:
                print(int(nums_list[1] / 2))
            else:
                print(-1)
        else:
            print(result)


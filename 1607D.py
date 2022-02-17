
num_cases = int(input())

for i in range(num_cases):
    total_nums = int(input())
    nums_list = list(map(int, input().split()))
    color_list = list(input())

    blue_list = []
    red_list = []

    for j in range(total_nums):
        if color_list[j] == 'B':
            blue_list.append(nums_list[j])
        else:
            red_list.append(nums_list[j])
    
    blue_list.sort()
    red_list.sort()

    if len(blue_list) > 0 and blue_list[0] < 1:
        print('NO')
    elif len(red_list) > 0 and red_list[-1] > total_nums:
        print('NO')
    elif len(blue_list) > 0 and len(red_list) > 0 and red_list[0] - blue_list[-1] > 1:
        print('NO')
    else:        
        tam_B = len(blue_list)
        blue_list_2 = []
        for item in blue_list:
            if item <= tam_B:
                blue_list_2.append(item)

        tam_R = len(red_list)
        red_list_2 = []
        for item in red_list:
            if item >= total_nums - tam_B:
                red_list_2.append(item)
        
        if len(blue_list_2) > 0:
            sum_B = sum(blue_list_2)
            tam_B = len(blue_list_2)
            #last_B = blue_list[-1]

            if sum_B < tam_B * (tam_B + 1) / 2:
                print('NO')
                continue

        if len(red_list_2) > 0:
            sum_R = sum(red_list_2)
            tam_R = len(red_list_2)

            p = total_nums - tam_R

            if sum_R > total_nums * (total_nums + 1) / 2 - (p + 1) * p / 2:
                print('NO')
                continue
        
        print('YES')
    

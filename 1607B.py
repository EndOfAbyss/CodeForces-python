
num_cases = int(input())

for i in range(num_cases):
    x, num_jumps = map(int, input().split())

    if num_jumps % 4 == 0:
        last_jumps = []
    elif num_jumps % 4 == 1:
        last_jumps = [num_jumps]
    elif num_jumps % 4 == 2:
        last_jumps = [num_jumps-1, num_jumps]
    elif num_jumps % 4 == 3:
        last_jumps = [num_jumps-2, num_jumps-1, num_jumps]
    
    for jump_distance in last_jumps:
        if x % 2 == 0:
            x -= jump_distance
        else:
            x += jump_distance
    
    print(x)

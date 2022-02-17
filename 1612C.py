
num_cases = int(input())

for i in range(num_cases):
    k, x = list(map(int, input().split()))

    num_messages_max = 2 * k - 1
    num_emotes_max = k * k

    if x >= num_emotes_max:
        print(num_messages_max)
    else:
        if x <= k * (k + 1) / 2:
            extremo_inferior = (-1 + (1 + 8 * x) ** 0.5) / 2

            if extremo_inferior % 1 == 0:
                num_messages = int(extremo_inferior)
            else:
                num_messages = int(extremo_inferior + 1)
            
            print(num_messages)
        else:
            extremo_inferior = k - 0.5 - (8 * k * k - 8 * x + 1) ** 0.5 / 2
            
            if extremo_inferior % 1 == 0:
                num_messages = int(extremo_inferior)
            else:
                num_messages = int(extremo_inferior + 1)
            
            num_messages += k

            print(num_messages)



num_cases = int(input())

for i in range(num_cases):
    keyboard = input()
    s = input()

    time = 0

    position = keyboard.index(s[0])

    for j in range(1, len(s)):
        next_position = keyboard.index(s[j])
        time += abs(next_position - position)
        position = next_position

    print(time)

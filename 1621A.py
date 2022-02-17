
num_cases = int(input())

for i in range(num_cases):
    n, k = list(map(int, input().split()))

    if (n + 1) >= (2 * k):
        for j in range(n):
            if j % 2 == 0 and (j + 1) <= (2 * k):
                line = "." * j + "R" + "." * (n - j - 1)
            else:
                line = "." * n
            print(line)
    else:
        print(-1)

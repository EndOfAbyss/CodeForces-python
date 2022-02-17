
num_cases = int(input())

for i in range(num_cases):
    n, a, b = list(map(int, input().split()))

    punto_medio = (n + 1) / 2

    if (a < punto_medio and b < punto_medio) or (a > punto_medio and b > punto_medio):
        print("-1")
    elif a > n/2 + 1 or b < n/2:
        print("-1")
    else:
        numbers_list = list(range(1, n + 1))

        if a == n/2 + 1 and b == n/2:
            mitad_left = numbers_list[int(n/2):]
            mitad_right = numbers_list[:int(n/2)]
            result_list = mitad_left + mitad_right

            print(' '.join(map(str, result_list)))
        else:
            numbers_list[a-1] = b
            numbers_list[b-1] = a

            mitad_left = numbers_list[int(n/2):]
            mitad_right = numbers_list[:int(n/2)]
            result_list = mitad_left + mitad_right

            print(' '.join(map(str, result_list)))




        #numbers_list[a]


num_cases = int(input())

for i in range(num_cases):
    tam_array = int(input())
    array_1 = list(map(int, input().split()))
    array_2 = list(map(int, input().split()))

    if tam_array == 1:
        print(0)
    else:
        average_sum = (sum(array_1) + sum(array_2)) / 2
        
        last_sum = 0
        first_bucle = True

        while True:
            for j in range(tam_array):
                sum_1 = sum(array_1[:j]) + array_1[j] + sum(array_1[j+1:])
                sum_2 = sum(array_1[:j]) + array_2[j] + sum(array_1[j+1:])

                if abs(sum_1 - average_sum) > abs(sum_2 - average_sum):
                    aux = array_1[j]
                    array_1[j] = array_2[j]
                    array_2[j] = aux
            
            if first_bucle:
                first_bucle = False
                last_sum = sum(array_1)
            else:
                if last_sum == sum(array_1):
                    break
                else:
                    last_sum = sum(array_1)
    
        result = 0
        for j in range(tam_array - 1):
            for k in range(j + 1, tam_array):
                result += (array_1[j] + array_1[k]) * (array_1[j] + array_1[k])
                result += (array_2[j] + array_2[k]) * (array_2[j] + array_2[k])
        
        print(result)

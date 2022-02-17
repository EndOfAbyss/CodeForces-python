
import random
import string

letter_to_position = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 
    'K': 11, 'L':12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y':25, 'Z': 26
}

position_to_letter = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R',
    19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
}

num_cases = int(input())

for i in range(num_cases):
    #coordinates = input()
    
    mode = random.randint(1, 2)

    if mode == 1:
        row = str(random.randint(1, 100000))
        col = str(random.randint(1, 100000))

        coordinates = "R" + row + "C" + col
    else:
        tam = random.randint(1, 4)

        col = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        if tam == 4:
            col = random.choice(string.ascii_uppercase[:4]) + col

        row = row = str(random.randint(1, 100000))
        
        coordinates = col + row


    numbers = []

    pos = 0

    while pos < len(coordinates):
        num = ""

        while pos < len(coordinates) and coordinates[pos].isdigit():
            num += coordinates[pos]
            pos += 1
        
        if num:
            numbers.append(num)

        while pos < len(coordinates) and not coordinates[pos].isdigit():
            pos += 1

    if len(numbers) == 2:
        col_int_format = numbers[1]
        row = numbers[0]

        col_int_format_aux = int(col_int_format)
        col_str_format = ""

        while col_int_format_aux > 0:
            r = col_int_format_aux % 26
            if r == 0:
                r = 26
            col_str_format = position_to_letter[r] + col_str_format
            col_int_format_aux = int(col_int_format_aux / 26)

        print(col_str_format + row)
    else:
        row = numbers[0]
        col_str_format = coordinates[:len(coordinates) - len(row)]

        col_int_format = 0

        for letter in col_str_format:
            col_int_format = col_int_format * 26 + letter_to_position[letter]
        
        print("R" + row + "C" + str(col_int_format))


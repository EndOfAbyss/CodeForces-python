
num_cases = int(input())

for i in range(num_cases):
    bx, by = list(map(int, input().split()))

    if (bx + by) % 2 == 1:
        print("-1 -1")
    elif bx == 0:
        print(f"0 {int(by / 2)}")
    elif by == 0:
        print(f"{int(bx / 2)} 0")
    else:
        if bx % 2 == 0:     # Ambos son pares
            print(f"{int(bx / 2)} {int(by / 2)}")
        else:               # Ambos son impares
            if bx <= by:
                print(f"{int((bx + 1) / 2)} {int((by - 1) / 2)}")
            else:
                print(f"{int((bx - 1) / 2)} {int((by + 1) / 2)}")


def timestable():
    n = int(input("Enter number 10-99"))
    if 10 <= n <= 99:
        y = int(n / 10)
        z = n % 10
        for i in range(9):
            a = y * i
            b = z * i
            bx = int(b / 10)
            result = n * i
            print(f"{a}" + " || " + f"{b}" + " || " + f"({a} + {bx})" + " || " + f"{result}")
    else:
        print("invalid input")


if __name__ == "__main__":
    timestable()

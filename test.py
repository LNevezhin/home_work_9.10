def div():
    for i in range(2):
        try:
            x = int(input("enter a number: \n"))
            y = int(input("enter another number: \n"))
            print(x, '/', y, '=', x / y)
        except ValueError as value_err:
            print("Введите корректные данные", value_err)
        except ZeroDivisionError as zero_err:
            print("y не может быть равен '0'", zero_err)


div()

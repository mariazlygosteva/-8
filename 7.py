def get_integer_input():
    while True:
        user_input = input("Введите число: ")
        if user_input.isdigit():
            integer_input = int(user_input)
            print(f"Введено целое число: {integer_input}")
            break
        else:
            print("Ошибка. Попробуйте еще раз.")

get_integer_input()
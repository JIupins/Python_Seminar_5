# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def create_number(phrase):
    number = int(input(phrase))
    return number


def find_degree(one, two):
    if two == 0:
        return 1
    elif two == 1:
        return one
    else:
        return one * find_degree(one, two - 1)


num_one = int(create_number("Введите 1-е число: "))
num_two = int(create_number("Введите 2-е число: "))

print(f"{num_one} в степени {num_two} равно {find_degree(num_one, num_two)}.")

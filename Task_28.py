# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

def create_number(phrase):
    number = int(input(phrase))
    return number


def find_sum(one, two):
    return one if two == 0 else find_sum(one + 1, two - 1)


num_one = int(create_number("Введите 1-е число: "))
num_two = int(create_number("Введите 2-е число: "))

print(f"{num_one} плюс {num_two} равно {find_sum(num_one, num_two)}.")

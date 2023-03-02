# Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя, если только для проверки
# вашего алгоритма. На вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения.
# Например: на входе 8+6/2*3-4, на выходе 5

def multiplication(str2):
    for i in range(0, len(str2) - 1):
        if str2[i] == '*':
            num = str(int(str2[i - 1]) * int(str2[i + 1]))
            str2 = str2[:i - 1] + num + str2[i + 2:]
            return str2


def divide(str3):
    for i in range(0, len(str3) - 1):
        if str3[i] == '/':
            num = str(int(str3[i - 1]) // int(str3[i + 1]))
            str3 = str3[:i - 1] + num + str3[i + 2:]
            return str3


def addition(str4):
    for i in range(0, len(str4) - 1):
        if str4[i] == '+':
            num = str(int(str4[i - 1]) + int(str4[i + 1]))
            str4 = str4[:i - 1] + num + str4[i + 2:]
            return str4


def subtraction(str5):
    for i in range(0, len(str5) - 1):
        if str5[i] == '-':
            num = str(int(str5[i - 1]) - int(str5[i + 1]))
            str5 = str5[:i - 1] + num + str5[i + 2:]
            return str5


def calculate(str1):
    while str1.find('*') != -1:
        str1 = multiplication(str1)
    while str1.find('/') != -1:
        str1 = divide(str1)
    while str1.find('+') != -1:
        str1 = addition(str1)
    while str1.find('-') != -1:
        str1 = subtraction(str1)
    return str1


str_main = input("Введите массив: ")

print(calculate(str_main))
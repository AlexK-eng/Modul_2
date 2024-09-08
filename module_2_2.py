# This is a sample Python script.
print('Введите три целых числа:')
first = input('Первое число: ')
second = input('Второе число: ')
third = input ('Третье число: ')
if first == second and first == third :
    print(3)
elif first != second and second != third and first != third :
    print(0)
else:
    print(2)
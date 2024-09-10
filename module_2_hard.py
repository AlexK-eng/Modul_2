# This is  Additional task.

import random
n = random.randint(3, 20)
def get_password(n): # Функция вычисления пар ключей паролей.
    pass_get = []
    for i in range(1, n):
        for j in range(i, n):
            if i == j:
                continue
            if n % (i + j) == 0:
                pass_get.append([i,j])
    return pass_get

def prn_password(x): # Функция вывода пар ключей паролей в виде строки.
    print(f' {n} - ', end='')
    for i in range(len(x)):
        for j in range(2):
            print(x[i][j], end='')

result = get_password(n)
prn_password(result)

# This is  Additional task.

import random
n = random.randint(3, 20)
def get_password(n):
    pass_get = []
    for i in range(1, n):
        for j in range(i, n):
            if i == j:
                continue
            if n % (i + j) == 0:
                pass_get.append([i,j])
    return pass_get
result = get_password(n)
print(f'Key field: {n}')
for i in range(len(result)):
    print(f'Password key: {result[i]}')

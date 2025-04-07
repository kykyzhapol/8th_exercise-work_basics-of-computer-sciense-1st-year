#1st
res = []
while -1 not in res:
    res.append(int(input()))

max1 = res[0]
for i in res:
    if i > max1:
        max1 = i
print(max1)

#1st
res = []
while -1 not in res:
    res.append(int(input()))
print(len(res)-1)

#3rd
income = []
while 0 not in income:
    income.append(int(input()))

print(sum(income)/(len(income)-1))

#4th
num = int(input('enter integer number -->'))
for i in range(1, num+1):
    print(sum(range(1, i+1)))

#5th
num = int(input())
def sum_div(num):
    div = []
    for i in range(1, num):
        if num%i == 0:
            div.append(i)
    return sum(div)

perf = 0
for i in range(1, num):
    if i == sum_div(i):
        perf +=1
print(perf)

#6th
q = int(input())
for i in range(1, q+1):
    if q >= 80:
        print('слишком много')
        break
    print(' '*(q-i), '*'*i)

#7th
s = input('Введите число:')
while s.isdigit() == False:
    s = input('Ошибка. Попробуйте еще раз. Введите число:')
else:
    print(f'Введено целое число: {s}')

#8th

for i in range(1, 10):
    one = list(range(1,i+1))
    two = list(range(9, 9-i, -1))
    print(*one,sep='', end='')
    print(f'*8+{i}=', end='')
    print(*two,sep='')
print()
for i in range(1, 10):
    one = list(range(1,i+1))
    two = '1'*i
    print(*one,sep='', end='')
    print(f'*9+{i+1}=', end='')
    print(two,sep='')
print()
for i in range(1, 10):
    one = '1'*i
    two = '1'*i
    print(one,sep='', end='')
    print(f'*{two}=', end='')
    print(int(one)*int(two),sep='')

#9th
q = int(input())
def sum_div(num):
    div = []
    for i in range(1, num):
        if num%i == 0:
            div.append(i)
    return sum(div)
for i in range(1, q+1):
    if sum_div(i) == 1:
        print(i)

#10th
num = int(input())
def sum_div(num):
    div = []
    for i in range(1, num):
        if num%i == 0:
            div.append(i)
    return sum(div)

perf = 0
for i in range(1, num):
    if i == sum_div(i):
        print(i)
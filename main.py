#1st
res = []
while -1 not in res:
    res.append(int(input()))

max1 = res[0]
for i in res:
    if i > max1:
        max1 = i
print(max1)

#2nd
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
a, b = input().split()

a_case = [a]
b_case = [b]

for i in a:
    if i == '5':
        a_case.append(a.replace(i, '6'))
    elif i == '6':
        a_case.append(a.replace(i, '5'))

for i in b:
    if i == '5':
        b_case.append(b.replace(i, '6'))
    elif i == '6':
        b_case.append(b.replace(i, '5'))

a_case = list(map(int, a_case))
b_case = list(map(int, b_case))
sum_ = []

for i in a_case:
    for j in b_case:
        sum_.append(i + j)

print(min(sum_), max(sum_))
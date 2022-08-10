case = []

for _ in range(5):
    num = int(input())
    case.append(num)

print(sum(case) // len(case))
print(sorted(case)[2])
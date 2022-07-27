def abs_val(n):
    if n > 0:
        return n
    else:
        return -n

result = []
total_point = []
add_point = 0

for i in range(10):
    point = int(input())
    add_point += point
    total_point.append(add_point)

for i in range(len(total_point)):
    result.append(abs_val(100 - total_point[i]))

min_result = result[0]
for i in range(len(result)):
    if min_result >= result[i]:
        min_result = result[i]
        min_idx = i

print(total_point[min_idx])

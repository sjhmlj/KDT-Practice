'''
* stack : push & pop
'''

# 정수 k
k = int(input())

check = []

for i in range(k):
    num = int(input())
    
    if num == 0:
        check.pop()
    else:
        check.append(num)
    
print(sum(check))
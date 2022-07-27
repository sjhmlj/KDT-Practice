'''
* 셀프 넘버
'''
# 생성자 n을 가지고 수를 만들어감
# 생성자가 없는 수 => 셀프 넘버
def d(n):
    val = n
    for i in str(n):
        val += int(i)
    return val

dn = []
for i in range(1, 10000 + 1):
   
    dn.append(d(i))

print(dn)
# for i in range(1, 10000 + 1):
#     if i not in dn:
#         print(i)



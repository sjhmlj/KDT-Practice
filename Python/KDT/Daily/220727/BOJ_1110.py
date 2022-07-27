'''
* 더하기 사이클
'''

origin_num = input()
num = origin_num
cnt = 0

while True:
    temp = 0

    for digit in num:
        temp += int(digit)
    
    new_num = str(num[-1] + str(temp)[-1])
    num = new_num

    cnt += 1

    if int(new_num) == int(origin_num):
        print(cnt)
        break


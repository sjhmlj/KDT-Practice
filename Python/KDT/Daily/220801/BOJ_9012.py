'''
괄호 문자열 : (, )로만 구성
-> valid / invalid 판별

'''

t = int(input())

for i in range(t):
    case = list(input())
    stack_ = []

    for char in case:
        if char == '(':
            stack_.append(char)
        else:
            if stack_:
                stack_.pop()
            else:
                print('NO')
                break
    else:
        if not stack_:
            print('YES')
        else:
            print('NO')
# stack 문제

import sys

sys.stdin = open("_괄호짝짓기.txt")

for tc in range(1, 10 + 1):
    # 길이 n
    n = int(input())
    case = list(input())
    # 소괄호(s), 중괄호(m), 대괄호(l)
    s_left = []
    m_left = []
    l_left = []

    flag = True
    for i in range(len(case)):
        if case[i] == '(':
            s_left.append(case[i])
        elif case[i] ==')':
            if s_left:
                s_left.pop()
            else:
                flag = False
                break

        if case[i] == '{':
            m_left.append(case[i])
        elif case[i] == '}':
            if m_left:
                m_left.pop()
            else:
                flag = False
                break
  
        if case[i] == '[':
            l_left.append(case[i])
        elif case[i] == ']':
            if l_left:
                l_left.pop()
            else:
                flag = False
                break

    result = 1 if flag else 0
    print('#{} {}'.format(tc, result))
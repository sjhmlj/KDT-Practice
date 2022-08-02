'''
문자열이 주어졌을 때 괄호들의 균형이 잘 맞춰져있는지 판단
-> 소괄호, 대괄호 2종류
-> 무조건 연속적으로 짝을 이루어 이어져야함
'''
import sys
input = sys.stdin.readline

while True:
    text = input().rstrip()

    stack = []
    result = True    
    
    if text == '.':
        break
    
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = False
                break

        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = False
                break


    if result and len(stack) == 0:
        print('yes')
    else:
        print('no')
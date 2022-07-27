'''
오타를 낸 문장과 위치가 주어짐
오타를 지워 출력
오타는 반드시 하나
'''

# slicing의 조작만으로도 가능

T = int(input())

for i in range(T):
    case = input().split()
    num = int(case[0])
    text = list(case[1])
    # replace 는 해당 요소를 전부 선택함
    text.pop(num-1)
    
    print(''.join(text))




'''
처음 색 2개 = 저항값 <= 문자열로 연결
마지막 색 = 곱해야하는 값 

'''
color = [
        'black', 'brown', 'red', 'orange', 'yellow', 'green',
        'blue', 'violet', 'grey', 'white'
        ]

c1 = str(color.index(input()))
c2 = str(color.index(input()))
c3 = 10 ** color.index(input())

print(int(c1 + c2) * c3)
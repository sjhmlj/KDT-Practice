'''
* I : 숫자 개수 n  / 공백없이 숫자 n개
* O : 숫자의 합
* map() method의 iterable에 str오는 것 유의
'''
# list 접근
n = int(input())

case = sum(list(map(int, input())))
print(case)

# str 접근, for문
case = input()  
result = 0

for num in case:
    result += int(num)

print(result)

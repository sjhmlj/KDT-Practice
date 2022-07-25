'''
* I : 두 수 a, b (not same)
* O : 거꾸로 읽어서 큰 수 출력
'''

a, b = input().split()

reversed_a = int(a[::-1])
reversed_b = int(b[::-1])

result = reversed_a if reversed_a > reversed_b else reversed_b

print(result)

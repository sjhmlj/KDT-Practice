'''
* 뒤집힌 덧셈
* slicing, casting 적절히 활용
'''

def Rev(n):
    result = n[::-1]
    return int(result)

x, y = input().split()

print(Rev(str(Rev(x) + Rev(y))))


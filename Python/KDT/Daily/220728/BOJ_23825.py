'''
* SASA 모형 만들기
'''
n, m = map(int, input().split())
print(min(n // 2, m // 2))

# n, m = map(int, input().split())

# cnt = 0 

# while n >= 2 and m >= 2:
    
#     if n - 2 >= 0 and m - 2 >= 0:
#         cnt += 1
    
#     n -= 2
#     m -= 2

# print(cnt)
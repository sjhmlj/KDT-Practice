a, b = map(int, input().split())

a -= 1
b -= 1

x = abs(b // 4 - a // 4)
y = abs(b % 4 - a % 4)
print(x + y)

# i = 0
# cnt = 0

# while True:

#     a_ = a + (4 * i)

#     if a_ == b:
#         break

#     elif a_ == b - 1:
#         cnt += 1
#         break
    
#     elif a_ > b:
#         while a_ != b:
#             a_ -= 1
#             cnt += 1
#         print(cnt)
#         exit(0)
#     i += 1
#     cnt += 1

# print(cnt)


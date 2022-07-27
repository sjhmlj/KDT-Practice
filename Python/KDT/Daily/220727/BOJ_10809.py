s = input()
result = []

for i in range(ord('a'), ord('z') + 1):
    if  chr(i) in s:
        result.append(s.index(chr(i)))
    else:
        result.append(-1) 

for n in result:
    print(n, end=' ')
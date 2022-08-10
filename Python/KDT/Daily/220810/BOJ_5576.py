'''
w 10
k 10

'''
w = []
k = []

for _ in range(10):
    w.append(int(input()))

for _ in range(10):
    k.append(int(input()))

w = sum(sorted(w, reverse=True)[:3])
k = sum(sorted(k, reverse=True)[:3])

print(w, k)
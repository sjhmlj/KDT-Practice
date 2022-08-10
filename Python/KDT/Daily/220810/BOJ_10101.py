list_ = []

for _ in range(3):
    angle = int(input())
    list_.append(angle)

result = sum(list_)
 
if result != 180:
    ans = 'Error'
elif list_[0] == list_[1] == list_[2]:
    ans = 'Equilateral'
elif list_[0] == list_[1] or list_[0] == list_[2] or list_[1] == list_[2]:
    ans = 'Isosceles'
else:
    ans = 'Scalene'
    
print(ans)
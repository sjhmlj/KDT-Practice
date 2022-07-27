'''
* 태보태보 총난타
'''
s = input()
punch = s.split('(^0^)')

left = punch[0].count('@')
right = punch[1].count('@')

print(left, right)

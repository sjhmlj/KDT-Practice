text = input().replace(' ', '')

imoji1 = text.count(':-)')
imoji2 = text.count(':-(')

if imoji1 == 0 and imoji2 == 0:
    print('none')
elif imoji1 == imoji2:
    print('unsure')
elif imoji1 > imoji2:
    print('happy')
elif imoji1 < imoji2:
    print('sad')
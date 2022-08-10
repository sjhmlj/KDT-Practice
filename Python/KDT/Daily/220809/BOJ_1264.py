target = 'aeiou'

while True:
    text = input().lower()
    cnt = 0

    if text == '#':
        break

    for char in text:
        if char in target:
            cnt += 1
    
    print(cnt)
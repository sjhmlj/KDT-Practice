import sys

sys.stdin = open('input_6996.txt', 'r')

tc = int(input())

for _ in range(tc):
    front, back = input().split()
    
    front_ = sorted(list(front))
    back_ = sorted(list(back))

    result = True if front_ == back_ else False

    if result:
        print('{} & {} are anagrams.'.format(front, back))
    else:
        print('{} & {} are NOT anagrams.'.format(front, back))
    
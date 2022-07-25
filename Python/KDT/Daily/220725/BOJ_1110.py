'''
* 문제 : 더하기 사이클 (새로운 수를 만들어가며 자기 자신이 나올 때 까지 카운팅)
* 접근
    * 0 <= n <= 99
    * 각 자릿수를 더하고 마지막 피연산자와 그대로 이어붙여 수를 만듬
    * 조건에 대한 반복이 적절하여 while loop
'''

n = int(input())  
original_n = n  
cnt = 0

while True:
    plus_num = (n // 10) + (n % 10)   
    new_num = int(str(n % 10) + str(plus_num)[-1]) 
    n = new_num  

    if original_n == n:
        cnt += 1
        break
    
    cnt += 1

print(cnt)

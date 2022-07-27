'''
absolutes : 정수들의 절댓값을 차례대로 담음
sigins : 정수들의 부호를 차례대로 담음
실제 정수들의 합을 구하시오
'''
def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

absolutes = [4, 7, 12]
signs = [True, False, True]

print(solution(absolutes, signs))
def solution(s):
    table = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine'
        ]   

    for i in range(len(table)):
        if table[i] in s:
            s = s.replace(table[i], str(i))
    
    answer = int(s)
    
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
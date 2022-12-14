# 🎞 후기
- 자료구조에 대한 수업이 끝나고 알고리즘 단계로 넘어옴
- two dimensional list에 대한 내용이었고 전반적으로 평이한 수준이었다고 생각한다
- 주어진 자료를 2차원으로 해석할 수 있는 힘을 기를 수 있었다
- 여태까지 발생하였던 `시간초과`문제를 해결하기 위한 수단이 많이 추가되었음
    1. `import sys`를 통해 input 정의
    2. `PyPy3`로 소스코드 실행

## 💎 가장 강렬했던 문제
- 맞왜틀을 수차례 외치게 만든 [BOJ_1236](./BOJ_1236.py)
- input에 따른 output이 일치하였으나 시간초과도 아닌 `틀렸습니다`의 메시지를 받음
- 즉, 복잡도 또는 사용한 문법의 문제가 아닌 코드 자체에 문제가 있음을 확인할 수 있었음
- 실행 프로그램을 PyPy로 바꿔보거나 for문의 반복을 줄여보는 방식을 시도했으나 본질적으로 해결할 수 없었고 결국 디버깅을 진행, 단순 `index error`를 확인할 수 있었고 수정하여 성공적으로 제출
###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) "사람 수", smoking "흡연 여부" FROM healthcare WHERE smoking != '' GROUP BY smoking;

사람 수    흡연 여부
------  -----
626138  1
189808  2
183711  3
```
 
###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT COUNT(*) "사람 수", is_drinking "음주 여부" FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;

사람 수    음주 여부
------  -----
415119  0
584685  1
```
 
### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

```sql
SELECT count(*) "사람 수", is_drinking "음주 여부" FROM healthcare WHERE blood_pressure >= 200 GROUP BY is_drinking;

사람 수  음주 여부
----  -----
6064  0
1770  1
```

### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

```sql
SELECT sido "sido code", COUNT(*) "인구" FROM healthcare GROUP BY sido HAVING COUNT(*) >= 50000;

sido code  인구
---------  ------
11         166231
26         69025
28         58345
41         247369
47         54438
48         68530
```

### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
SELECT height "신장", COUNT(*) "사람 수" FROM healthcare GROUP BY height ORDER BY COUNT(*) DESC LIMIT 5;

신장   사람 수
---  ------
160  184993
155  181306
165  179352
170  152585
150  128555
```

### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
SELECT weight "몸무게", height "키", COUNT(*) "사람 수" FROM healthcare GROUP BY height, weight ORDER BY COUNT(*) DESC LIMIT 5;

몸무게  키    사람 수
---  ---  -----
55   155  45866
60   160  42454
65   165  40385
50   155  38582
55   160  38066
```

### 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

```sql 
SELECT is_drinking "음주", waist "둘레", COUNT(*) "수" FROM healthcare WHERE is_drinking != '' GROUP BY is_drinking;

음주  둘레    수
--  ----  ------
0   72.1  415119
1   94.0  584685
``` 

### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
SELECT gender, round(AVG(va_left), 2) "평균 왼쪽 시력", round(AVG(va_right), 2) "평균 오른쪽 시력" FROM healthcare GROUP BY gender; 

gender  평균 왼쪽 시력  평균 오른쪽 시력
------  --------  ---------
1       0.98      0.99
2       0.88      0.88
```

### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
SELECT age, round(AVG(height), 2) "평균 키", round(AVG(weight), 2) "평균 몸무게" FROM healthcare GROUP BY age;
HAVING AVG(height) >= 160 AND AVG(weight) >= 60;

age  평균 키    평균 몸무게
---  ------  ------
9    165.67  67.24
10   164.12  65.68
11   162.11  63.9
12   160.65  62.6
```

### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql
SELECT is_drinking, smoking, round(weight/((height * 0.01)*(height * 0.01)), 3) BMI FROM healthcare WHERE is_drinking != '' AND smoking != '' GROUP BY is_drinking, smoking;

is_drinking  smoking  BMI
-----------  -------  ------
0            1        22.039
0            2        22.857
0            3        25.391
1            1        29.297
1            2        25.952
1            3        24.836
```
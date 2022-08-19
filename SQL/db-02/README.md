# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age), MIN(age) FROM healthcare;
```

```
MAX(age)  MIN(age)
--------  --------
18        9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT max(height), min(height), max(weight), min(weight) FROM healthcare;
```

```
max(height)  min(height)  max(weight)  min(weight)
-----------  -----------  -----------  -----------
195          130          135          30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE height  BETWEEN 160 AND 170;
-- 또는
SELECT COUNT(*) FROM healthcare WHERE height >= 160 AND height <= 170;
```

```
COUNT(*)
--------
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
-- 서브쿼리 활용
SELECT id, waist, is_drinking FROM (SELECT * FROM healthcare WHERE waist IS NOT '') WHERE is_drinking = 1 ORDER BY waist DESC LIMIT 5;

```

```
id      waist  is_drinking
------  -----  -----------
993531  146.0  1
87897   142.0  1
826643  141.4  1
567314  140.0  1
611146  140.0  1
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE (va_left >= 1.5 AND va_right >= 1.5) AND is_drinking = 1;
```

```
COUNT(*)
--------
36697
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE blood_pressure < 120;
```

```
COUNT(*)
--------
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
AVG(waist)
----------------
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;
```

```
AVG(height)       AVG(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1, 1;
```

```
id      height  weight
------  ------  ------
836005  195     110
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare WHERE (weight)/((height*0.01)*(height*0.01)) >= 30;
```

```
COUNT(*)
--------
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, (weight)/((height*0.01)*(height*0.01)) as BMI FROM healthcare WHERE smoking = 3 ORDER BY (weight)/((height*0.01)*(height*0.01)) DESC LIMIT 5; 
```

```
id      BMI
------  ----------------
231431  50.78125
934714  49.9479708636837
722707  48.828125
947281  47.7502295684114
948801  47.7502295684114
```

### 13. (자유) 술을 마시면서 흡연 지수 1이상인 사람의 수

```sql
SELECT count(*) FROM healthcare WHERE is_drinking = 1 AND smoking >= 1;
```

```
count(*)
--------
584685
```

### 14. (자유) 양쪽 시력 모두 1.0 미만인 사람의 수

```sql
SELECT COUNT(*) FROM healthcare WHERE (va_left < 1.0 AND va_right < 1.0);
```

```
COUNT(*)
--------
432797
```

### 15. (자유) 키가 180 이상 200 이하이면서 몸무게가 80 kg 이상인 사람의 수

```sql
SELECT COUNT(*) FROM healthcare WHERE (height  BETWEEN 180 AND 200) AND (weight >= 80);
```

```
COUNT(*)
--------
18786
```
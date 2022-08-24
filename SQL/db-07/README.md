# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.

</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드
> 

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```

### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```

### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name | debut | country |
| --- | --- | --- |
| 봉준호 | 1993-01-01 | KOR |
| 김한민 | 1999-01-01 | KOR |
| 최동훈 | 2004-01-01 | KOR |
| 이정재 | 2022-01-01 | KOR |
| 이경규 | 1992-01-01 | KOR |
| 한재림 | 2005-01-01 | KOR |
| Joseph Kosinski | 1999-01-01 | KOR |
| 김철수 | 2022-01-01 | KOR |

> 코드 작성
> 

```python
Director.objects.create(name = '봉준호', debut = '1993-01-01', country = 'KOR')
Director.objects.create(name = '김한민', debut = '1999-01-01', country = 'KOR')
Director.objects.create(name = '최동훈', debut = '2004-01-01', country = 'KOR')
Director.objects.create(name = '이정재', debut = '2022-01-01', country = 'KOR')
Director.objects.create(name = '이경규', debut = '1992-01-01', country = 'KOR')
Director.objects.create(name = '한재림', debut = '2005-01-01', country = 'KOR')
Director.objects.create(name = 'Joseph Kosinski', debut = '1999-01-01', country = 'KOR')
Director.objects.create(name = '김철수', debut = '2022-01-01', country = 'KOR')
```

### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title |
| --- |
| 액션 |
| 드라마 |
| 사극 |
| 범죄 |
| 스릴러 |
| SF |
| 무협 |
| 첩보 |
| 재난 |

> 코드 작성
> 

```python
# 리스트로도 가능할듯
genres = ['액션', '드라마', '사극', '범죄', '스릴러', 'SF', '무협', '첩보', '재난']

for name in gernres:
    genre = Genre()
    genre.title = name
    genre.save()

# 직접 인스턴스 조작
genre = Genre()
genre.title = '액션'
genre.save()
genre = Genre()
genre.title = '드라마'
genre.save()
genre = Genre()
genre.title = '사극'
genre.save()
genre = Genre()
genre.title = '범죄'
genre.save()
genre = Genre()
genre.title = '스릴러'
genre.save()
genre = Genre()
genre.title = 'SF'
genre.save()
genre = Genre()
genre.title = '무협'
genre.save()
genre = Genre()
genre.title = '첩보'
genre.save()
genre = Genre()
genre.title = '재난'
genre.save()
```

### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
for info in Director.objects.all() :
    print(info.name, info.debut, info.country)
```

### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
target = Director.objects.get(id=1)
print(target.name, target.debut, target.country)
```

### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(country='USA')
```

### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
DoesNotExist: Director matching query does not exist.
```

> 이유 작성
> 

```
Director table안에 없는 정보를 조회하여 해당 오류 메시지 출력
```

### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성
> 

```python
target = Director.objects.get(name = 'Joseph Kosinski')
target.country = 'USA'
target.save()

# 변경 확인
print(target.name, target.debut, target.country)
```

### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(country='KOR')
```

### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지
> 

```bash
MultipleObjectsReturned: get() returned more than one Director -- it returned 7!
```

> 이유 작성
> 

```
get method는 1개의 값만 리턴을 해야하는데 리턴값이 1개 초과(해당 문제의 경우 7개)하여 오류 메시지 출력
```

### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시
> 

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성
> 

```python
target = Director.objects.filter(country = 'KOR')
typeof(target)

for x in target:
    print(x.name, x.debut, x.country)
```

### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
두 메소드에 대하여 type()을 적용하는 경우
- get() : db.models.Director (director 객체 하나)
- filter() : django.db.models.query.QuerySet (queryset으로 반환)

따라서, get()은 객체 한 개를 반환하는 반면 filter()의 경우 부합하는 모든 객체를 모아서 리스트 형식으로 반환한다
```

### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성
> 

```python
Director.objects.get(name = '김철수').delete()

# 메시지
# (1, {'db.Director': 1})
```
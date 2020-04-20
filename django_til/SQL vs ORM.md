# SQL과 django ORM

## 참고문서

[Making queries | Django documentation | Django](https://docs.djangoproject.com/en/2.2/topics/db/queries/#making-queries)

[QuerySet API reference | Django documentation | Django](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#queryset-api-reference)

[Aggregation | Django documentation | Django](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation)

## **기본 준비 사항**

> Gitlab에서 프로젝트를 다운받으면 아래의 내용이 이미 반영되어 있습니다.

- django app
    - `django_extensions` 설치
    - `users` app 생성
    - csv 파일에 맞춰 `models.py` 작성 및 migrate

            $ python manage.py sqlmigrate users 0001

- `db.sqlite3` 활용 및 데이터 반영
    - `sqlite3` 실행

            $ ls
            db.sqlite3 manage.py ...
            $ sqlite3 db.sqlite3

    - csv 파일 data 로드

            sqlite > .tables
            auth_group                  django_admin_log
            auth_group_permissions      django_content_type
            auth_permission             django_migrations
            auth_user                   django_session
            auth_user_groups            auth_user_user_permissions
            users_user
            sqlite > .mode csv
            sqlite > .import users.csv users_user
            sqlite > SELECT COUNT(*) FROM users_user;
            1000

- 확인
    - sqlite3에서 스키마 확인

            sqlite > .schema users_user

## **문제**

> 아래의 문제들을 sql문과 대응되는 orm을 작성 하세요.

### Table 생성

- django

    ```python
    # django
    class User(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        age = models.IntegerField()
        country = models.CharField(max_length=10)
        phone = models.CharField(max_length=15)
        balance = models.IntegerField()
    ```

- SQL
    - sql.sqlite3에 동일하게 테이블 생성

        ```sql
        --sql
        CREATE TABLE users_user (
        	id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            country TEXT NOT NULL,
            phone TEXT NOT NULL,
            balaence INTEGER NOT NULL,
        );
        ```

### 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   User.objects.all().count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(
   	first_name = 'unani',
       last_name = 'Jung'
       ...
       ...
       ...
   )
   ```

   ```sql
   -- sql
   INSERT INTO users_user(
   	id,first_name,last_name....)
   VALUES(
   	'unani','jung',....);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   ```python
   # orm
   User.objects.get(pk=101)
   ```

      ```sql
   -- sql
   SELECT * FROM users_user WHERE id=101
      ```

4. 해당 user 레코드 수정

   ```python
   # orm
   user = User.objects.get(pk=101)
   user.first_name = 'unani'
   user.save()
   ```

      ```sql
   -- sql
   UPDATE users_user
   SET last_name='Choi'
   WHERE first_name='unani';
      ```

5. 해당 user 레코드 삭제

   ```python
   # orm
   user.delete()
```
   
      ```sql
   -- sql
   DELETE FROM users_user 
   WHERE first_name = 'unani';
      ```

### 조건에 따른 쿼리문

1. 전체 인원 수

   ```python
   # orm
   User.objects.count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
      ```

2. 나이가 30인 사람의 이름

   ```python
   # orm
   User.objects.filter(age=30)
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
   WHERE age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   ```python
   # orm
    User.objects.filter(age__gte = 30).count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user
   WHERE age>=30;
      ```

4. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30,last_name='김').count()
   User.objects.filter(age=30).filter(last_name='김').count()
   ```

      ```sql
   -- sql
   select count(*) from users_user
   where age=30 and last_name='김' ;
      ```

5. 지역번호가 02인 사람의 인원 수

   > https://docs.djangoproject.com/en/2.2/topics/db/queries/#escaping-percent-signs-and-underscores-in-like-statements

   ```python
   # orm
   User.objects.filter(
   	phone__startswith='02-'
   ).count()
   ```

   - (`iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith` and `iendswith`)
     - `i~~ `: 대소문자 구분하지 않음
     - `exact` : 완전 일치하는 것을 필터링
     - `contains` : 대소문자 구분은 하지만 해당 내용을 **포함하는** 것을 필터링
     - `startswith` : 해당 내용으로 시작하는 것
     - `endswith` : 해당 내용으로 끝나는 것 

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user
   WHERE phone LIKE '02-%'
      ```

6. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter(first_name='황',country='강원도').first_name
```
   
      ```sql
   -- sql
   SELECT first_name FROM users_user
   WHERE first_name='황' AND country='강원도'
      ```



### 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람 10명

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. 잔액이 적은 사람 10명

   ```python
   # orm
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
   ORDER BY age DESC
   LIMIT 10;
      ```

3. 성, 이름 내림차순 순으로 5번째 있는 사람

      ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
   ORDER BY last_name DESC, first_name DESC
   LIMIT 1 OFFSET 4
   -- 1개만 보여주세요..... 4번에 있는 것(0부터 시작하니깐)
      ```



### 표현식

> 표현식을 위해서는 [aggregate]([https://docs.djangoproject.com/en/2.2/topics/db/aggregation/](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/)) 를 알아야한다.

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.aggregate(AVG('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   User.objects.filter(last_name = '김').aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user WHERE last_name='김';
      ```

3. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   SELECT MAX(balance) FROM users_user;
      ```

4. 계좌 잔액 총액

      ```python
   # orm
   User.objects.aggregate(Sum('balance'))
```
   
      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```



### Group by

> annotate는 개별 item에 추가 필드를 구성한다.
> 추후 1:N 관계에서 활용된다.

1. 지역별 인원 수

   ```python
   # orm
   User.objects.values('country').annotate(Count('country'))
```
   
   ```sql
   -- sql
   SELECT country,COUNT(country) FROM users_user
   GROUP BY country;
   ```


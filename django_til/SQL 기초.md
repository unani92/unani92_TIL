# SQL 기초

![image](https://user-images.githubusercontent.com/53211781/79714840-f6b31880-830c-11ea-8d33-338091a67e7e.png)

### 1. flights 테이블 생성하기

```sql
CREATE TABLE flights(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	flight_num TEXT NOT NULL,
	departure TEXT NOT NULL,
	waypoint TEXT NOT NULL,
	arrival TEXT NOT NULL,
	price INTEGER NOT NULL);
```

#### 주의사항 

1. 반드시 그래야 하는 것은 아니나 **가독성을 위해** 변수명은 소문자, **명령어는 대문자**를 컨벤션으로 한다. 
2. 파이썬과 달리 **끝나는 부분은 쉼표를 붙이지 않는다.**
3. 구문의 끝은 반드시 `;` 으로 마친다. 



### 2. 데이터 입력하기

#### 1번 방식 : 넣고자 하는 칼럼을 모두 적어주고 내용을 모두 적어준다.

```sql
INSERT INTO filghts (id, flight_num, departure, waypoint,arrival,price) 
VALUES (1,'RT9122','Madrid','Beijing','Incheon',200);
```

#### 2번 방식 : 칼럼을 특정하지 않으면 모든 칼럼에 해당 내용들이 매칭된다. 

```sql
INSERT INTO filghts VALUES (2,'XZ0352','LA','MOSCOW','Incheon',200);
```

#### 3번 방식 : id 값을 빼고 특정했지만 `AUTOINCREMENT`로 인해 자동 반영된다.

```sql
INSERT INTO filghts (flight_num, departure, waypoint, arrival, price)
VALUES ('SQ0972', 'London', 'Beijing', 'Sydney', 500);
```



### 3. 테이블 전체 데이터를 조회하기

```sql
SELECT * FROM flights ;
```

- `*`은 모든 칼럼을 의미하고 flights의 모든 row를 보여준다.

- 특정 칼럼을 보고 싶은 경우 `*`에 칼럼명을 기재한다. 

  - 예) 모든 waypoint 조회하기

    ```sql
    SELECT waypoint FROM flights;
    
    -- 중복 없이 출력하기
    SELECT DISTINCT waypoint FROM flights;
    ```



### 4. 조건에 맞는 데이터 조회하기

- 항공권 가격 500 이상의 항공편의 id, flight_num 조회하기

  ```sql
  SELECT id, flight_num FROM filghts WHERE price < 600;
  ```



### 5. 와일드카드 사용하기

- 숫자부분이 0으로 시작하고 2로 끝나면서 경유지가 Beijing 항공편의 id, flight_num 조회하기

  ```sql
  SELECT id, flight_num FROM flights WHERE flight_num LIKE '__0__2' AND waypoint='Beijing';
  ```

  - `_` : 1글자 아무거나
  - `%` : 글자 수 상관 없이 아무거나



### 6. 데이터 수정하기

- 항공편 SQ0972의 경유지를 Tokyo로 수정

  ```sql
  UPDATE flights SET waypoint='Tokyo' WHERE flight_num='SQ0972';
  ```

  - 테이블 flights에서 Tokyo로 waypoint를 바꿔라
  - flight_num이 'SQ0972인 row의'



### 7. row 삭제하기

- 항공편 RT9122를 테이블에서 삭제

  ```sqlite
  DELETE FROM flights WHERE flight_num='RT9122'
  ```

  - flights 테이블에서 삭제해라
  - flight_num이 RT9122인 row를



### 8. 테이블 삭제하기

```sql
DROP TABLE flights
SELECT * FROM flights

--Error: no such table: flights
```
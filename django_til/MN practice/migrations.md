# migrations 

```bash
$ python manage.py makemigrations
# default값 없이 NOT NULL를 지정 => 기존 레코드에 값이 필요하다.
You are trying to add a non-nullable field 'image' to article without a default; we can't do that (the database needs something to populate existing rows).
# 2가지 옵션 제시
Please select a fix:
 # 1) 디폴트 값을 지금 설정 => python console
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 # 2) 종료하고 직접 models.py에 default 설정
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
```




![1_ePn61nZEatSdCPKVl5yxZQ](https://user-images.githubusercontent.com/89339349/141935627-71b33a42-d56a-4778-9312-09c57eccecdb.png)

# 원티드x위코드 백엔드 프리온보딩 과제 5.



> ## [Assignment] 과제 제출 기업정보



- 기업명 : Humanscape
- [Humanscape 웹사이트 링크](https://humanscape.io/kr/)
- [원티드 채용공고 링크](https://www.wanted.co.kr/wd/41413)





> ## Members



| 이름       | Github                                          | 담당 기능                                                    |
| ---------- | ----------------------------------------------- | ------------------------------------------------------------ |
| 👨🏻‍🎤 김주현 | [kjhabc2002](https://github.com/kjhabc2002)     | DB data control,  AWS / Docker 배포                          |
| 👨🏻‍🦳 양가현 | [chrisyang256](https://github.com/chrisyang256) | 최근 일주일내에 업데이트 된 임상정보 리스트 view, unit test  |
| 👶🏻 구본욱  | [qhsdnr0](https://github.com/qhsdnr0)           | 특정 임상정보 읽기 view, unit test, postman api              |
| 👰🏻‍♂️ 이다빈 | [thisisempty](https://github.com/thisisempty)   | 임상정보 검색 view, unit test, postman api                   |
| 🦹🏻‍♂️ 문승준 | [palza4dev](https://github.com/palza4dev)       | 임성정보를 수집하는 batch task view,  postman api, README 작성 |
| 🥷 김지훈   | [kimfa123](https://github.com/kimfa123)         | 임성정보를 수집하는 batch task view,  postman api, README 작성 |

ㅤ👪 공동작업: DB Modeling





> ## 사용 기술



[![Python](https://camo.githubusercontent.com/a1b2dac5667822ee0d98ae6d799da61987fd1658dfeb4d2ca6e3c99b1535ebd8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)](https://camo.githubusercontent.com/a1b2dac5667822ee0d98ae6d799da61987fd1658dfeb4d2ca6e3c99b1535ebd8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)ㅤ[![Django](https://camo.githubusercontent.com/5473e0d3006bb7e662bdf754d830a026ce050be61f1cbbd4689783ae49950b93/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d2532333039324532302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/5473e0d3006bb7e662bdf754d830a026ce050be61f1cbbd4689783ae49950b93/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d2532333039324532302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d7768697465)ㅤ[![SQLite](https://camo.githubusercontent.com/b310667470594171440f9b80f624787ea58555296d88af177788509b0d73a40b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d2532333037343035652e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/b310667470594171440f9b80f624787ea58555296d88af177788509b0d73a40b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d2532333037343035652e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d7768697465)ㅤ[![AWS](https://camo.githubusercontent.com/9281daa5684971fd3325661e3dd5fea86b21a902e3741a556fb636fbf0e2f3d4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4157532d2532334646393930302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e2d617773266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/9281daa5684971fd3325661e3dd5fea86b21a902e3741a556fb636fbf0e2f3d4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4157532d2532334646393930302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e2d617773266c6f676f436f6c6f723d7768697465)ㅤ[![Docker](https://camo.githubusercontent.com/6b7f701cf0bea42833751b754688f1a27b6090fdf90bf2b226addff01be817f0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f636b65722d2532333064623765642e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/6b7f701cf0bea42833751b754688f1a27b6090fdf90bf2b226addff01be817f0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f636b65722d2532333064623765642e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465)ㅤ[![Postman](https://camo.githubusercontent.com/3f0e26b0951bab845a1bb9a7198ecca0da272e462921b6edd85879f3673b6927/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d706f73746d616e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/3f0e26b0951bab845a1bb9a7198ecca0da272e462921b6edd85879f3673b6927/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d706f73746d616e266c6f676f436f6c6f723d7768697465)ㅤ[![GitHub](https://camo.githubusercontent.com/f6d50128cb007f85916b7a899da5d94f654dce35a37331c8d28573aef46f4274/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333132313031312e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/f6d50128cb007f85916b7a899da5d94f654dce35a37331c8d28573aef46f4274/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333132313031312e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)





> ## 과제 내용



ㅤ아래 요구사항에 맞춰 임상정보 관리 Restfull API를 개발합니다.



### ▶︎ 필수 포함사항

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현



### ▶︎ 확인 사항

- **ORM 사용 필수**
- **데이터베이스는 SQLite로 구현**
- **secret key, api key 등을 레포지토리에 올리지 않도록 유의**
- **[README.md](http://README.md) 에 관련 설명 명시 필요**



### ▶︎도전 과제: 스스로에게도 도움이 되는 내용 + 추가 가산점

- **배포하여 웹에서 사용 할 수 있도록 제공 **
- **임상저보 검색 API 제공**



### ▶︎과제 안내

다음 사항들을 충족하는 서비스를 구현해주세요.

- **임상정보를 수집하는 batch task**
  - 참고 : https://www.data.go.kr/data/3074271/fileData.do#/API목록/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887

- **수집한 임상정보에 대한 API**
  - 특정 임상정보 읽기(키 값은 자유)

- **수집한 임상정보 리스트 API**
  - 최근 일주일내에 업데이트(변경사항이 있는) 된 임상정보 리스트
    - Pagination 기능 


- **Test 구현시 가산점이 있습니다.**





> ## 모델링



![image](https://user-images.githubusercontent.com/89339349/141937912-e78ce3d3-a04d-4cf1-9b6b-af4517b6ce37.png)



> ## 구현 기능 

### ▶︎ 임상정보를 수집하는 batch task

- [임상연구 과제정보](https://www.data.go.kr/data/3074271/fileData.do#/API%20%EB%AA%A9%EB%A1%9D/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887) 오픈API를 이용해 주기적으로 데이터를 저장 및 수정하는 batch 기능 구현하였습니다.

- `django-crontab`을 활용해 background batch scheduler를 만들었고 매일 자정시간에 해당 API로 요청을 보냅니다.

- 첫번째 요청의 응답으로 전체 데이터 수량을 확인하고 두번째 요청의 응답으로 전체 데이터를 받아옵니다.

- tasks 테이블의 외래키로 설정된 데이터는 `get_or_create` 메소드로 생성 혹은 선택하고, 존재하지 않는 경우 if문 삼항연산자를 이용해 None 값을 객체에 담습니다.

- 데이터의 고유한 과제번호를 기준으로 이미 존재하는 데이터는 update 해주고, 신규 데이터는 create하여 데이터베이스에 저장합니다. 

  


### ▶︎ 임상정보 검색 API 

- `/task/search?` 뒤에 위치한 query parameters를 분석하여 검색 결과를 리턴합니다.

- pagenation을 위해 `offset` 과 `limit` 값이 필요합니다.

- 사용할 수 있는 query parameters의 키는 다음과 같습니다.

  | key                       | value example | 결과                                                         |
  | ------------------------- | ------------- | ------------------------------------------------------------ |
  | title(과제명)             | 한국인        | 유저가 입력한 과제명이 포함되는 데이터를 리턴합니다.         |
  | department(진료과)        | psychiatry    | 유저가 입력한 진료과와 정확히 일치하는 데이터를 리턴합니다. 대소문자는 구분하지 않습니다. |
  | institute(연구책임기관)   | 가톨릭대      | 유저가 입력한 연구책임기관을 포함하는 데이터를 리턴합니다.   |
  | type(연구종류)            | 관찰연구      | 유저가 입력한 연구종류와 정확히 일치하는 데이터를 리턴합니다. |
  | trial_stage(임상시험단계) | Case-only     | 유저가 입력한 임상시험 단계와 정확히 일치하는 데이터를 리턴합니다. 대소문자는 구분하지 않습니다. |
  | scope(연구범위)           | 단일기관      | 유저가 입력한 연구범위와 정확히 일치하는 데이터를 리턴합니다. |



### ▶︎ 수집한 임상정보에 대한 API

- `/tasks/<int:task_id>`로 URI에 입력되는 임상정보 id에 해당하는 임상정보를 조회합니다.



### ▶︎ 임상정보 업데이트 리스트 API

- 검색을 실행하는 해당 날짜를 기준으로 최근 7일간 업데이트 된 내용일 있는 경우에 대한 임상정보만 반환



### ▶︎ UnitTest

- 검색기능을 통한 리스트 출력에서 테스트의 신뢰성을 높이기 위해 Local Database를 활용해 UnitTest를 진행하였습니다.
- 테스트에 사용되는 Database는 humanscape.settings_test에 test_db.sqlite3로 명시했습니다.
- 터미널에서 ```python manage.py test tasks --settings='humanscape.settings_test'``` 명령어로 테스트를 할 수 있습니다.




### ▶︎ 설치 및 실행 방법 

#### - Local 개발 및 테스트 용

1. 해당 프로젝트를 clone하고, 프로젝트 폴더로 이동한다.

```
git clone https://github.com/kooted-pre-onboarding/humanscape-assignment.git
cd humanscape-assignment
```

2. 가상 환경을 생성하고 프로젝트에 사용한 python package를 설치한다

```
conda create -n "humanscape" python=3.8
conda activate humanscape
```

3. docker 환경 설정 파일을 생성하고 다음을 작성한다.

```
touch .env
vi .env
HUMANSCAPE_SECRET_KEY=SECRET_KEY
```

4. 다음 명령어로 서버를 실행시킨다

```
docker-compose -f docker-compose.yml up 
```

4-1. 백그라운드로 실행하고싶을 시 `-d`옵션을 추가한다.

```
docker-compose -f docker-compose.yml up -d
```

#### - 배포용

1. 해당 프로젝트를 clone하고, 프로젝트 폴더로 이동한다.

```
git clone https://github.com/kooted-pre-onboarding/humanscape-assignment.git
cd humanscape-assignment
```

2. 가상 환경을 생성하고 프로젝트에 사용한 python package를 설치한다

```
conda create -n "humanscape" python=3.8
conda activate humanscape
```

3. docker 환경 설정 파일을 생성하고 다음을 작성한다.

```
touch .env
vi .env
HUMANSCAPE_SECRET_KEY=SECRET_KEY
```

4. 다음 명령어로 서버를 실행시킨다

```
sudo docker-compse -f docker-compose-deploy.yml up
```

4-1. 백그라운드로 실행하고싶을 시 `-d`옵션을 추가한다.

```
sudo docker-compse -f docker-compose-deploy.yml up -d
```






> ## API Document & Test 



1. [Postman API 문서 링크](https://documenter.getpostman.com/view/18218753/UVC9hkTh)로 접속해 우측 상단의 `Run in Postman` 버튼을 클릭합니다.
2. 개인 Workspace로 Import 합니다.
3. hostname 환경변수를 deploy로 선택합니다.
4. 배포 주소 `52.78.50.16:8000/tasks` 를 확인합니다. 
5. API 문서 예시를 참고해 Request를 보냅니다.





> ## 폴더 구조 



```
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── humanscape
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── settings_test.py
│   ├── test_runner.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pull_request_template.md
├── requirements.txt
├── tasks
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── cron.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── test_db.sqlite3
```





# Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 Humanscape에서 출제한 과제를 기반으로 만들었습니다.

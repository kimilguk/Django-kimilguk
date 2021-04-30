### 장고(파이썬) 프레임워크 기반 웹사이트 만들기
- CRUD(첨부파일기능포함) 및 관리자단 사용.
- 기초기술 : https://docs.djangoproject.com/ko/3.2/intro/tutorial01/

### 20210429 로컬 윈도우PC에서 작업하기-기존 깃허브에서 프로젝트 연동시
- 깃 허브에 있는 소스 클론
- SW 설치 : https://www.python.org/downloads/ (파이썬), VS code (IDE, 파이썬확장팩 설치)
- 터미널을 PS(파워쉘)에서 cmd(명령프롬프트)로 변경 정보: m.blog.naver.com/wideeyed/221837368919
- python -m pip install --upgrade pip (파이선 인스톨 패키지버전을 최신으로 변경)
- pip install virtualenv virtualenvwrapper-win (가상환경모듈 설치)
- mkvirtualenv human (윈도우에 가상환경 만들기)
- workon (가상개발환경 이름 확인)
- workon human (가상개발환경 선택)
- python -m pip install --upgrade pip (파이선 인스톨 패키지버전을 최신으로 변경)
- [강조]: 가상환경 안에서 장고를 설치하고 프로젝트를 추가하고, 앱을 생성합니다.
- python -m pip install django (필요시설치)
- python -m pip install Pillow (필요시설치)
- 아래 신규프로젝트 생성시 누락부분이 필요하면 추가 하고 다음 진행
- manage.py migrate (마이그레이션시 에러 처리- 아래2건)
- 자동증가필드 에러: Auto-created primary key used when not defining a primary key type
   id = models.AutoField(primary_key=True) 추가 후 OK
- 들여쓰기 에러: 스페이스와 탭키가 혼합되어 있으면 TabError: inconsistent use of tabs and spaces in indentation
  한가지로 통일 후 OK.
- 사용자확인시1: python namage.py shell 관련정보: kitle.xyz/post/58/
- 사용자확인시2: python manage.py createsuperuser (사용자가 없다면 추가)
- 사용자확인시3: python manage.py changepassword admin (관리자 암호변경)
- python manage.py runserver (서버실행)

### 신규프로젝트 생성시 누락부분 추가
- Django-kimilguk 폴더를 프로젝트 환경으로 만들어야 settings.py 파일이 만들어진다.(아래)
  (가상환경) ~/Django-kimilguk django-admin startproject mysite (mysite라는 폴더와 함께 장고 프로젝트 환경 구축됨.settings.py 파일생성)
- 앱생성 : 프로젝트에 kik_profile 이라는 앱을 생성 합니다. 
  (가상환경) ~/Django-kimilguk python manage.py startapp kik_profile

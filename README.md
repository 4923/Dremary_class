<h1> Django로 Dremary 클론코딩하기: Dremary_class </h1>


### **local admin account<br>**
  **ID** admin<br>
  **PW** djangoadmin<br>

1. [[1강] Django 그게 뭐야?](https://www.notion.so/1-Django-f31cf6ee230a42dc88ec158b8a659f64)<br>
    * Framework의 기능과 MTV 패턴에 대해 알아보기
    * 드리머리란?
2. [[2강] Hello, Django](https://www.notion.so/2-Hello-Django-eedae7bc69254b43b1cf3de03eca612b)<br>
    * 개발환경 구축하기 (가상환경, pip 이해)
    * Django 파일들 둘러보기
    * HomePage 출력하기
3. [[3강] Django가 관리하는 법](https://www.notion.so/3-Django-6826463424a648e1b0b9d4987699e074)<br>
    * Django에서 url을 관리하는방법: `urls.py`
    * Template언어 `{{ 템플릿 변수 }}` 와 `{% 템플릿 태그 %}`의 차이
    * Path의 구조
    * Static file의 이해 (Image, CSS)
      * Static과 Media의 차이
    * Static 파일 모으기
4. [[4강] Django로 나를 소개해볼게 #1](https://www.notion.so/4-Django-1-f33f455804374a9e854b49e2482090c3)<br>
    * Model의 이해
    * Migration: Model과 DB를 연동하기
    * Admin의 기능 파악
    * object 이름 수정하기 (설정한 제목으로 object 이름 설정하기)
5. [[5강] Django로 나를 소개해볼게 #2](https://www.notion.so/5-Django-2-9587384bc2ea41948a89c5ba07754816)<br>
    * admin 계정 잃어버렸을 때
    * 쿼리셋의 이해
      * 객체의 이해
    * Detail Page 구현
      * 없는 글을 불러오려고 할 때<br>
        404 page not found Error & `get_object_or_404`
      * urls.py에서 글마다 path를 만들지 않고 url 만들기<br>
        **path converter**
      * 각각의 글을 분류하기<br>
        **PK (Primary Key)**
6. [[6강] Django는 중복을 싫어해](https://www.notion.so/Django-ddb63281793d46078c3eba0e3cc8f549)<br>
    * URL Include
    * Template 상속: base.html
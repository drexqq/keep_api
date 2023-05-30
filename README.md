# keep_api

keep backend

    app
    ├── api              - api에 관련된 것들
    │   ├── errors       - 에러 핸들링
    │   ├── exceptions   - 예외 핸들링
    │   └── routes       - api 라우트, service를 사용
    ├── config           - 앱에 대한 설정
    ├── models           - pydantic models for this application
    │   ├── domain       - 메인으로 사용될 모델 클래스
    │   └── schemas      - 각 api 라우트에서 사용되는 스키마
    ├── service          - 각 라우트별 비즈니스로직, repository를 사용
    ├── repository       - 각 라우트별 데이터 접근
    ├── util             - 유틸리티
    └── main.py          - FastAPI 생성 및 설정

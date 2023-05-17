# keep_api

keep backend

## presentation

HTTP 요청을 처리하는 데 사용되는 폴더입니다.

- endpoints: 각 엔드포인트(Endpoint)에 대한 라우팅 로직을 정의하는 폴더입니다.
- models: API의 요청과 응답 모델링을 위한 Pydantic 모델 클래스가 포함되는 폴더입니다.
- schemas: 도메인 레이어와 데이터를 교환하기 위한 객체를 정의하는 폴더입니다.

## domain

애플리케이션의 비즈니스 로직을 구현하는 데 사용되는 폴더입니다.

- models: 도메인 객체를 정의하는 폴더입니다.
- services: 비즈니스 로직을 구현하는 폴더입니다.

## infrastructure

데이터베이스, 캐싱, 외부 서비스와의 통신 등의 인프라스트럭처를 처리하는 데 사용되는 폴더입니다.

- database: 데이터베이스 레이어를 구현하는 폴더입니다.

## config

애플리케이션의 설정을 처리하는 데 사용되는 폴더입니다.

- settings.py: 애플리케이션의 설정 파일입니다.

# utils

애플리케이션에서 사용되는 유틸리티들을 처리하는데 사용되는 폴더입니다.

## test

테스트 코드를 저장하는 데 사용되는 폴더입니다.

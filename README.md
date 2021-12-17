# reviewSystem

### 프로젝트 내용
![image](https://github.com/harryjung0330/reviewSystem/blob/main/%EC%82%AC%EC%A7%84%ED%8C%8C%EC%9D%BC/%EB%A6%AC%EB%B7%B0%EC%8B%9C%EC%8A%A4%ED%85%9C%EB%AC%B8%EC%A0%9C.PNG)
![image](https://github.com/harryjung0330/reviewSystem/blob/main/%EC%82%AC%EC%A7%84%ED%8C%8C%EC%9D%BC/%EB%A6%AC%EB%B7%B0%EC%8B%9C%EC%8A%A4%ED%85%9C%ED%95%B4%EA%B2%B0.PNG)

현재 많은 플랫폼들이 거짓리뷰, 조작된 리뷰, 이벤트성 리뷰 등으로 피해를 입고있습니다. 이 프로젝트에서는 유저들에게 신뢰도 점수를 매김으로써, 신뢰도가 높은 유저들이 쓴 리뷰는 다른 유저들에게 좀더 
노출이 되고, 평점에도 더 큰 비중을 차지하게 했습니다. 이렇게함으로써, 악성리뷰와 조작된 리뷰들은 덜 노출이 되고, 별점에도 적게 영향을 미치기 때문입니다. 

### 기술 스택

![image](https://github.com/harryjung0330/reviewSystem/blob/main/%EC%82%AC%EC%A7%84%ED%8C%8C%EC%9D%BC/%EB%A6%AC%EB%B7%B0%EC%8B%9C%EC%8A%A4%ED%85%9C%EA%B8%B0%EC%88%A0.PNG)
- AWS S3 -> 이미지 파일 저장
- AWS RDS -> 유저, 식당, 리뷰 정보 저장
- AWS Lambda -> 유저의 트래픽 처리
- AWS apigateway -> 람다랑 연동해 유저의 트래픽을 받는다
- python
- HTML, CSS, javascript

Aws Rds 데이터베이스 모델링
![image](https://github.com/harryjung0330/reviewSystem/blob/main/%EC%82%AC%EC%A7%84%ED%8C%8C%EC%9D%BC/ER.PNG)


### 역할
저는 이 프로젝트에서 아래의 역할들을 맡았습니다:
- 데이터베이스 모델링
- 람다 프로그래밍
- 시스템 아키텍쳐 구상

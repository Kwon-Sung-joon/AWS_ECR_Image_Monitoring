# AWS_ECR_Image_Monitoring
- ECR 리포지토리에 푸시된 이미지 CVE 스캔 결과 로그를 관리형 계정의 로그 그룹에서 관리

# Precondition
- 서비스 계정과 관리형 계정 간 IAM 연동 후 Lambda 환경 변수 설정
- 관리형 계정 내 로그 그룹 생성


# Architecture

![image](https://user-images.githubusercontent.com/43159901/212323161-50021308-88ea-4de1-b7cb-ded0d8340bf3.png)




# AWS_ECR_Image_Monitoring
AWS_ECR_Image_Monitoring

# Architecture

![image](https://user-images.githubusercontent.com/43159901/212323161-50021308-88ea-4de1-b7cb-ded0d8340bf3.png)



# Scenario
ECR 내 기본 스캔을 활성화하지 않고 배포 후 15분간 텀을 주어 해당 이미지를 스캔해야하는 구성으로 파이프라인을 통해 배포가 수행되며 ECR에 이미지가 Push되는 것을 이벤트로 잡아 SQS에 해당 메시지를 전송 하고 15분 후에 Lambda로 메시지를 전송할 수 있도록 구성하여 해당 Lambda에서는 수신 받은 메시지, 즉 ECR에 Push 된 이미지를 스캔하고 스캔 결과를 관리 AWS 계정 내 로그그룹에 전송되도록 구성하여 ECR 이미지 취약점 스캔과 결과 로그를 수집할 수 있도록 구성

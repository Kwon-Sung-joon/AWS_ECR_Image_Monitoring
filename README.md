# AWS_ECR_Image_Monitoring

AWS ECR 이미지 모니터링 시스템은 ECR 리포지토리에 푸시된 이미지의 CVE 스캔 결과를 관리형 계정의 로그 그룹에서 관리합니다. 이 시스템은 AWS Lambda와 Boto3 SDK를 사용하여 ECR 이미지의 보안 취약성을 자동으로 검사하고 결과를 로그 그룹에 기록합니다.

## Flow

1. Amazon EventBridge가 Lambda를 호출하고 이미지 스캔 이벤트를 전송합니다.
2. Lambda 함수는 SSM Parameter Store를 통해 스캔을 수행할 리포지토리 정보를 가져옵니다.
3. ECR 클라이언트를 사용하여 이미지 스캔을 시작합니다.
4. 스캔이 완료되면, 결과를 확인하고 로그로 기록합니다.
5. 결과는 AWS CloudWatch Logs에 기록됩니다.

## Precondition

- 서비스 계정과 관리형 계정 간 IAM 연동 후 Lambda 환경 변수를 설정해야 합니다.
- 관리형 계정 내에서 로그 그룹을 생성해야 합니다.
- AWS ECR에서 이미지를 푸시할 수 있는 권한이 있어야 합니다.

## Architecture

![image](https://user-images.githubusercontent.com/43159901/212323161-50021308-88ea-4de1-b7cb-ded0d8340bf3.png)

## Code Overview

### Ecr Class

- **`__init__`**: ECR 클라이언트를 초기화합니다.
- **`image_scan`**: 지정된 리포지토리 및 이미지 ID에 대해 이미지 스캔을 시작합니다.
- **`image_scan_waiter`**: 이미지 스캔이 완료될 때까지 대기합니다.
- **`get_image_scan_desc`**: 이미지 스캔 결과를 가져옵니다.
- **`get_image_current_tags`**: 현재 이미지 태그를 가져옵니다.

### Logs Class

- **`__init__`**: STS 클라이언트를 초기화하고 IAM 역할을 가져옵니다.
- **`put_logs`**: 이미지 스캔 결과를 CloudWatch Logs에 기록합니다.

### Lambda Handler

- **`lambda_handler`**: Lambda 함수의 진입점으로, 이벤트를 처리하고 ECR 이미지 스캔을 수행합니다.

## Environment Variables

- **`ASSUME_ROLE_ARN`**: IAM 역할 ARN을 환경 변수로 설정합니다. 이 역할은 ECR과 CloudWatch Logs에 대한 접근 권한을 포함해야 합니다.

## Usage

1. ECR에 이미지를 푸시합니다.
2. EventBridge가 Lambda를 호출하여 이미지 스캔을 시작합니다.
3. 스캔 결과는 지정된 CloudWatch Logs 그룹에 기록됩니다.

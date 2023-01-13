import json
import boto3
import os
import time

'''
create by ksj 2022-11-18
'''


class Ecr:
  def __init__(self):
    self.ecr_client=boto3.client('ecr');
  
  def image_scan(self,_repositoryName,_imageId):
    try:
      image_scan = self.ecr_client.start_image_scan(
        repositoryName=_repositoryName,
        imageId=_imageId
      )
    except:
      result=self.get_image_scan_desc(_repositoryName,_imageId);
    else:
      #image scan waiting...
      self.image_scane_waiter(_repositoryName,_imageId);
      result=self.get_image_scan_desc(_repositoryName,_imageId);
    return result
    #scan_result=self.image_scan_waiter(self.repositoryName,self.imageDigest,self.imageTag)
  def image_scan_waiter(self,_repositoryName,_imageId):
    waiter = self.ecr_client.get_waiter('image_scan_complete')
    waiter.wait(
      repositoryName=_repositoryName,
      imageId=_imageId
    )
  def get_image_scan_desc(self,_repositoryName,_imageId):
    response = self.ecr_client.describe_image_scan_findings(
      repositoryName=_repositoryName,
      imageId=_imageId
    )
    
    scan_result_arr=[]
    '''
    for i in response.get('imageScanFindings').get('findings'):
      scan_result_dict = {
        'name':i.get('name')
        'severity':i.get('severity')
      }
      scan_result_arr.append(scan_result_dict)
      
      
      
      result = {
        'repositoryName':_repositoryName,
        'imageId':_imageId,
        'imageScanStatus':response.get('imageScanStatus'),
        'vulerabilities':scan_result_arr
      }
      '''
    result = {
      'repositoryName':_repositoryName,
      'imageId':_imageId,
      'imageScanStatus':response.get('imageScanStatus'),
      'vulnerabilities':response.get('imageScanFindings').get('findings')
    }
    
    return result
  
class Logs:
  def __init__(self):
    self.sts_client=boto3.client('sts');
    assumed_role=self.sts_client.assume_role(
      RoleArn=os.getenv('ASSUME_ROLE_ARN'),
      RoleSessionName="Assume_Role_Session"
    )
    credentials=assumed_role['Credentials']
    self.logs_client=boto3.client('logs',
                aws_access_key_id=credentials['AccessKeyId]',
                aws_secret_access_key=['SecretAccessKey'],
                aws_session_token=credentials['SessionToken']                             
                                              )
  
  def put_logs(self,msg):
                                              
    
  
  
  
  
  
  
  
  
  
      
      
      
      
      
      
      
      
    
    
    
    
    
    
    

# -*- coding: utf-8 -*-
import logging
import json
import sys
import getopt
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkcore.request import CommonRequest
from aliyunsdkvpc.request.v20160428.DescribeVpcsRequest import DescribeVpcsRequest
from aliyunsdkecs.request.v20140526.DescribeSecurityGroupsRequest import DescribeSecurityGroupsRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest



# if you open the initializer feature, please implement the initializer function, as below:
# def initializer(context):
#   logger = logging.getLogger()
#   logger.info('initializing')

def handler(event, context):
    logger = logging.getLogger()
    logger.info('hello world')

    creds = context.credentials
    sts_token_credential = StsTokenCredential(creds.accessKeyId, creds.accessKeySecret, creds.securityToken)

    #logger.info('creds.accessKeyId '+creds.accessKeyId)
    #logger.info('creds.accessKeySecret '+creds.accessKeySecret)
    #logger.info('creds.securityToken '+creds.securityToken)

    client = AcsClient(credential=sts_token_credential)
    #Regions in which vms should be decribed and checked if they belong to default SG


    regions = ['cn-beijing', 'cn-shanghai', 'ap-southeast-1']
    #regions = ['cn-shanghai']
    toMerge = []
    for eachReg in regions:
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('ecs.aliyuncs.com')
        request.set_method('GET')
        request.set_protocol_type('https')
        request.set_version('2014-05-26')
        request.set_action_name('DescribeInstances')
        request.add_query_param('RegionId', eachReg)
        try:
            response = client.do_action(request)
        except ServerException as e:
            print(e.get_http_status(), e.get_error_code(), e.get_error_msg())
            raise e
        vms = str(response, encoding = 'utf-8')

        vmsJson = json.loads(vms)
        instances = vmsJson['Instances']['Instance']

        #instancesJson = json.loads(instances)


        for instance in instances:




            zoneid = instance['ZoneId']
            instanceId = instance['InstanceId']
            instanceName = instance['InstanceName']

            #logger.info('zoneid '+str(zoneid))
            logger.info('instanceName '+str(instanceName) +str(' from ') +str(eachReg))
            #logger.info('tempInstances '+str(tempInstances))

            #toMerge.extend(tempInstances)
            #instances=json.dumps(toMerge)


    return 'hello world'
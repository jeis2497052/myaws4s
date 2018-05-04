#!/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Run this quick test to validate ec2 access using Boto3 and keys from Kevin
'''
import boto3
EC2 = boto3.client('ec2')
RESPONSE = EC2.describe_instances()
print RESPONSE
# SUCCESS is sample instance output
SUCCESS = "{u'Reservations': [], 'ResponseMetadata': " \
    "{'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': " \
    "'365e7b83-d40c-4620-ac4b-4a072e9950bc', 'HTTPHeaders': " \
    "{'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding', " \
    "'server': 'AmazonEC2', 'content-type': 'text/xml;charset=UTF-8', " \
    " 'date': 'Fri, 04 May 2018 13:24:29 GMT'}}}"

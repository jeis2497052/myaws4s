#!/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
simple boto instance example
'''
# import argparse
from collections import defaultdict
import boto3

EC2 = boto3.resource('ec2')

SESSION = boto3.Session()
REGIONS = SESSION.get_available_regions('ec2')
# print REGIONS

EC2CLIENT = SESSION.client('ec2', 'us-west-1')
EC2_INSTANCES = EC2CLIENT.describe_instances()
EC2TAGS = EC2CLIENT.describe_tags()
# print EC2_INSTANCES

EC2R = SESSION.resource('ec2')
print EC2R.Instance
print EC2R.Tag
print EC2R.instances
print EC2R.internet_gateways
for i in EC2R.instances.all():
    print i


EC2W3 = boto3.resource('ec2')

# Get information for all running instances
RUNNING_INSTANCES = EC2W3.instances.filter(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running']}])

EC2INFO = defaultdict()
for instance in RUNNING_INSTANCES:
    for tag in instance.tags:
        if 'Name'in tag['Key']:
            name = tag['Value']
    # Add instance info to a dictionary
    EC2INFO[instance.id] = {
        'Name': name,
        'Type': instance.instance_type,
        'State': instance.state['Name'],
        'Launch Time': instance.launch_time
    }

ATTRIBUTES = ['Name', 'Type', 'State',
              'Private IP', 'Public IP', 'Launch Time']
for instance_id, instance in EC2INFO.items():
    for key in ATTRIBUTES:
        print "{0}: {1}".format(key, instance[key])
    print "------"

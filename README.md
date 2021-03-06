# myaws4s - problem to solve is create AWS API tool to list EC2 instances

# include id, tag value, instance type, launch time
## tag value called Owner
## type could be unknown - origin task snippet shown below:

```

Using your favorite high-level language (Python, Ruby, Perl, or
compiled if desired), create a tool which uses the AWS API to list all
EC2 instances in any single region, sorted by the value of a tag each
instance has called ‘Owner’.


The script should display the results in an easy to read format which
includes the instance id, tag value, instance type and launch
time. The script should work for any number of instances and should
display any instances without an Owner tag as type 'unknown' with the
instance id, type and launch time. Design the script so it could be
used later to index on different tags and output additional instance
metadata.

AWS Access Key: AKIAII52CLCS24MEZM4A
AWS Secret: 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

You can submit with a git repository, zip file, or whatever you’re comfortable with.

```



# Install awscli
# configure awscli
# Install Boto3 as SDK approach
# validate keys - issue to start - Kevin sent fresh keys


```python
Python 2.7.15rc1 (default, Apr 15 2018, 21:51:34)
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> ec2=boto3.client('ec2')
>>> response=ec2.describe_instances()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/botocore/client.py", line 314, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/usr/local/lib/python2.7/dist-packages/botocore/client.py", line 612, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (AuthFailure) when calling the DescribeInstances operation: AWS was not able to validate the provided access credentials
>>> quit()
```

# Kevin sends updated keys

```sh
$ cat ~/.aws/config
[default]
region = us-east-1
$ cat ~/.aws/credentials
[default]
aws_access_key_id = AXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
aws_secret_access_key = 9XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxx
$
```

# Validate updated keys

```python
Python 2.7.15rc1 (default, Apr 15 2018, 21:51:34)
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> ec2=boto3.client('ec2')
>>> response=ec2.describe_instances()
>>> print response
{u'Reservations': [], 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '7df079d7-5754-4e9b-b51d-a2d45c0b0243', 'HTTPHeaders': {'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding', 'server': 'AmazonEC2', 'content-type': 'text/xml;charset=UTF-8', 'date': 'Fri, 04 May 2018 13:12:32 GMT'}}}
>>> quit()
```

# sample shell script using variables to change the environment

```sh
./runec2
Traceback (most recent call last):
  File "./ec2_validate.py", line 8, in <module>
    RESPONSE = EC2.describe_instances()
  File "/home/jeis247/Public/jeis2497052/boto3/src/botocore/botocore/client.py", line 314, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/home/jeis247/Public/jeis2497052/boto3/src/botocore/botocore/client.py", line 612, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (AuthFailure) when calling the DescribeInstances operation: AWS was not able to validate the provided access credentials


Error: something went wrong

{u'Reservations': [], 'ResponseMetadata': {'RetryAttempts': 0, 'HTTPStatusCode': 200, 'RequestId': '604c35c3-debf-470a-bfd8-383657abc2b9', 'HTTPHeaders': {'transfer-encoding': 'chunked', 'vary': 'Accept-Encoding', 'server': 'AmazonEC2', 'content-type': 'text/xml;charset=UTF-8', 'date': 'Fri, 04 May 2018 14:17:28 GMT'}}}


#!/usr/bin/env bash
export AWS_ACCESS_KEY_ID='AKIAII52CLCS24MEZM4A'
export AWS_SECRET_ACCESS_KEY='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'
./ec2_validate.py
[ $? -ne 0 ] && echo -e "\n\nError: something went wrong\n"

export AWS_ACCESS_KEY_ID='AXXXXXXXXXXXXXXXXXXXXXXXXX'
export AWS_SECRET_ACCESS_KEY='9XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx'

./ec2_validate.py
[ $? -ne 0 ] && echo -e "Error: something went wrong\n"

BTW, git guardian is awesome as I was sent email regarding the keys in bash
so I removed script from repo

```

# Start solving this assignment.
## Access provided is very restricted, for example via cli:

```sh
aws ec2 describe-instances
{
    "Reservations": []
}
```

## One more set of cli with very restricted access
```sh
$ aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, Hypervisor, NetworkInterfaces[0].Attachment.DeleteOnTermination]'

[]
$ aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId]'

[]
$ aws ec2 describe-instances --query 'Reservations[*].Instances[*]'
[]
$ 
```

### And in an ipython shell no instances will print

```python
ipython3
Python 3.6.5 (default, Apr  1 2018, 05:46:30)
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import boto3
In [1]: import boto3

In [2]: s = boto3.Session()
In [2]: s = boto3.Session()

In [3]: ec2 = s.resource('ec2')
In [3]: ec2 = s.resource('ec2')

In [4]: for i in ec2.instances.all(): print(i)
In [4]: for i in ec2.instances.all(): print(i)

In [5]:
```



# Reference links

[ipython gist](https://gist.github.com/iMilnb/0ff71b44026cfd7894f8)

[boto3](http://boto3.readthedocs.io/en/latest/guide/quickstart.html)

[another descrbe_instance page](https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_instances)

[python gist](https://gist.githubusercontent.com/iMilnb/df47cd6aea9eeac153ff/raw/bf0a5d743b044897d3fed54be2891e53737c5fd1/ec2.py)

[stackoverflow ec2 boto3](https://stackoverflow.com/questions/38112770/iterate-thru-ec2-describe-instance-boto3)

[aws cli](https://aws.amazon.com/cli/)


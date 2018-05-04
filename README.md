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


```
python
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
aws_access_key_id = AKIAI4FLFVEXDEYPZUEA
aws_secret_access_key = 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
$
```

# Validate updated keys

```sh
python 
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

# Start solving this assignment.

import boto3
s3 = boto3.resource('s3')

location={'LocationConstraint':'us-east-1'}

res=s3.create_bucket(Bucket='bkt0402eastashis',CreateBucketConfiguration=location)
print(res)

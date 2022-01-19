import boto3
s3 = boto3.resource('s3')

print("Below are the S3 Buckets :")
for bkt in s3.buckets.all():
    print(bkt.name)

myBkt=input("Enter Your S3 Bucket Name :")

my_bucket = s3.Bucket(myBkt)

for file in my_bucket.objects.all():
    print(file.key)
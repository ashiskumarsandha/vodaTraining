
def generateBucketNameList(preFixBktName):
    import string
    data=string.ascii_lowercase+string.digits
    import random
    randSize=4
    randString=''.join(random.choice(data) for _ in range(randSize))
    bktName=preFixBktName+randString
    return bktName

def createBucketName(bktName):
    import boto3
    s3 = boto3.resource('s3')

    location={'LocationConstraint':'us-west-1'}

    res=s3.create_bucket(Bucket=bktName,CreateBucketConfiguration=location)
    print(res)

# randBktName=generateBucketNameList()
for i in range(4):
    createBucketName(generateBucketNameList('bktrandashis'))

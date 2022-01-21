provider "aws" {
    access_key = "AKIAZMNCSZ3T4CNWXOFT"
    secret_key = "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"
    region = "us-east-1"
}



resource "aws_s3_bucket" "createbucketblock" {
    bucket = "bkttfv1ashis"
    tags ={
        Name="bkttfv1ashis"
        Enviornment="Dev"
    }
}
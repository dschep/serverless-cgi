# Serverless CGI

Because [serverless is just cgi-bin](https://twitter.com/benschwarz/status/743180671720398848).
And I just had surgery so painkiller made this seem like a hilarious idea.

This is a [serverless framework](https://serverless.com) and AWS Lambda based
simple CGI service. Just drop your scripts into the `cgi-bin` directory.

## Example use
Here's how to install and deploy your CGI script (`hello-world.pl` in this
case).
```
$ npm i -g serverless
$ sls install https://github.com/dschep/serverless-cgi
$ sls deploy
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (4.85 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: sls-cgi
stage: dev
region: us-east-1
api keys:
  None
endpoints:
  ANY - https://u5j8jngzyc.execute-api.us-east-1.amazonaws.com/dev/cgi-bin/{path+}
functions:
  cgi-bin: sls-cgi-dev-cgi-bin
Serverless: Removing old service versions...
$ http -v https://u5j8jngzyc.execute-api.us-east-1.amazonaws.com/dev/cgi-bin/hello-world.pl
GET /dev/cgi-bin/hello-world.pl HTTP/1.1
Connection: keep-alive
Host: u5j8jngzyc.execute-api.us-east-1.amazonaws.com
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: HTTPie/0.9.8



HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 11
Connection: keep-alive
Date: Wed, 02 Aug 2017 17:24:25 GMT
x-amzn-RequestId: 6e93728b-77a7-11e7-a743-f58b9a3ef9b0
X-Amzn-Trace-Id: sampled=0;root=1-59820ac9-e30697d6cf113580ba23f338
X-Cache: Miss from cloudfront
Via: 1.1 f19281f08e79aa6c6634266c50732dd5.cloudfront.net (CloudFront)
X-Amz-Cf-Id: RFLj0hA_Jm8pSVW60EvrOxqlkXiS-eNSrNF8Kiz9e9W0zjF54FCadQ==

Hello World
```

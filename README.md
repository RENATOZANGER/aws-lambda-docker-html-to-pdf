# aws-lambda-docker-html-to-pdf

Python script to read an HTML template, load some values and then save the changed template as a PDF in a bucket.

`Note: It will be necessary to include permission to write to the bucket in the role used by the lambda.`

### Dockerfile

The Dockerfile includes:

- Python 3.11, based on the official AWS Lambda image.
- Installation of `wkhtmltopdf`, allowing conversion from HTML to PDF within Lambda functions.
- Installation of additional packages necessary for `wkhtmltopdf` to work correctly in the AWS Lambda environment.

### lambda_function.py

- Receives data through Lambda events (name and age).
- Renders an HTML template with the received data using Jinja2.
- Generates a PDF file from the rendered HTML.
- Saves the PDF to the specified S3 bucket.

### Usage

To use this Lambda function, follow these steps:

1. Create a new private repository in Amazon ECR:
- Ex: account_id.dkr.ecr.us-east-1.amazonaws.com/htmltopdf

2. Retrieve an authentication token and authenticate your Docker client to your registry
- aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin account_id.dkr.ecr.us-east-1.amazonaws.com

3. Build your Docker image
- docker build -t htmltopdf .

4. Tag your image so you can push
- docker tag htmltopdf:latest account_id.dkr.ecr.us-east-1.amazonaws.com/htmltopdf:latest

5. Push this image to your newly created AWS repository
- docker push account_id.dkr.ecr.us-east-1.amazonaws.com/htmltopdf:latest

6. Create a Lambda function in AWS Lambda.

7. Configure the Lambda function to use the container image from the container registry.

8. set the lambda timeout to more than 30 seconds

10. click on test

### Local Testing:

1. Build the image
docker build -t htmltopdf .

2. Run the image
docker run -e LOCAL_EXECUTION=true -p 9000:8080 htmltopdf:latest

3. Test the running image
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"nome":"jose","idade":12}'
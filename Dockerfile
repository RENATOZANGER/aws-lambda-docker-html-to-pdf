FROM public.ecr.aws/lambda/python:3.11

# Install necessary packages for wkhtmltopdf
RUN yum install -y wget xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 && \
    yum clean all

# Download wkhtmltopdf and install
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.centos7.x86_64.rpm && \
    yum install -y ./wkhtmltox-0.12.6-1.centos7.x86_64.rpm && \
    rm ./wkhtmltox-0.12.6-1.centos7.x86_64.rpm

COPY . .

RUN pip install -r requirements.txt
CMD ["lambda_function.handler"]

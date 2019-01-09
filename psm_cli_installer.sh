#!/bin/bash
curl -LO https://bootstrap.pypa.io/get-pip.py
yum install -y git
python get-pip.py
python -m pip uninstall awscli -y
python -m pip install awscli
python -m pip install boto3
python -m pip install docopt
aws s3 cp s3://k8s.cicd..ps.vpc-utils/scripts/psm
curl -LO https://raw.githubusercontent.com/HumbleFool006/py-workshop/master/psm
chmod +x psm
mv psm /usr/local/bin/psm

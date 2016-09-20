# These values can be overridden in config_local.py
REPORT_PATH = 'report.html'
REPORT_URL = ''
TIME_ZONE = 'US/Central'


from config_local import *


ebay_keys = ('appid', 'devid', 'certid', 'token')
EBAY_CREDENTIALS = {}
for k, v in EBAY_PARAMS:
    EBAY_CREDENTIALS[k] = dict(zip(ebay_keys, v.split(';')))


aws = AWS_PARAMS.split(';')
AWS_CREDENTIALS = dict(
    aws_access_key_id=aws[0],
    aws_secret_access_key=aws[1],
)

import os

os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DEVELOPMENT'] = 'True'
# Set because I am using the CI db locally (Bad?? maybe idc)
os.environ['DATABASE_URL'] = 'redacted-from-github'

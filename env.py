import os

os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DEVELOPMENT'] = 'True'
# Set because I am using the CI db locally (Bad?? maybe idc)
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:3tgNshSPlwz6@ep-steep-sunset-a28pigfk.eu-central-1.aws.neon.tech/daisy_pound_woven_483693'
import os
class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'abylkassovm')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'Advirtys93')
    HOST = os.environ.get('POSTGRES_HOST')
    PORT = os.environ.get('POSTGRES_PORT')
    DB = os.environ.get('POSTGRES_DB')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"  
    SECRET_KEY = 'KWBDoypJ}1WV6AkKbe]LLqz+YgGnq?UND?qE8eYtggNq>y4^Xdo_qcJC2CGxoBUMny1?oRcgHT1Md)vV>FqWo7QnC=8BjxT7g'
    SQLALCHEMY_TRACK_MODIFICATIONS = True 

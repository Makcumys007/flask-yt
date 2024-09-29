from flask import Flask
from .extentions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"    
    app.config['SECRET_KEY'] = 'KWBDoypJ}1WV6AkKbe]LLqz+YgGnq?UND?qE8eYtggNq>y4^Xdo_qcJC2CGxoBUMny1?oRcgHT1Md)vV>FqWo7QnC=8BjxT7g'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
   # app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///project.db'
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
    return app

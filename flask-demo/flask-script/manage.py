from flask.ext.script import Manager
from flask import Flask




''' 
 python manage.py runserver -h

'''

app = Flask(__name__)

manager = Manager(app)

if __name__=="__main__":
	manager.run()

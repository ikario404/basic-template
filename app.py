import json
import os
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

def create_app():
	app = Flask(__name__)
	Bootstrap(app)
	with open('conf/conf.json') as f:
		conf = json.load(f)
		app.config['PORT'] = conf['PORT']
		app.config['DEBUG_LEVEL'] = conf['DEBUG_LEVEL']
	return app

try:
	app = create_app()    
except BaseException as error:
	print('An exception occurred : {}'.format(error))

@app.route("/")
def hello():
	return render_template('home.html')




##########################################################################
# Start
##########################################################################
if __name__ == '__main__':
	app.secret_key = os.urandom(24)
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD']=True
	app.run(debug=app.config['DEBUG_LEVEL'], host='0.0.0.0', port=app.config['PORT'], threaded=True)


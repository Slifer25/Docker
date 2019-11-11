from flask import Flask
from flask import jsonify
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

@app.route('/maior/<int:x>/<int:y>')
def maior(x,y):
    if(x>y):
	return jsonify (x,"eh maior")
    elif(y>x):
	return jsonify  (y,"eh maior")
    else:
	return jsonify  ("sao iguais")



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

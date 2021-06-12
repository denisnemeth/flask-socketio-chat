from flask import Flask 
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, ping_timeout=3, ping_interval=1)

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

#import logging

if __name__ == '__main__':
	socketio.run(app)

from app import app, db, socketio
from app.models import Message
from flask import request, json, render_template, session

from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect

import datetime

#@app.route('/messages.send', methods=['POST'])
#def send_message():
#    data = request.form
#    msg = Message(time=datetime.datetime.now(), name=data['name'], color=data['color'], text=data['text'])
#    db.session.add(msg)
#    db.session.commit()
#    message = {'time': datetime.datetime.now(), 'name': data['name'], 'color': data['color'], 'text': data['text']}
#    print("WebSock")
#    socketio.emit('new_message',
#         {'data': json.dumps(message)},
#         broadcast=True, namespace='/momoru.messages')
#    return 'ok'

#@app.route('/messages.get', methods=['GET', 'POST'])
#def get_messages():
#    messages = Message.query.all()
#    json_messages = []
#    for message in messages:
#        m = {'time': message.time, 'name': message.name, 'color': message.color, 'text': message.text}
#        json_messages.append(m)
#    return json.dumps(json_messages)

@app.route('/messages-frame')
def send_messages_iframe():
    return render_template('messages.html')

@socketio.on('new_message', namespace='/momoru.messages')
def test_broadcast_message(message):
    print("Broadcast handeled")
    name = ""
    if message['data']['name'].replace(" ", "") == "":
        name = "Anon"
    else: 
        name = message['data']['name']
    emit('my_response',
         {'event': 'message', 'data': message['data']['text'], 'name': name, 'online': session['online']}, broadcast=True)

@socketio.on('disconnect_request', namespace='/momoru.messages')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    emit('my_response',
         {'data': 'Disconnected!'},
         callback=can_disconnect)


@socketio.on('connect', namespace='/momoru.messages')
def test_connect():
    session['online'] = session.get('online', 0) + 1
    emit('my_response', {'event': 'connect', 'online': session['online']})


@socketio.on('disconnect', namespace='/momoru.messages')
def test_disconnect():
    session['online'] = session.get('online', 0) - 1
    emit('my_response', {'event': 'disconnect', 'online': session['online']})
    print('Client disconnected', request.sid)
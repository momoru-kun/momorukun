from app import app, db, socketio
from app.models import Message
from flask import request, session, json

from threading import Lock

from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect

import datetime

thread = None
thread_lock = Lock()

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

@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    print("Broadcast handeled")
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)

@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    # for this emit we use a callback function
    # when the callback function is invoked we know that the message has been
    # received and it is safe to disconnect
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)
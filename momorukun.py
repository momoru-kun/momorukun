
# A very simple Flask Hello World app for you to get started with...

from app import app, db, socketio

if __name__ == "__main__":
    app.run(host="0.0.0.0")


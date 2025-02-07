from flask import Flask
from flask_socketio import SocketIO
from routes.route import api_routes

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

socketio = SocketIO(app, cors_allowed_origins="*")  

# Register API routes
app.register_blueprint(api_routes)

if __name__ == "__main__":
    socketio.run(app, debug=True)

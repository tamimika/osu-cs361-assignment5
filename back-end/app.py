from flask import Flask
from flask_cors import CORS
from models import db
import routes as routes

app = Flask(__name__)
CORS(app, origins=['http://localhost:8080'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
db.init_app(app)
routes.add_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5555)


from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

class Salary(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    salary = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.String(36), nullable=False)  # Assuming a user id is available. If not, this line can be omitted.

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = str(uuid4())

    def __repr__(self):
        return f'<Salary {self.salary}>'

    def to_dict(self):
        return {
            "id": self.id,
            "salary": self.salary,
            "user_id": self.user_id,  # If user id is not available, this line can be omitted.
        }

class Transaction(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    date = db.Column(db.DateTime, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    item = db.Column(db.String(50), nullable=False)
    vendor = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = str(uuid4())

    def __repr__(self):
        return f'<Transaction {self.item}>'

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.strftime('%Y-%m-%d'),
            "cost": self.cost,
            "item": self.item,
            "vendor": self.vendor,
            "category": self.category,
        }

from flask import request, jsonify
from datetime import datetime
from models import db, Transaction, Salary
from datetime import datetime

def add_routes(app):

  @app.route('/salary', methods=['PUT'])
  def add_salary():
      data = request.get_json()
      salary = Salary(salary=data.get('salary'), user_id=data.get('user_id'))  # If user id is not available, remove `user_id=data.get('user_id')`.
      db.session.add(salary)
      db.session.commit()
      return jsonify({'message': 'Salary added'}), 201

  @app.route('/salary/<string:user_id>', methods=['GET'])  # If user id is not available, adjust this route to your needs.
  def get_salary(user_id):
      salary = Salary.query.filter_by(user_id=user_id).first()  # Fetch the salary record of the user. If user id is not available, adjust this line.
      if salary is None:
          return jsonify({"message": "Salary not found"}), 404
      return jsonify(salary.to_dict()), 200

  @app.route('/add', methods=['POST'])
  def add_transaction():
      data = request.get_json()
      date_str = data.get('date')
      date = datetime.strptime(date_str, '%Y-%m-%d')
      transaction = Transaction(
          date=date,
          cost=float(data.get('cost')),
          item=data.get('item'),
          vendor=data.get('vendor'),
          category=data.get('category')
      )
      db.session.add(transaction)
      db.session.commit()
      return jsonify({'message': 'Transaction added'}), 201

  @app.route('/upload', methods=['POST'])
  def upload_file():
      if 'file' not in request.files:
          return {"message": "No file part"}, 400
      file = request.files['file']
      if file.filename == '':
          return {"message": "No file selected"}, 400
      if file and file.filename.endswith('.json'):
          data = json.load(file)

          for item in data:
              date = datetime.strptime(item['date'], '%Y-%m-%d')
              transaction = Transaction(
                  date=date,
                  cost=float(item['cost']),
                  item=item['item'],
                  vendor=item['vendor'],
                  category=item['category']
              )
              db.session.add(transaction)
          db.session.commit()

          return jsonify({'message': 'File uploaded and transactions saved'}), 200
      else:
          return jsonify({'message': 'Allowed file types are .json'}), 400

  @app.route("/transactions/<string:transaction_id>", methods=["GET"])
  def get_transaction(transaction_id):
      transaction = db.session.query(Transaction).get(transaction_id)
      if transaction is None:
          return jsonify({"message": "Transaction not found"}), 404
      return jsonify(transaction.to_dict())

  @app.route('/transactions', methods=['GET'])
  def get_transactions():
      transactions = Transaction.query.all()
      return jsonify({'data': [transaction.to_dict() for transaction in transactions]}), 200

  @app.route('/transactions/<transaction_id>', methods=['PUT'])
  def update_transaction(transaction_id):
      # Get transaction from database
      transaction = db.session.query(Transaction).get(transaction_id)

      # Get request data
      data = request.get_json()

      # Convert date from string to datetime
      date = datetime.strptime(data['date'], '%Y-%m-%d')  # adjust date format if necessary

      # Update transaction
      transaction.date = date
      transaction.cost = float(data['cost'])
      transaction.item = data['item']
      transaction.vendor = data['vendor']
      transaction.category = data['category']

      # Save changes
      db.session.commit()

      return jsonify(transaction.to_dict()), 200

  @app.route("/transactions/<string:transaction_id>", methods=["DELETE"])
  def delete_transaction(transaction_id):
      transaction = Transaction.query.get(transaction_id)
      if transaction is None:
          return jsonify({"message": "Transaction not found"}), 404

      db.session.delete(transaction)
      db.session.commit()
      return jsonify({"message": "Transaction deleted"})

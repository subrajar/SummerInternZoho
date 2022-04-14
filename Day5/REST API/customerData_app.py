from flask import Flask, request

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(20))

    def __repr__(self):
        return f"{self.customer_name} - {self.id}"


db.create_all()


@app.route('/')
def hii():
    return "hello"


@app.route('/customers')
def get_customers():
    customers = Customers.query.all()
    output = []
    for customer in customers:
        customer_data = {"id": customer.id, "customer_name": customer.customer_name}
        output.append(customer_data)
    return {"customers": output}


@app.route('/customers/<customer_id>')
def get_customer(customer_id):
    customer = Customers.query.get_or_404(customer_id)
    return {"id": customer.id, "customer_name": customer.customer_name}


@app.route('/customers', methods=['POST'])
def add_customer():
    customer = Customers(id=request.json['id'], customer_name=request.json['customer_name'])
    db.session.add(customer)
    db.session.commit()
    return "sucessfully added"

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from smail import send_mail

app=Flask(__name__)


ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/Reviews'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/Reviews'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    product = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    mail=db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, customer, product,mail, rating, comments):
        self.customer = customer
        self.product = product
        self.mail=mail
        self.rating = rating
        self.comments = comments

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def sumit():
    if request.method=='POST':
        customer=request.form['customer']
        Product=request.form['Product']
        mail=request.form['E-mail']
        rating=request.form['rating']
        comments=request.form['comments']
        if customer == '' or Product == '' or mail=='' :
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback):
            data=Feedback(customer,Product,mail,rating,comments)
            db.session.add(data)
            db.session.commit()
            send_mail(mail)
            return render_template('final.html')

if __name__=='__main__':
    app.debug=True
    app.run()
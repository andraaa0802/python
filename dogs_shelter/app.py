from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/shelter'
db=SQLAlchemy(app)

class Dog(db.Model):
    __tablename__='dogs'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    availability = db.Column(db.Boolean, default=True)
    photo_path = db.Column(db.String(255), nullable=False, default='images/tyson.jpg')

@app.route('/')
def index():
    dogs=Dog.query.all()
    return render_template('index.html', dogs=dogs)

@app.route('/dog/<int:dog_id>')
def dog_detail(dog_id):
    dog=Dog.query.get(dog_id)
    return render_template('dog_detail.html', dog=dog)

@app.route('/adopt/<int:dog_id>', methods=['GET', 'POST'])
def adopt(dog_id):
    dog=Dog.query.get(dog_id)
    if request.method=='POST':
        dog.availability=False
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('adopt.html', dog=dog)


if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
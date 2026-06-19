from flask import Flask, render_template, request , url_for,redirect, flash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import Integer, String, Boolean
from sqlalchemy.exc import IntegrityError

import os
from datetime import datetime,timezone



app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)






class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)


class Note(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(1000), nullable=False)
    note: Mapped[str] = mapped_column(String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    
    
 

    
    
    
     
    

with app.app_context():
    db.create_all()

@app.route('/')
def main():
    return render_template('userinterface.html')




@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        print(username, email, password)  # DEBUG

        user = User(
            username=username,
            email=email,
            password=password
        )
        try:
            db.session.add(user)
            db.session.commit()
            
        except IntegrityError:
            flash("Sorry, this email has already registered!")
        else:
            flash("Registration successful!")
            

    return render_template("register.html")

@app.route("/delete/<int:id>")
def delete_note(id):
    note = Note.query.get_or_404(id)

    db.session.delete(note)
    db.session.commit()

    return redirect("/home")

@app.route('/home',methods=["GET","POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        note_text = request.form["note"]

        new_note = Note(title=title, note=note_text)
        db.session.add(new_note)
        db.session.commit()

        return redirect("/home")

    notes = Note.query.all()

    return render_template("home.html", note=notes)
    
    
@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")
  
  
        user = db.session.query(User).filter_by(email=email).first()
        

        if user:
            if password==user.password:
                return redirect(url_for("home"))
            else:
                flash("Sorry, password is wrong")
        else:
            flash("Sorry, this email is not valid😥!")
    
    
    return render_template("checkforlogin.html")


if __name__ == '__main__':
    app.run(debug=True)
     
from flask import Flask, render_template
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(message="That is not a valid email address")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters")])
    login = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    name = None
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email)
        print(login_form.password)
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', name=name, form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
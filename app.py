from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '6Lfkwe8pAAAAACTvtSA3tEistOxeU4GG2RhXiuC7'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfkwe8pAAAAAHJtVwA-5G49-cMzr4dCAbkO-m_0'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lfkwe8pAAAAACTvtSA3tEistOxeU4GG2RhXiuC7'
bootstrap = Bootstrap(app)

# Mock user database
users = {'sample24@examplemail.com': 's@mplepass^27'}

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email in users and users[email] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'error')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    # Sample table data
    table_data = [
        {'Name': 'John Doe', 'Age': 30, 'Location': 'New York'},
        {'Name': 'Jane Smith', 'Age': 25, 'Location': 'Los Angeles'},
        {'Name': 'Bob Johnson', 'Age': 35, 'Location': 'Chicago'}
    ]
    return render_template('dashboard.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)

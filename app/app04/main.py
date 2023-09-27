from flask import Flask, render_template, request, make_response, redirect, url_for, flash
from app04.models import db, Users
from logging import getLogger as Logger
from flask_wtf.csrf import CSRFProtect
from app04.registration_form import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_database.db'
app.config['SECRET_KEY'] = '...'
csrf = CSRFProtect(app)
db.init_app(app)



@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')
    
    
@app.cli.command('fill-db')
def fill_db():
    ...
        
        
@app.get('/')
def home():
    context = {'users': Users.query.all()}
    return render_template('home.html', **context)

@app.route('/register/', methods=['GEt','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        hash_pswd = generate_password_hash(form.user_password.data)
        new_user = Users(
            user_name=form.user_name.data,
            user_email=form.e_mail.data,
            user_password=hash_pswd,
        
        )
        db.session.add(new_user)
        db.session.commit()
        response = make_response(redirect(url_for('home')))
        flash('Успешная регистрация', 'success')
        # return response
    return render_template('register.html', form=form)
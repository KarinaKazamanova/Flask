from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/hello/<name>', methods=['GET','POST'])
def hello(name):
    if request.method == 'POST':
        response = make_response("Удаление пользоватея")
        response.delete_cookie('username')
        response.delete_cookie('email')
        return redirect('/registration_form/')
    return render_template('hello.html', name=name)
    

@app.route("/registration_form/", methods=['GET','POST'])
def registration_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response("Создаем пользователя")
        response.set_cookie('username', name)
        response.set_cookie('email', email)
        return redirect(url_for('hello', name=name))
    
    return render_template('registration_form.html')
        
@app.route('/getcookie')
def get_cokies():
    name = request.cookies.get('username')
    return f"Значение cokie: {name}"


if __name__ == "__main__":
    app.run(debug=True)
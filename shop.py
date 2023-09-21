from flask import Flask, render_template


app = Flask(__name__)

@app.get('/')
def main_page():
    return render_template('main.html')


@app.get('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.get('/shoes/')
def shoes():
    return render_template('shoes.html')

@app.get('/jacket/')
def jacket():
    return render_template('jacket.html')



if __name__ == ('__main__'):
    app.run(debug=True)
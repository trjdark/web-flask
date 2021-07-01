from flask import Flask
from flask import url_for, escape, render_template
from conf.config import *
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    return render_template('index.html', name = name, movies = movies)

@app.route('/user/<id>')
def user(id):
    db = SQLManager()
    user = db.get_one('SELECT * from `chart_user` where id = ' + id)
    db.close()
    if (user == None):
        return  'no user'
    else:
        return 'user: ' + user['username']

@app.route('/test')
def a():
    user = {
        'username': 'jack',
        'age': '23'
    }

    return '''
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!, you’re ''' + user['age'] + ''' years old.</h1>
        </body>
    </html>
    
    '''
if __name__ =="__main__":
    app.run(debug=True,port=8080)


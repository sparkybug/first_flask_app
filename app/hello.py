from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# @app.route('/hello/<name>')

# def hello_name(name):
#     return 'Hello %s!' % name

# if __name__ == '__main__':
#     app.run(debug=True)

# Another example of url

# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#     return 'Blog Number %d' % postID

# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#     return 'Revision Number %f' % revNo

# if __name__ == '__main__':
#     app.run()

# url_for() script example

# @app.route('/admin')
# def hello_admin():
#     return 'Hello, Admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'Hello %s as Guest' % guest

# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))

# if __name__ == '__main__':
#     app.run(debug=True)

# A simple flask app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
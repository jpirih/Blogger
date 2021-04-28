from flask import Flask, render_template


# Create Flask instance
app = Flask(__name__)


# -------------------Create route decorator ------------------
@app.route('/')
def index():
    first_name = 'Janko'
    title = 'Home'
    return render_template('index.html', first_name=first_name, title=title)


@app.route('/users/<username>')
def user(username):
    title = 'User Profile'
    return render_template('user.html', username=username, title=title)


# ------------- Error pages ------------------------------------
# Page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404


# Internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500

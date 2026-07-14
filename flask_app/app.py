# Import flask
from flask import Flask

# Create an Instance of a flask class
# ''__name__" is a special variable that tells Flask where to look for resouces

app = Flask(__name__)

#Decorator: /about : Maps the URL '/' 

@app.route('/')

# Define a function to display text Welcome to Flask

def home():
    # Write the Text that can be displayed on your browser
    return '<h1> Welcom to Flask Framework </h2>'
#roue o abou

@app.route('/about')
def about():
    return '<h1> i love flask </h1>'

#route for /contact
@app.route('/contact')
def contact():
    return '<h1> Contact us </h1>'

#route for /myStory
@app.route('/myStory')
def myStory():
    return '<h1> My Story </h1>'

#dynamic routing
@app.route('/contact/<name>')

def contacts(name):
    return f'welcome to {name}'

# To Ensure your server runs only if this script is executed directly

if __name__ == '__main__':
    app.run(debug=True)
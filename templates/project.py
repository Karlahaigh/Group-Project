from flask import Flask, request, render_template  #redirect  #url_for
import random

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

personne = 'person'
#person = request.form['person']
greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])

@app.route('/', methods=['GET','POST'])
#def hello_person():
def home():
    error=None
    if request.method=='POST':
        if request.form['person']=="":
            error = 'Please enter your name.'
        else:
            return render_template('intro.html',greet=greet, personne=request.form['person'])
    return render_template('home.html', error=error)

#@app.route('/greet') #,methods=['GET','POST']
#def greet():
 #   global personne
 #   greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
 #   personne = request.form['person']
 #   return render_template('greet.html', greet, personne)

@app.route('/intro')
def intro():
    global personne
    greet = random.choice(["Welcome", "Hello", "Greetings", "Hi"])
    return render_template('intro.html', greet = greet, personne = personne)

    #intro = paragraph"

@app.route('/option1')
def option1():
    #option1 =  page of option 1
    return render_template('option1.html')

@app.route('/option2')
def option2():
    global personne
    #return(option2, personne)
    return render_template('option2.html', personne=personne)


from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)    
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')         
def index():
    if 'counter' not in session:
        session ['counter'] = 0
    session['counter'] +=0    
    return render_template( "index.html", count=session['counter'])  

@app.route('/addone')
def addone():
    session['counter'] +=1
    return redirect('/')

@app.route ('/reset')
def reset():
    session ['counter'] = 0
    return redirect('/')

  
app.run(debug=True)
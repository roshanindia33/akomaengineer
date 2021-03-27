from flask import Flask,render_template,redirect,request
app=Flask(__name__)
# for database
from flask_sqlalchemy import SQLAlchemy

# ****************************************************************************************
# ****************************************************************************************
# *********************************Read Values In csv Files*******************************


app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:/Courses/Flask WebDevlopment/todo.sqllite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creating a class for data getting
class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(500),nullable=False)
    subject = db.Column(db.String(299),nullable=False)
    message = db.Column(db.String(599),nullable=False)
    

    def __init__(self,name,email,subject,message):
        self.name=name
        self.email=email
        self.subject=subject
        self.message=message


    # return
    def __repr__(self) -> str:
        return f"{self.name}  -  {self.email}"

def create(name,email,subject,message):
    # db.create_all()
    all = Todo(name=name,email=email,subject=subject,message=message)
    db.session.add(all)
    db.session.commit()


# ****************************************************************************************
# ****************************************************************************************

# fill contact form on index page
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        if len(name)>1:
            create(name=name,email=email,subject=subject,message=message)
    return render_template('index.html')








# fill contact form on index page

# For Account login or SignUp Form
@app.route('/login')
def login():
    # return render_template('login.html')
    return redirect('/')

@app.route('/forget')
def forget():
    # send password into mail
    return redirect('/')

@app.route('/signup',methods=['GET','POST'])
def signup():
    # return render_template('signup.html')
    return redirect('/')

# ****************************************************************************
# ****************************************************************************
# ****************************************************************************
# ****************************************************************************
# blog,devloper (url)
@app.route('/coming')
def coming():
    return render_template('coming.html')



# For Navigation bar Link's get next page
@app.route('/projects')
def projects():
    return render_template('project.html')

@app.route('/caitalog')
def caitalog():
    return render_template('caitalog.html')


@app.route('/datasets')
def datasets():
    return render_template('coming.html')


@app.route('/competition')
def competition():
    return render_template('coming.html')


@app.route('/notebook')
def notebook():
    return render_template('coming.html')

# For Courses Caitalog link's next pages
@app.route('/artificial-intelligence')
def artificial_intelligence():
    return redirect('/')


@app.route('/reinforcement-learning')
def reinforcement_learning():
    return redirect('/')


@app.route('/deep-learning')
def deep_learning():
    return redirect('/')

@app.route('/machine-learning')
def machine_learning():
    return redirect('/')


@app.route('/data-science')
def data_science():
    return redirect('/')


@app.route('/python-course')
def python_course():
    return redirect('/')


@app.route('/akomaweb')
def akoma():
    return render_template('boost.html')


@app.route('/blog')
def blog():
    return render_template('coming.html') #change this file fasly


# *********************************************************************

# About page
@app.route('/about-akoma')
def about_akoma():
    return render_template('about.html')

# **********************************************************************

@app.route('/privacy-policy')
def privacy():
    return render_template('privacypolicy.html')


@app.route('/terms&conditions')
def terms():
    return render_template('terms.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')


@app.route('/devloper')
def devloper():
    return render_template('coming.html')

@app.route('/career')
def career():
    return render_template('coming.html')














# run app
if __name__=="__main__":
    app.run(debug=False)
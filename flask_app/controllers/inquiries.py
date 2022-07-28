from flask_app import app
from flask import flash, render_template,redirect,request,session
from flask_app.models.inquiry import Inquiry
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

site_title = "seVIIn's Studio"

#Home
@app.route('/')
def index():
    return render_template('index.html', title = site_title)

@app.route('/inquiry_form', methods = ['POST'])
def inquiry_form():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'return_email_address' : request.form['return_email_address'],
        'subject' : request.form['subject'],
        'message' : request.form['message']
    }

    # print(first_name, last_name, return_email_address, subject, message)
    Inquiry.create(data)

    return redirect('/')


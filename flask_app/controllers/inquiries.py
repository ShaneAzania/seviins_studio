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
    session['first_name'] = data['first_name']
    session['last_name'] = data['last_name']
    session['return_email_address'] = data['return_email_address']
    session['subject'] = data['subject']
    session['message'] = data['message']
    print()
    print('INQUIRY PROJECT TYPE / SUBJECT:',session['subject'])
    print()
    if Inquiry.validate_form(data):
        session.pop('first_name')
        session.pop('last_name')
        session.pop('return_email_address')
        session.pop('subject')
        session.pop('message')
        # print(first_name, last_name, return_email_address, subject, message)
        Inquiry.create(data)
    return redirect('/#nav')


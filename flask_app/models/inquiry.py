from flask import flash, session
from flask_app.assets.regex import EMAIL_REGEX
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import sighting

class Inquiry :
    db = "seviins_studio"
    db_table = 'inquiries'
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.return_email_address = db_data['return_email_address']
        self.subject = db_data['subject']
        self.message = db_data['message']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    # **********************************************************************************************************************************
    # create*****************************************************************
    @classmethod
    def create( cls , data ):
        query = "INSERT INTO " + cls.db_table + " ( first_name, last_name, return_email_address, subject, message ) VALUES ( %(first_name)s, %(last_name)s, %(return_email_address)s, %(subject)s, %(message)s );"
        return connectToMySQL(cls.db).query_db( query, data)
    #**********************************************************************************************************************************
    #retreive*****************************************************************
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM " + cls.db_table + ";"
        result =  connectToMySQL(cls.db).query_db(query)
        all =[]
        if result:
            for x in result:
                all.append(cls(x))
            return all
        else:
            print()
            print(f'Inquiry.get_all() NO ROWS IN DATABASE')
            print()
            return all
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM " + cls.db_table + " WHERE id = %(id)s;"
        result =  connectToMySQL(cls.db).query_db(query,data)
        if result: 
            return cls(result[0])
        else:
            print()
            print(f'Inquiry.get_one( {data["id"]} ) IS NOT IN DATABASE')
            print()
            return result
    #**********************************************************************************************************************************
    #delete*****************************************************************
    @classmethod
    def delete (cls, data):
        query = "DELETE FROM " + cls.db_table + " WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db( query, data)

    def validate_form(data):
        valid = True
        if len(data['first_name']) < 3:
            valid = False
            flash('First name must be at least 3 characters long.', 'first_name')
        if len(data['last_name']) < 3:
            valid = False
            flash('Last name must be at least 3 characters long.', 'last_name')
        if not EMAIL_REGEX.match(data['return_email_address']):
            valid = False
            flash('Please provide a valid email address (  example@email.com ).', 'return_email_address')
        if data['subject'] == "Website/Application Development(Ecommerce)" or data['subject'] == "Website/Application Development(Portfolio)" or data['subject'] == "Website/Application Development(Blog)" or data['subject'] == "Website/Application Development(Other)" or data['subject'] == "Photogrphy(Commercial/Business Purposes)" or data['subject'] == "Photogrphy(Portrait)" or data['subject'] == "Photogrphy(Event)" or data['subject'] == "Photography(Other)" or data['subject'] == "Video(Commercial/Business Purposes)" or data['subject'] == "Video(Behind The Scenes)" or data['subject'] == "Video(Documentary)" or data['subject'] == "Video(Interview)" or data['subject'] == "Video(Music Video)" or data['subject'] == "Video(Other)":
            None
        else:
            valid = False
            flash('Please select a project type.', 'subject')
        if len(data['message']) < 10:
            valid = False
            flash('Please leave a detailed message.', 'message')

        if valid:
            flash('Message Sent. Thankyou!', 'success')
        return valid
        '''
        {% with messages = get_flashed_messages(category_filter=["error"]) %}
        {% if messages %}
        <div class="alert-message block-message error">
        <a class="close" href="#">×</a>
        <ul>
            {%- for msg in messages %}
            <li>{{ msg }}</li>
            {% endfor -%}
        </ul>
        </div>
        {% endif %}
        {% endwith %}
        '''


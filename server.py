from flask import Flask, flash, render_template, url_for, request, redirect
import csv
from secret_key import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/')
def index():
    """Display Landing Page"""
    return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)
# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email}, \n{subject}, \n{message},\n-----------')


def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            print(data)
            flash('Thank You! I will get in touch with you, shortly!')
            return redirect('/')
        except Exception as e:
            print(e)
            return 'Did not save to database'
    else:
        flash('Something went wrong, try again!')
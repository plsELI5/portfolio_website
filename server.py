from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv


@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_name(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\nEmail: {email}\nSubject: {subject}\nMessage: {message}')  

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csv_database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Did not save to database."
    else:
        return 'Something went wrong. Try again.'



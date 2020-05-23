from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

# Routes listed here
# route to home page
@app.route('/')
def index():
    return render_template('index.html')

# route to projects page
@app.route('/works')
def works():
    return render_template('works.html')

# route to about me page
@app.route('/about')
def about():
    return render_template('about.html')
    
# route to contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# route to thank you page
@app.route('/thankyou')
def thanks():
    return render_template('thankyou.html')

# save form data to csv file
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as csv_database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_database, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# form submission route
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'did not save to csv'
    else:
        return 'something went wrong'

# if this page is the main page, run it
if __name__ == '__main__':
    app.run(debug=True)

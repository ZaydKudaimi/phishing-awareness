from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cs166team1@gmail.com'
app.config['MAIL_PASSWORD'] = 'oiqypvbuoabcrbpy'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/home', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        msg = Message(
            "Hey", 
            sender='noreply@demo.com', 
            recipients=['san.vu@sjsu.edu']
        )
        msg.subject = "Subject"
        msg.body = "Hi" 
        mail.send(msg)
        return "Sent email."
    return render_template('index.html');

if __name__ == '__main__':
    app.run(debug=True)

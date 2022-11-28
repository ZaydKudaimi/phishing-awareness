from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mail import Mail, Message
from deta import Deta

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cs166team1@gmail.com'
app.config['MAIL_PASSWORD'] = 'oiqypvbuoabcrbpy'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

deta = Deta("b0yvgkme_J3ubJYBx9wYFeEBpwx7qk9sLuKykNjiD")
db = deta.Base("db")

@app.route('/home', methods=['GET','POST'])
@app.route('/', methods=['GET','POST'])
def home():
    db.put({"key": "counter", "counter": 0})

    if request.method == 'POST':
        msg = Message(
            "Hey", 
            sender='noreply@demo.com', 
            recipients=['james.yu@sjsu.edu']
            #recipients=
            #[
            #    'shohin.abdulkhamidov@sjsu.edu', 'tejas.aditya@sjsu.edu', 'zaria.baker@sjsu.edu', 'jonathan.borda@sjsu.edu', 'hohin.chan@sjsu.edu', 
            #    'tommy.dao@sjsu.edu', 'anh.dinh@sjsu.edu', 'eivind.eckhoff@sjsu.edu', 'ask.ekrareistad@sjsu.edu', 'harrison.yu@sjsu.edu',
            #    'vidhyut.gopinath@sjsu.edu', 'sriram.govindan@sjsu.edu', 'samanthaelaine.guanzon@sjsu.edu', 'yunseo.han@sjsu.edu',
            #    'ryan.hedgecock@sjsu.edu', 'elizabeth.huelfenhaus@sjsu.edu', 'sahana.ilenchezhian@sjsu.edu', 'muhammad.a.jeelani@sjsu.edu',
            #    'abhayjot.johal@sjsu.edu', 'jason.khy@sjsu.edu', 'isaac.kim@sjsu.edu', 'ryan.kwong@sjsu.edu', 'victor.la@sjsu.edu',
            #    'joshua.lawson@sjsu.edu', 'thuynhatphuong.le@sjsu.edu', 'vivian.letran@sjsu.edu', 'tristan.lorenzo@sjsu.edu', 'dylan.zeglinski@sjsu.edu',
            #    'alan.luu@sjsu.edu', 'ali.ma@sjsu.edu', 'lexin.ma@sjsu.edu', 'volodymyr.makarenko@sjsu.edu', 'farah.masood@sjsu.edu',
            #    'siri.mudumbi@sjsu.edu', 'arun.murugan@sjsu.edu', 'anjana.nambiar@sjsu.edu', 'huy.ong@sjsu.edu', 'cody.ourique@sjsu.edu',
            #    'danh.pham@sjsu.edu', 'doan.pham@sjsu.edu', 'eric.p.pham@sjsu.edu', 'truc.t.phan@sjsu.edu', 'chiranjeev.puri@sjsu.edu',
            #    'praggathi.rajarao@sjsu.edu', 'austin.rivard@sjsu.edu', 'vladislav.semenyutin@sjsu.edu', 'temuudei.shiilegdamba@sjsu.edu',
            #    'harmandeepsingh@sjsu.edu', 'inderpreet.singh01@sjsu.edu', 'hyeonmin.song@sjsu.edu', 'jimin.song@sjsu.edu', 'steven.ta@sjsu.edu',
            #    'lovepreet.uppal@sjsu.edu', 'saharsh.vedi@sjsu.edu', 'karanpartap.virk@sjsu.edu', 'angela.yang@sjsu.edu', 'atsuya.yano@sjsu.edu'
            #    'justin.barragan@sjsu.edu', 'zayd.kudaimi@sjsu.edu', 'san.vu@sjsu.edu', 'james.yu@sjsu.edu'
            #]
        )
        msg.subject = "Subject"
        link = url_for('home', _external=True)
        msg.body = '{}'.format(link)
        mail.send(msg)
        return "Sent email."
    return render_template('index.html')

@app.route('/pages', methods=['GET'])
def pages():
    db.put({"key": "counter", "counter": db.get("counter")["counter"]+1})
    pass

@app.route('/page', methods=['GET'])
def page():
    pass

#if __name__ == "__main__":
#    app.run(debug=True)
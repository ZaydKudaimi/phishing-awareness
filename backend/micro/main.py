from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from deta import Deta
#from react.render import render_component

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'cs166team1@gmail.com'
app.config['MAIL_PASSWORD'] = 'oiqypvbuoabcrbpy'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
classmates1=[
    'shohin.abdulkhamidov@sjsu.edu', 'tejas.aditya@sjsu.edu', 'zaria.baker@sjsu.edu', 'jonathan.borda@sjsu.edu', 'hohin.chan@sjsu.edu', 
    'tommy.dao@sjsu.edu', 'anh.dinh@sjsu.edu', 'eivind.eckhoff@sjsu.edu', 'ask.ekrareistad@sjsu.edu', 'harrison.yu@sjsu.edu',
    'vidhyut.gopinath@sjsu.edu', 'sriram.govindan@sjsu.edu', 'samanthaelaine.guanzon@sjsu.edu', 'yunseo.han@sjsu.edu',
    'ryan.hedgecock@sjsu.edu', 'elizabeth.huelfenhaus@sjsu.edu', 'sahana.ilenchezhian@sjsu.edu', 'muhammad.a.jeelani@sjsu.edu',
    'justin.barragan@sjsu.edu', 'zayd.kudaimi@sjsu.edu', 'san.vu@sjsu.edu', 'james.yu@sjsu.edu'
]
classmates2=[
    'abhayjot.johal@sjsu.edu', 'jason.khy@sjsu.edu', 'isaac.kim@sjsu.edu', 'ryan.kwong@sjsu.edu', 'victor.la@sjsu.edu',
    'joshua.lawson@sjsu.edu', 'thuynhatphuong.le@sjsu.edu', 'vivian.letran@sjsu.edu', 'tristan.lorenzo@sjsu.edu', 'dylan.zeglinski@sjsu.edu',
    'alan.luu@sjsu.edu', 'ali.ma@sjsu.edu', 'lexin.ma@sjsu.edu', 'volodymyr.makarenko@sjsu.edu', 'farah.masood@sjsu.edu',
    'siri.mudumbi@sjsu.edu', 'arun.murugan@sjsu.edu', 'anjana.nambiar@sjsu.edu', 'huy.ong@sjsu.edu', 'cody.ourique@sjsu.edu',
    'justin.barragan@sjsu.edu', 'zayd.kudaimi@sjsu.edu', 'san.vu@sjsu.edu', 'james.yu@sjsu.edu'
]
classmates3=[
    'danh.pham@sjsu.edu', 'doan.pham@sjsu.edu', 'eric.p.pham@sjsu.edu', 'truc.t.phan@sjsu.edu', 'chiranjeev.puri@sjsu.edu',
    'praggathi.rajarao@sjsu.edu', 'austin.rivard@sjsu.edu', 'vladislav.semenyutin@sjsu.edu', 'temuudei.shiilegdamba@sjsu.edu',
    'harmandeepsingh@sjsu.edu', 'inderpreet.singh01@sjsu.edu', 'hyeonmin.song@sjsu.edu', 'jimin.song@sjsu.edu', 'steven.ta@sjsu.edu',
    'lovepreet.uppal@sjsu.edu', 'saharsh.vedi@sjsu.edu', 'karanpartap.virk@sjsu.edu', 'angela.yang@sjsu.edu', 'atsuya.yano@sjsu.edu',
    'justin.barragan@sjsu.edu', 'zayd.kudaimi@sjsu.edu', 'san.vu@sjsu.edu', 'james.yu@sjsu.edu'
]
teammates=[
    'justin.barragan@sjsu.edu', 'zayd.kudaimi@sjsu.edu', 'san.vu@sjsu.edu', 'james.yu@sjsu.edu'
]

deta = Deta("b0yvgkme_J3ubJYBx9wYFeEBpwx7qk9sLuKykNjiD")
db = deta.Base("db")

### ------------ SEND EMAILS OUT --------------
@app.route('/send', methods=['GET','POST'])
def home():
    #db.put({"key": "google-email-clicks", "counter": 0})
    #db.put({"key": "google-phish-clicks", "counter": 0})
    #db.put({"key": "facebook-email-clicks", "counter": 0})
    #db.put({"key": "facebook-phish-clicks", "counter": 0})
    #db.put({"key": "sjsu-email-clicks", "counter": 0})
    #db.put({"key": "sjsu-phish-clicks", "counter": 0})

    if request.method == 'POST':
        msg1 = Message(
            "Hey", 
            sender='noreply@demo.com', 
            recipients=classmates1
        )
        msg1.subject = "[IMPORTANT] Google Password Reset"

        msg2 = Message(
            "Hey", 
            sender='noreply@demo.com', 
            recipients=classmates2
        )
        msg2.subject = "[IMPORTANT] Facebook Password Reset"

        msg3 = Message(
            "Hey", 
            sender='noreply@demo.com', 
            recipients=classmates3
        )
        msg3.subject = "[IMPORTANT] SJSU Password Reset"

        msg1.html = render_template('gmail.html')
        msg2.html = render_template('facebook_email.html')
        msg3.html = render_template('sjsu-email.html')

        mail.send(msg1)
        mail.send(msg2)
        mail.send(msg3)
        return "Sent email."
    return render_template('sent.html')

### ------------ PHISHER ROUTES --------------
#google password phisher
@app.route('/google', methods=['GET'])
def reset():
    db.put({"key": "google-email-clicks", "counter": db.get("google-email-clicks")["counter"]+1})
    return render_template('google_phish.html')

#facebook password phisher
@app.route('/facebook', methods=['GET'])
def facebook():
    db.put({"key": "facebook-email-clicks", "counter": db.get("facebook-email-clicks")["counter"]+1})
    return render_template('facebookindex.html')

#sjsu password phisher
@app.route('/sjsu', methods=['GET'])
def sjsu():
    db.put({"key": "sjsu-email-clicks", "counter": db.get("sjsu-email-clicks")["counter"]+1})
    return render_template('sjsu_phish.html')



### ------------ YOU HAVE BEEN PHISHED ROUTES --------------
# I had to create 3 different phished routes to keep track of clicks separately(and lazy)
#you have been phished by google!
@app.route('/phished1', methods=['GET'])
def phished1():
    db.put({"key": "google-phish-clicks", "counter": db.get("google-phish-clicks")["counter"]+1})
    return 'You have been phished by Team 1 in Professor Tarngs CS166 class(Do not worry, none of your information was saved).'

#you have been phished by facebook!
@app.route('/phished2', methods=['GET'])
def phished2():
    db.put({"key": "facebook-phish-clicks", "counter": db.get("facebook-phish-clicks")["counter"]+1})
    return 'You have been phished by Team 1 in Professor Tarngs CS166 class(Do not worry, none of your information was saved).'

#you have been phished by sjsu!
@app.route('/phished3', methods=['GET'])
def phished3():
    db.put({"key": "sjsu-phish-clicks", "counter": db.get("sjsu-phish-clicks")["counter"]+1})
    return 'You have been phished by Team 1 in Professor Tarngs CS166 class(Do not worry, none of your information was saved).'

#if __name__ == "__main__":
#    app.run(debug=True)
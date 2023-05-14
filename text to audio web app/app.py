from flask import *
from gtts import gTTS

app=Flask(__name__,static_folder='static/')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert',methods=['POST'])
def convert():
    if request.method=='POST':
        data=request.form['data']
        myfile=gTTS(text=data,lang='en',slow=False)
        myfile.save('./media/output.mp3')

    return render_template('download.html')

@app.route('/download',methods=['POST'])
def download():
    if request.method=='POST':
        return send_file('./media/output.mp3',as_attachment=True)

app.run()
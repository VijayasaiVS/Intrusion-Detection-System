import os
import shutil
from flask import *
from flask.templating import render_template
import pandas as pd
import chart_studio.tools as tls
import chart_studio
import chart_studio.plotly as py
import plotly.express as px
from werkzeug.utils import secure_filename
from dotenv import load_dotenv, main
load_dotenv()

app=Flask(__name__,static_folder='../frontend',template_folder='../frontend/views')
app.secret_key=os.getenv('SECRET_KEY')
upload_folder = os.getenv('UPLOAD_FOLDER')
data_folder=os.getenv('DATA_FOLDER')
@app.route("/")
def index():
    session.clear
    return render_template('index.html')

@app.route("/intrusion")
def intrusion():
    return render_template('intrusion.html')

@app.route("/upload",methods=['POST'])
def upload():
    if request.method == 'POST':
      f = request.files['upload_file']
      filename=secure_filename(f.filename)
      ext=os.path.splitext(filename)
      session['file_ext']=ext[-1]
      if not ext[-1]=='.csv':
          flash('File is not compatible!!\n Choosen file is {0} expected is .csv'.format(ext[-1]))
          return redirect('/intrusion')
      f.save(os.path.join(upload_folder,filename))
      src_folder=os.path.join(upload_folder,filename)
      dest_folder=os.path.join(data_folder,'data.csv')
      shutil.move(src_folder, dest_folder)
    return render_template('report.html',op=ext)

if __name__=='__main__':
    app.run(host='localhost',port=os.getenv('PORT'),debug=True)
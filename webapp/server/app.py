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
import module as md
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
    session.clear
    return render_template('intrusion.html')

@app.route("/upload",methods=['POST'])
def upload():
    f = request.files['upload_file']
    filename=secure_filename(f.filename)
    session['filename']=filename
    ext=os.path.splitext(filename)
    if not ext[-1]=='.csv':
        flash('File is not compatible!!\n Choosen file is {0} expected is .csv'.format(ext[-1]))
        return redirect('/intrusion')
    f.save(os.path.join(upload_folder,filename))
    src_file=os.path.join(upload_folder,filename)
    dest_file=os.path.join(data_folder,'data.csv')
    shutil.move(src_file, dest_file)
    if not md.check_columns(dest_file):
        if os.path.exists(dest_file):
            os.remove(dest_file)
        flash('The given CSV file cannot be predicted since there are some missing features')
        return redirect('/intrusion')
    
    prediction_df=md.predict(dest_file)
    md.save_csv(prediction_df,(os.path.join(data_folder,'predicted_data.csv')))
    label_info,data_length,total_accuracy,each_label_accuracy=md.predict_info(prediction_df)
    render_content={
                    'filename': filename,
                    'data_length':data_length,
                    'accuracy':total_accuracy,
                    }
    return render_template('report.html',**render_content)

@app.route("/download/csv")
def download():
    return send_from_directory(directory=data_folder, filename='predicted_data.csv',as_attachment=True)

if __name__=='__main__':
    app.run(host='localhost',port=os.getenv('PORT'),debug=True)
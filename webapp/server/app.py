import os
import shutil
from flask import *
from numpy.core.fromnumeric import mean
import pandas as pd
from werkzeug.utils import secure_filename
import module as md
from dotenv import load_dotenv, main
load_dotenv()

app=Flask(__name__,static_folder='../frontend',template_folder='../frontend/views')
app.secret_key=os.getenv('SECRET_KEY')
upload_folder = os.getenv('UPLOAD_FOLDER')
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)
data_folder=os.getenv('DATA_FOLDER')
if not os.path.exists(data_folder):
    os.mkdir(data_folder)
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
    label_info,data_length,total_accuracy=md.predict_info(prediction_df)
    anomaly_score,anomaly_info=md.anomaly_count(label_info)
    mean_score=md.label_items(prediction_df)
    plot0=md.plot_bar(mean_score,mean_score['Type'],mean_score['Accuracy Score'],'Predicted Accuracy of Each Category')
    plot1=md.plot_pie(anomaly_info,anomaly_info['Type'],anomaly_info['No. of Data'],'Intrusion Detection')
    plot2=md.plot_pie(label_info,label_info['Label'],label_info['No. of Data'],'Detailed Categorization of Attack')
    render_content={
                    'filename': filename,
                    'data_length':data_length,
                    'accuracy':total_accuracy,
                    'anomaly_score':anomaly_score,
                    'plot0':plot0,
                    'plot1':plot1,
                    'plot2':plot2
                    }
    return render_template('report.html',**render_content)

@app.route("/download/csv")
def download():
    return send_from_directory(directory=data_folder, filename='predicted_data.csv',as_attachment=True)

if __name__=='__main__':
    app.run(host='localhost',port=os.getenv('PORT'),debug=True)
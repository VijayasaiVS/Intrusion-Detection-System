import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from pycaret.classification import *
import plotly.express as px
import chart_studio
import chart_studio.tools as tls
import chart_studio.plotly as py

req_columns=['duration', 'protocol_type','service','flag','src_bytes', 'dst_bytes', 'land', 'hot', 'logged_in', 'num_compromised',
            'su_attempted', 'num_root', 'num_file_creations', 'is_host_login', 'is_guest_login', 'count','srv_count', 'serror_rate', 
            'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate','srv_diff_host_rate', 'dst_host_count', 
            'dst_host_srv_count','dst_host_same_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_serror_rate',
            'dst_host_srv_serror_rate','dst_host_rerror_rate', 'dst_host_srv_rerror_rate']


def check_columns(f):
    data=pd.read_csv(f)
    list_columns=data.columns.tolist()
    check = all(item in list_columns for item in req_columns)
    return check

def predict(src):
    data=pd.read_csv(src)
    prediction=load_model(os.getenv('MODEL_LOC'))
    prediction_df=predict_model(estimator=prediction,data=data)
    return prediction_df

def save_csv(dataframe,loc):
    dataframe.to_csv(loc,index=False)
    return ("Saved at: ",loc)

def predict_info(dataframe):
    label_info = pd.DataFrame(dataframe['Label'].value_counts().reset_index().values, columns=["Label", "No. of Data"])
    data_length=len(dataframe['Label'])
    accuracy=round((dataframe['Score'].mean()*100),4)
    label_items=dataframe['Label'].unique().tolist()
    return label_info,data_length,accuracy

def anomaly_count(label_info):
    temp=label_info[label_info['Label']=='normal']
    total_no_of_data=label_info['No. of Data'].sum()
    normal_count=int(temp['No. of Data'])
    anomaly_count=total_no_of_data-normal_count
    anomaly_percent=anomaly_count/total_no_of_data*100
    anomaly_info={
        'Type':['normal','anomaly'],
        'No. of Data':[normal_count,anomaly_count]}
    anomaly_info=pd.DataFrame.from_dict(anomaly_info)
    if anomaly_count>25:
        return "Moderate",anomaly_info
    elif anomaly_count>50:
        return "Severe",anomaly_info
    else:
        return "Good",anomaly_info
        
def label_items(prediction_df):
    label_items=prediction_df['Label'].unique().tolist()
    accuracy=[]
    for i in label_items:
        temp=prediction_df[prediction_df['Label']==i]
        accuracy.append(round(temp['Score'].mean()*100,4))
    mean_score={
        'Type':label_items,
        'Accuracy Score': accuracy
    }
    mean_score=pd.DataFrame.from_dict(mean_score)
    return mean_score

def plot_bar(dataframe,x,y,title):
    plot1=px.bar(dataframe,x=x,y=y,color=x,title=title)
    fig1=py.plot(plot1,filename=title,auto_open=False)
    return tls.get_embed(fig1)

def plot_pie(dataframe,name,value,title):
    plot1=px.pie(dataframe,names=name,values=value,title=title)
    fig1=py.plot(plot1,filename=title,auto_open=False)
    return tls.get_embed(fig1)
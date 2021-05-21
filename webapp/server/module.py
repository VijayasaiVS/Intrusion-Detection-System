import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from pycaret.classification import *

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
    each_label_accuracy=[]
    for i in label_items:
        temp=dataframe[dataframe['Label']==i]
        each_label_accuracy.append(round(temp['Score'].mean()*100,4))
    return label_info,data_length,accuracy,each_label_accuracy
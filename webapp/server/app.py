import os
from flask import Flask, request,session
from flask.templating import render_template
import pandas as pd
import chart_studio.tools as tls
import chart_studio
import chart_studio.plotly as py
import plotly.express as px
from dotenv import load_dotenv, main
load_dotenv()

app=Flask(__name__,static_folder='../frontend',template_folder='../frontend/views')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/intrusion")
def intrusion():
    return render_template('intrusion.html')

if __name__=='__main__':
    app.run(host='localhost',port=os.getenv('PORT'),debug=True)
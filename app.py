from flask import Flask, request, render_template
import numpy as np
import re
import requests

app = Flask(__name__)


def check(typ,output):
    url = "https://api.deepai.org/api/summarization"
    payload = {"text": output}
    print(payload)
    headers = {'api-key': '79728e79-d56e-40bc-be98-ece560a7dd3c'}
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    return response.json()["output"]

#page for home
@app.route('/')
def home():
    return render_template('home.html')

#page for summarizer input
@app.route('/summarizer')
def summarizer():
    return render_template('summarizer.html')

#output page
@app.route('/summarize',methods=['POST'])
def summarize():
    typ=request.form['type']
    output = request.form['output']
    if typ=="text":
        output=re.sub("[^a-zA-Z.,]"," ",output)
    print(output)
    essay = check(typ,output)
    return render_template('summary.html',essay=essay)
 
if __name__ == "__main__":
    app.run(debug=True)
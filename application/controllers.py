from flask import request, redirect, url_for, flash
from flask import render_template
from flask import current_app as app
from application.models import Data
from .database import db
from datetime import datetime as dt
import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from bs4 import BeautifulSoup as bs
import requests

label= {
    0:"business",
    1:"entertainment",
    2:"politics",
    3:"sport",
    4:"tech"
  }

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template('Home.html')
    else:
        url = request.form['url']

        re = requests.get(url)
        soup = bs(re.content,'html.parser')
        text = soup.find('article').get_text()

        words = text.split()[:300]
        limited_text = ' '.join(words)
        
        # tokenizer = AutoTokenizer.from_pretrained("abhishek/autonlp-bbc-news-classification-37229289")
        # model = AutoModelForSequenceClassification.from_pretrained("abhishek/autonlp-bbc-news-classification-37229289")

        # inputs = tokenizer(limited_text, return_tensors="pt")
        # output = model(**inputs).logits[0].tolist()

        # category = label[output.index(max(output))]

        API_URL = "https://api-inference.huggingface.co/models/abhishek/autonlp-bbc-news-classification-37229289"
        headers = {"Authorization": "Bearer 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"}

        response = requests.post(API_URL, headers=headers, json={"inputs": limited_text})
        output = response.json()
        print(output)

        category = output[0][0]['label']

        data = Data(url=url, category=category)
        db.session.add(data)
        db.session.commit()

        rows = Data.query.all()

        return render_template('Prediction.html',url=url, category=category, rows=rows)
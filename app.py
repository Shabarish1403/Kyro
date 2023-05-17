from bs4 import BeautifulSoup as bs
import streamlit as st
import requests
from requests.exceptions import *
from sqlalchemy.orm import sessionmaker
from models import Data
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data.sqlite3')
Session = sessionmaker(bind=engine)
db = Session()

#Functions
def scrape(url):
    re = requests.get(url)
    soup = bs(re.content,'html.parser')
    # text = soup.find('article').get_text()
    text = "".join(soup.strings)

    words = text.split()[:100]
    content = ' '.join(words)

    return content

def predict(content):
    API_URL = "https://api-inference.huggingface.co/models/abhishek/autonlp-bbc-news-classification-37229289"
    headers = {"Authorization": "Bearer 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"}

    response = requests.post(API_URL, headers=headers, json={"inputs": content})
    output = response.json()

    category = output[0][0]['label']

    return category

#Frontend
st.title("News Articles Classification")

st.text_input("Enter URL", key="url")

url = st.session_state.url

try:
    d = db.query(Data).filter(Data.url==url).first()
    if d is not None:
        category = d.category
    else:
        content = scrape(url)
        category = predict(content)

        data = Data(url=url, category=category)
        db.add(data)
        db.commit()

    st.subheader('Result')
    st.success(url+' - '+category)

    rows = db.query(Data).all()
    st.subheader('History')
    with st.container():
        # Place your content inside the expander
        for row in rows[::-1]:
            st.write(row.url, ' - ', row.category)

except MissingSchema as e:
    st.error('Please Enter URL')

except AttributeError as e:
    st.error('Unable to scrape the content from this URL')

except KeyError as e:
    st.error('Too many requests. Please try after sometime')

except Exception as e:
    st.error(e)


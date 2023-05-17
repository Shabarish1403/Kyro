# Kyro Offline Assignment - News Article Classification

## How to run Locally

* Download the repo to local.
* Install all necessary packages with the below command.
```
pip install -r requirements.txt
```
* Run the following code block for to create the sqlite database
```
python3 models.py
```
* Run the following code block to run the app
```
streamlit run app.py
```
* The above command is equivalent to
```
python -m streamlit run app.py
```
* Enter the news article URL in the displayed text box and click ENTER to get the predictions result and history of past requests.

## How to deploy

* Fork the project to github as repository.
* Login to [Streamlit](https://streamlit.io) website with the same mail id as the project repository in which it is present.
* Click on Add App and select the repository and app.py file. Click on deploy.

### Hurray🥳🎉, your app is successfully deployed.
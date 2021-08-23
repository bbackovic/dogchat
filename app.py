from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def feed():

    post1 = {
        "Text": "I can't wait to go to the park today!",
        "Name": "Cloud", 
        "Username": "cloud",
        "LikeCount": 10, 
        "CommentCount": 4,
        "DateTime": datetime(2021, 7, 1, 17, 0, 0),
        "Picture": 'Dog1.jpg'
    }
    post2 = {
        "Text": "Me too! Can I join in?",
        "Name": "Fluffy", 
        "Username": "fluffy",
        "LikeCount": 5, 
        "CommentCount": 4,
        "DateTime": datetime(2021, 7, 1, 19, 0, 0),
        "Picture": 'doggy.jpg'
    }
    post3 = {
        "Text": "Yes! Ruff ruff",
        "Name": "Cloud", 
        "Username": "cloud",
        "LikeCount": 8, 
        "CommentCount": 2,
        "DateTime": datetime(2021, 7, 1, 20, 30, 0),
        "Picture": 'Dog1.jpg'
    }
    
    test_posts = [post1, post2, post3]

    return render_template('index.html', posts=test_posts)
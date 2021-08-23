from datetime import datetime

comment1 = {
    "Text" : "What time are you going?",
    "Name" : "Fluffy",
    "Username": "fluffy",
    "DateTime": datetime(2021, 7, 1, 18, 0, 0),
    "Picture": "doggy.jpg"
}
comment2 = {
    "Text" : "I'm going to go at 7 tonight!",
    "Name" : "Cloud",
    "Username": "cloud",
    "DateTime": datetime(2021, 7, 1, 19, 30, 0),
    "Picture": "Dog1.jpg"
}
comment3 = {
    "Text" : "You bet!",
    "Name" : "Fluffy",
    "Username": "fluffy",
    "DateTime": datetime(2021, 7, 1, 21, 30, 0),
    "Picture": "doggy.jpg"
}
post1 = {
        "PostID": 1,
        "Text": "I can't wait to go to the park today!",
        "Name": "Cloud", 
        "Username": "cloud",
        "Likes": ["fluffy"], 
        "Comments": [comment1, comment2],
        "DateTime": datetime(2021, 7, 1, 17, 0, 0),
        "Picture": 'Dog1.jpg'
    }
post2 = {
        "PostID": 2,
        "Text": "Me too! Can I join in?",
        "Name": "Fluffy", 
        "Username": "fluffy",
        "Likes": ["cloud"], 
        "Comments": [],
        "DateTime": datetime(2021, 7, 1, 19, 0, 0),
        "Picture": 'doggy.jpg'
    }
post3 = {
        "PostID": 3,
        "Text": "Yes! Ruff ruff",
        "Name": "Cloud", 
        "Username": "cloud",
        "Likes": ["fluffy"], 
        "Comments": [comment3],
        "DateTime": datetime(2021, 7, 1, 20, 30, 0),
        "Picture": 'Dog1.jpg'
    }
    
test_posts = {
    1 : post1,
    2 : post2, 
    3 : post3
}
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), 
        user=os.getenv("MYSQL_USER"), 
        password=os.getenv("MYSQL_PASSWORD"), 
        host=os.getenv("MYSQL_HOST"), 
        port=3306
    )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

"""
class nav:
    def __init__(self, url, people, label):
        self.url = url
        self.people = people
        self.label = label

profile_nav = nav(
    ["", "work_edu", "hobbies"],
    ["amber", "jacky", "william"],
    ["About Me", "Work Experience/Education", "Hobbies"]
)
"""



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    gname = request.form.get('name')
    if (gname == None) or (gname == ""):
        return "Invalid name", 400
    else:
        name = request.form['name']
    email = request.form['email']
    if "@" not in email and ".com" not in email:
        return "Invalid email", 400
    content = request.form['content']
    if content == "":
        return "Invalid content", 400
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")



""""
# for amber page
@app.route('/amber')
def amber():
    return render_template('amber.html', nav=profile_nav, title="Amber", url=os.getenv("URL"))

# for jacky page
@app.route('/jacky')
def jacky():
    return render_template('jacky.html', nav=profile_nav, title="Jacky", url=os.getenv("URL"))

# for william page
@app.route('/william')
def william():
    return render_template('william.html', nav=profile_nav, title="William", url=os.getenv("URL"))
"""





"""
# for work experience/education page
@app.route('/work_edu/<name>')
def work_edu(name):
    profile_title = name.capitalize()
    job = {
        "amber": ["Black Stallion Winery"],
        #"jacky": ["Wendy's"],
        #"william": ["U.S. Census Bureau"]
    }
    # key: name
    # value: 2d list with inner generating new lines
    job_description = {
        "amber": [["July 2019 - June 2020"]],
        "jacky": [["October 2019 - March 2020"]],
        "william": [["August 2020 - November 2020"]]
    }
    education = {
        "amber": ["University of Pennsylvania", "University of California, Davis"],
        "jacky": ["University of Kansas", "Northwest High School"],
        "william": ["University of Chicago", "Stuyvesant High School"]
    }
    # key: name
    # value: 2d list with inner generating new lines
    edu_description = {
        "amber": [["M.S Computer and Information Technology","Aug 2021 - May 2023"], ["Viticulture and Enology","Sep 2015 - Jun 2018"]],
        "jacky": [["B.S. Computer Science","Aug 2020 - May 2024"], ["High School", "Aug 2016 - May 2020"]],
        "william": [["B.S. Computer Science, Minor in Philosophy", "Sept 2020 - June 2024"], ["High School", "Sept 2016 - June 2020"]]
    }
    profile_edu = education[name]
    profile_edu_desc = edu_description[name]
    profile_job = job[name]
    profile_job_desc = job_description[name]
    return render_template("work_edu.html", nav=profile_nav, job=profile_job, job_description=profile_job_desc, education=profile_edu, 
            edu_description=profile_edu_desc, title=profile_title, url=os.getenv("URL"))

# for work experience/education page
@app.route('/hobbies/<name>')
def hobbies(name):
    profile_title = name.capitalize()
    hobbies = {
        "amber": ["Travelling, Photography, Wine, Baking"],
        "jacky": ["Basketball, Gaming, Driving, Deep discussions"],
        "william": ["dance, volleyball, gaming, tv series"]
    }
    profile_hobby = hobbies[name]
    photos = {
        "amber": "amber_hobby.jpg",
        "jacky": "jacky_hobby.jpg",
        "william": "william_hobby.jpg"
    }
    return render_template("hobbies.html", nav=profile_nav, hobbies=profile_hobby, title=profile_title, photo=photos[name], url=os.getenv("URL"))
"""
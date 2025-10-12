from flask import Flask,  render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('static/data/projects.json') as project:
        projects = json.load(project)

    return render_template('index.html', projects=projects)

@app.route('/about_me')
def about_me():
    with open('static/data/experience.json') as project:
        experience_projects = json.load(project)

    with open('static/data/skills.json') as skills_project:
        skills = json.load(skills_project)

    left_column = skills[::2]
    right_column = skills[1::2]
    return render_template("about_me.html", experience_projects=experience_projects, left_column=left_column, right_column=right_column)

@app.route("/projects")
def projects():
    with open('static/data/projects.json') as project:
        projects = json.load(project)
    
    return render_template("projects.html", projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
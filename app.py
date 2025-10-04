from flask import Flask,  render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('static/data/projects.json') as project:
        projects = json.load(project)

    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
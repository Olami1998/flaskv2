from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Lagos, Nigeria',
        'salary': '$10,000,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Lagos, Nigeria',
        'salary': '$15,000,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'ibadan, Nigeria',
        'salary': '$10,000,000'
    },
]

@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name='Lekan')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
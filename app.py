from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York, USA', 
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'New York, USA', 
    'salary': '$150,000'
  },
  {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'San Francisco, USA', 
    'salary': '$200,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)

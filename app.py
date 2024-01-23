from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('index.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=["POST"])
def apply_to_job(id):
  data = request.form
  name = data.get("name", "")
  add_application_to_db(id, data) # store in DB
  return redirect(url_for('application_submitted', id=id, name=name))

@app.route("/job/<id>/application_submitted")
def application_submitted(id):
  job = load_job_from_db(id)
  name = request.args.get("name", "")
  return render_template('application_submitted.html', job=job, name=name)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)

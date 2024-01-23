from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = [row._asdict() for row in result.all()]
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO applications (job_id, name, email, linkedin, education, experience, resume) VALUES (:job_id, :name, :email, :linkedin, :education, :experience, :resume)"
    )
    conn.execute(
        query, {
            "job_id": int(job_id),
            "name": data['name'],
            "email": data['email'],
            "linkedin": data['linkedin'],
            "education": data['education'],
            "experience": data['experience'],
            "resume": data['resume']
        })

import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://atqx5of1i5oefim6ewmd:pscale_pw_4fmq385DvwsgDGc6fKuyCUHRIQl7GhsHiCYxLmtIUfW@aws.connect.psdb.cloud/careers?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem",
    }
  }
)

with engine.connect() as conn: 
  result = conn.execute(text("select * from jobs"))
  result_dicts = [dict(row) for row in result.all()]

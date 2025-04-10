from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine(os.getenv('DATABASE_URL'))
    engine.connect()
    return engine

psql -U postgres -c "DO \$\$ BEGIN 
    CREATE USER my_user WITH PASSWORD 'my_password'; 
    CREATE DATABASE my_database OWNER my_user; 
END \$\$;"

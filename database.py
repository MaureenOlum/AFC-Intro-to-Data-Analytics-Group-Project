import pandas as pd
import sqlite3

wikipedia = pd.read_excel("wikipedia_dataset_flat.xlsx", sheet_name='Sheet1', header=0, index_col=0)


db_conn = sqlite3.connect("wikipedia.db")
c = db_conn.cursor()

c.execute(
    """
    CREATE TABLE wikipedia (
        'date' TEXT,
        'page' TEXT,
        'visits' INTEGER
        );
    """
) 

wikipedia.to_sql('wikipedia', db_conn, if_exists='append', index=False)

pd.read_sql("SELECT * FROM wikipedia LIMIT 10", db_conn)

db_conn.close()
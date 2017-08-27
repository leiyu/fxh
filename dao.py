import json
import sqlite3


db_file = r'fxh.db'


def CountByMediaType():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT mediaType, count(ID) as num FROM articles group by mediaType')
    rs = c.fetchall()
    conn.close()
    return(json.dumps(rs))
    
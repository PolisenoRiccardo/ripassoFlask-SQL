from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/', methods=['GET']) 
def table():
    
    import pyodbc
    import pandas as pd

    server = '5.172.64.20'
    database = 'zhao.filippo'
    username = 'zhao.filippo'
    password = 'xxx123##'
    driver= '{SQL Server}' # il driver ODBC deve essere installato sulla macchina in cui è in esecuzione l'interprete Python

              
    connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(connectionString) 

    sql_query = """
    SELECT * FROM Poliseno.Videogioco
    """
    
    df = pd.read_sql(sql_query, conn)
    return render_template('table.html', tabella = df.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True) 
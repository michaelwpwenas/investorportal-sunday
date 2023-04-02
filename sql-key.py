from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'investor_portal'

mysql = MySQL(app)

with app.app_context():
    cur = mysql.connection.cursor()
    
    # Define primary key for user table
    cur.execute("ALTER TABLE user ADD PRIMARY KEY (id)")
    
    # Define primary key for migration table
    cur.execute("ALTER TABLE migration ADD PRIMARY KEY (id)")
    
    # Define primary key for reset table
    cur.execute("ALTER TABLE reset ADD PRIMARY KEY (email)")
    
    # Define primary key and foreign keys for organization table
    cur.execute("ALTER TABLE organization ADD PRIMARY KEY (org_id), ADD FOREIGN KEY (constant_id) REFERENCES constant (constant_id), ADD FOREIGN KEY (company_id) REFERENCES company (company_id), ADD FOREIGN KEY (calculation_id) REFERENCES calculation (calculation_id)")
    
    # Define primary key for constant table
    cur.execute("ALTER TABLE constant ADD PRIMARY KEY (constant_id)")
    
    # Define primary key for company table
    cur.execute("ALTER TABLE company ADD PRIMARY KEY (company_id)")
    
    # Define primary key for calculation table
    cur.execute("ALTER TABLE calculation ADD PRIMARY KEY (calculation_id)")
    
    # Commit changes to the database
    mysql.connection.commit()


from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL database - change it to your username and your password
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'investor-portal'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Create user table
cur = mysql.connection.cursor()
cur.execute('''CREATE TABLE user (
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                password VARCHAR(255) NOT NULL,
                is_admin TINYINT(1) NOT NULL DEFAULT 0,
                PRIMARY KEY (id)
            )''')
mysql.connection.commit()
cur.close()

# Create migration table
cur = mysql.connection.cursor()
cur.execute('''CREATE TABLE migration (
                id INT NOT NULL AUTO_INCREMENT,
                migration VARCHAR(100) NOT NULL,
                batch INT NOT NULL,
                PRIMARY KEY (id)
            )''')
mysql.connection.commit()
cur.close()

# Create reset table
cur = mysql.connection.cursor()
cur.execute('''CREATE TABLE reset (
                email VARCHAR(100) NOT NULL,
                token VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (email)
            )''')
mysql.connection.commit()
cur.close()

# Create organization table
cur = mysql.connection.cursor()
cur.execute('''CREATE TABLE organization (
                id INT NOT NULL AUTO_INCREMENT,
                constant_id INT NOT NULL,
                company_id INT NOT NULL,
                calculation_id INT NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (constant_id) REFERENCES constant(id),
                FOREIGN KEY (company_id) REFERENCES company(id),
                FOREIGN KEY (calculation_id) REFERENCES calculation(id)
            )''')
mysql.connection.commit()
cur.close()

# Create constant table
cur = mysql.connection.cursor()
cur.execute('''CREATE TABLE constant (
                id INT NOT NULL AUTO_INCREMENT,
                total_capital_raised INT,
                num_investment_rounds INT,
                current_valuation INT,
                deal_type VARCHAR(100),
                invested_capital INT,
                shareholding INT,
                PRIMARY KEY (id)
            )''')
mysql.connection.commit()
cur.close()

# Create company table
cur = mysql.connection.cursor()
cur.execute('''CREATE TABLE company (
                id INT NOT NULL AUTO_INCREMENT,
                monthly_revenue INT,
                cac INT,
                new_customers INT,
                gross_burn INT,
                gross_profit INT,
                ebitda INT,
                impact_metric_1 INT,
                impact_metric_2 INT,
                web_traffic INT,
                som_usd INT,
                PRIMARY KEY (id)
            )''')
mysql.connection.commit()
cur.close()

# Create calculation table
cur = mysql.connection.cursor()
cur.execute('''CREATE TABLE calculation (
                id INT NOT NULL AUTO_INCREMENT,
                mom_growth INT,
                gross_margin INT,
                ebitda_margin INT,
                som_score INT,
                performance_index_monthly INT,
                performance_index_since_investment INT,
                impact_per_dollar_invested INT,
                PRIMARY KEY (id)
            )''')
mysql.connection.commit()
cur.close()

# Close database connection
mysql.connection.close()

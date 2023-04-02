import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="your-username",
  password="your-password",
  database="investor-portal"
)

# Get a cursor object
cursor = db.cursor()

# Define a function to calculate the values for the calculation table
def calculate(company_id):
    # Get the relevant data from the constant and company tables
    cursor.execute("SELECT * FROM constant WHERE company_id = %s", (company_id,))
    constant_data = cursor.fetchone()
    cursor.execute("SELECT * FROM company WHERE id = %s", (company_id,))
    company_data = cursor.fetchone()

    # Perform calculations
    mom_growth = 0.0  # replace with actual calculation
    gross_margin = 0.0  # replace with actual calculation
    ebitda_margin = 0.0  # replace with actual calculation
    som_score = 0.0  # replace with actual calculation
    perf_index_monthly = 0.0  # replace with actual calculation
    perf_index_since_investment = 0.0  # replace with actual calculation
    impact_per_dollar_invested = 0.0  # replace with actual calculation

    # Insert the calculated values into the calculation table
    sql = "INSERT INTO calculation (company_id, mom_growth, gross_margin, ebitda_margin, som_score, perf_index_monthly, perf_index_since_investment, impact_per_dollar_invested) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (company_id, mom_growth, gross_margin, ebitda_margin, som_score, perf_index_monthly, perf_index_since_investment, impact_per_dollar_invested)
    cursor.execute(sql, values)
    db.commit()

# Call the calculate function for all companies in the company table
cursor.execute("SELECT id FROM company")
company_ids = cursor.fetchall()
for company_id in company_ids:
    calculate(company_id[0])

# Close the database connection
db.close()
# Repository Title
Investor portal backend that I made on Sunday, April 2 2023.

# Python
1. Open a terminal or command prompt and navigate to the project directory.
2. Enter the following command to create a new virtual environment:
``python3 -m venv venv``
3. Activate the virtual environment:
``source venv/bin/activate``
4. ``pip install Flask Flask-MySQLdb``
5. The script in `database.py` was made to create the tables in the MySQL database using `Flask-MySQLdb`. Note that you need to replace the `your_username` and `your_password` placeholders with your actual MySQL database credentials.
6. The script in `sql-key.py` was made to define primary key and foreign key relationships for each table using Python script. This code snippet assumes that the investor_portal database has already been created with the necessary tables. It uses the ALTER TABLE command to define primary keys and foreign keys for each table.
7. `login.py` was made to implement regular login and Google authentication. In this script, the `is_admin` column is a Boolean field that defaults to False (i.e., regular user). If a user is an admin, the value of this field is set to True.
8. `calculation.py` script assumes that you have already defined the schema for the calculation table in your MySQL database, and that you have established a connection to the database using the mysql.connector library. The actual calculations performed in the calculate function will depend on the specific metrics and KPIs that you want to calculate for your investor portal.

# Javascript
1. Install ReactJS using `npm install -g create-react app` and `npm install axios`.
2. In `axios.js`, we define a class called DataService that has methods for making HTTP requests to the API. The API_URL constant is set to the URL of your backend API. The getAll, get, create, update, and delete methods correspond to the CRUD operations and take two arguments: tableName and data. tableName is the name of the database table you want to interact with, and data is the data you want to send in the request.
3. To use `axios.js` service in your React components, simply import it and call the appropriate method using the script within `react-script.js`. In this example, we import the DataService class and use the getAll method to fetch data from the my_table table. We store the returned data in the data state variable and render it in the component.
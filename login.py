from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import UserMixin

# Create the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Set up the Google OAuth blueprint
google_blueprint = make_google_blueprint(
    client_id="google_client_id",
    client_secret="google_client_secret",
    scope=["email", "profile"],
    redirect_url=url_for("google_authorized", _external=True)
)
app.register_blueprint(google_blueprint, url_prefix="/login")

# Create the user class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

    @classmethod
    def get(cls, id):
        return cls(id)

# Define whether user is admin or regular
class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = password
        self.is_admin = is_admin

# Define the user loader function
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Define the login route
@app.route('/login')
def login():
    return render_template('login.html')

# Define the regular login route
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    # Check if the email and password are valid
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Invalid email or password')
        return redirect(url_for('login'))

    # Log the user in
    login_user(user)
    return redirect(url_for('dashboard'))

# Define the Google login route
@app.route('/login/google')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))

    resp = google.get('/oauth2/v2/userinfo')
    if resp.ok:
        email = resp.json()['email']

        # Check if the user already exists in the database
        user = User.query.filter_by(email=email).first()
        if not user:
            # Create a new user
            user = User(email=email)
            db.session.add(user)
            db.session.commit()

        # Log the user in
        login_user(user)
        return redirect(url_for('dashboard'))

    flash('Failed to fetch user info.')
    return redirect(url_for('login'))

# Define the logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

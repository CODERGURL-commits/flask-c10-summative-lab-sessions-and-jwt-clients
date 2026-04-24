# Flask C10 Summative Lab: Sessions & JWT Clients
## Overview
This summative lab explores the evolution of authentication in Flask applications. 
It provides a side-by-side implementation of Stateful (Session-based) and Stateless (JWT-based) authentication. 
By the end of this project, you will understand how to secure endpoints, manage token lifecycles, and handle client-side authentication patterns for modern web apps.

# Features
``Dual Auth Strategy``: Support for both flask-session and PyJWT for comparative learning.

``Secure Password Hashing``: Implementation of Bcrypt for safe user credential storage.

``Stateless JWT Workflow``: Token generation, header-based transmission, and decorator-driven validation.

``Session Management``: Server-side session tracking and cookie-based client persistence.

``Protected Routes``: Custom decorators (@token_required or @login_required) to restrict access to sensitive data.

# Technologies
``Backend``: Flask 2.x

``Security``: PyJWT, Flask-Bcrypt

``Environment``: Python 3.8+

Storage: Flask-SQLAlchemy (for user persistence)

#  Installation & Setup
1. Environment Setup
Clone the repository and set up your virtual environment:

``Bash
git clone <your-repo-link>
cd flask-c10-summative``

python -m venv venv

# Windows:
``.\venv\Scripts\activate``
# Mac/Linux:
``source venv/bin/activate``

# 2. Install Dependencies
``Bash
pip install flask pyjwt flask-bcrypt flask-sqlalchemy flask-cors``

# 3. Configuration
Create a .env file in the root directory and add your secret key:
``FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_super_secret_random_string
``
## API Design & Authentication Patterns
Session-Based (Traditional)
Flow: Client sends credentials → Server creates session → Server sends Set-Cookie header.

Pros: Easy to revoke, simple for browser-only apps.

## JWT-Based (Modern)

Flow: Client sends credentials → Server returns a signed Token → Client sends Token in Authorization: Bearer <token> header.

Pros: Scalable, mobile-friendly, works across different domains.

# Usage
Running the server:
 ``Bash
flask run``
Example: Protecting a Route with JWT
Python
```
from functools import wraps
from flask import request, jsonify
import jwt
`
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorated
```

## Project Structure

├── app.py              # Main entry point and routes
├── models.py           # User models and DB schema
├── auth_utils.py       # JWT generation and decorator logic
├── .env                # Environment variables (do not commit!)
├── requirements.txt    # List of dependencies
└── tests/              # Unit tests for auth flows
## License
This project is licensed under the MIT License.

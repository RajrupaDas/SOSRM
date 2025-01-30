# SOSRM

This is the backend for the **SOSRM** project, built using **Django**. It provides API endpoints for handling user authentication, SOS alerts, secure access, and buddy matching. The backend is designed to be used with an HTML-based front end.

## Features

- **User Authentication**: Register, login, and email verification.
- **SOS Feature**: Triggers an alert and sends an SMS when activated.
- **SecureWay**: Displays different images based on user role (students, staff, security).
- **Buddy Matching**: Matches users based on a 5-digit location code.
- **Image Uploads**: Stores images for different features.

## Project Structure

```
SOSRM/
│
├── APP/                          # Main Django app
│   ├── migrations/               # Database migrations
│   ├── __init__.py               # App initialization
│   ├── admin.py                  # Admin panel setup
│   ├── apps.py                   # App configuration
│   ├── models.py                 # Database models
│   ├── serializers.py            # API serializers
│   ├── tests.py                  # Test cases (optional)
│   ├── urls.py                   # API routes
│   └── views.py                  # API views
│
├── SOSRM/                        # Django project folder
│   ├── __init__.py               # Project initialization
│   ├── asgi.py                   # ASGI configuration
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main project URLs
│   ├── wsgi.py                   # WSGI configuration
│
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
├── db.sqlite3                    # SQLite database (can be changed)
└── media/                         # Uploaded images
    └── images/
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/SOSRM.git
cd SOSRM
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root and add the following:
```env
SECRET_KEY=your_secret_key
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_password
```

### 5. Apply Migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python3 manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python3 manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Email Verification Setup
The backend sends a verification email when a user registers. To test email sending in development, use the console backend by adding this to `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

For production, configure SMTP settings.

## API Endpoints

| Endpoint                 | Method | Description |
|--------------------------|--------|-------------|
| `/api/register/`         | POST   | Registers a new user and sends a verification email |
| `/api/verify-email/`     | GET    | Verifies user email via token |
| `/api/login/`           | POST   | Authenticates a user |
| `/api/sos/`             | POST   | Triggers an SOS alert |
| `/api/secureway/`       | GET    | Fetches role-based images |
| `/api/buddy/`           | GET    | Finds users with matching location codes |

## Frontend Integration
The frontend (HTML, CSS, JavaScript) can call these API endpoints using `fetch()`.

Example login request:
```javascript
fetch('http://127.0.0.1:8000/api/login/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        email: 'user@example.com',
        password: 'securepassword'
    })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Testing
You can test API requests using **Postman** or **cURL**.

Example cURL request for registration:
```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{"email": "test@example.com", "password": "password123"}'
```

## Deployment
To deploy the project, use **Gunicorn** with **NGINX** or **Django’s built-in WSGI server**.

Example:
```bash
pip install gunicorn
python3 manage.py collectstatic
```

## Contributing
Feel free to fork the repo and submit pull requests.

## License
This project is licensed under the MIT License.


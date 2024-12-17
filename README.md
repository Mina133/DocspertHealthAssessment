# Documentation for Docspert Health

This document outlines the architecture, features, and setup instructions for the "Docspert Health" web application, developed using the Django framework.

---

## **Project Overview**
Docspert Health is a Django-based web application designed to manage account transfers and upload files. The application includes features for handling CSV file uploads, account management, and data visualization through a user-friendly interface.

---

## **Project Structure**

```
DocspertHealth/
│
├── AccountTransfer/                     # Django Application: AccountTransfer
│   ├── __pycache__/                     # Python bytecode cache
│   ├── migrations/                      # Database migration files
│   │   └── __init__.py                  # Marks migrations as a Python package
│   ├── __init__.py                      # Marks AccountTransfer as a Python package
│   ├── admin.py                         # Admin site configuration
│   ├── apps.py                          # Application configuration class
│   ├── forms.py                         # Custom forms
│   ├── models.py                        # Database models
│   ├── tests.py                         # Unit tests
│   ├── urls.py                          # Application-level URL routing
│   └── views.py                         # Views/Controllers for business logic
│
├── docspertHealth/                      # Project Configuration (Main Django Project)
│   ├── __pycache__/                     # Python bytecode cache
│   ├── __init__.py                      # Marks docspertHealth as a Python package
│   ├── asgi.py                          # ASGI configuration for asynchronous support
│   ├── settings.py                      # Global settings (e.g., INSTALLED_APPS, middleware)
│   ├── urls.py                          # Project-level URL configurations
│   └── wsgi.py                          # WSGI configuration for serving the app
│
├── templates/                           # HTML Templates (Shared by the project)
│   ├── accounts.html                    # Template for account management
│   ├── base.html                        # Base template (common structure)
│   ├── home.html                        # Home page template
│   ├── success.html                     # Success message/page template
│   ├── transfer.html                    # Transfer form page template
│   └── upload.html                      # Upload file/form template
│
├── .gitignore                           # Git ignore file for ignored assets
├── db.sqlite3                           # SQLite3 database for development
└── manage.py                            # Django's management script

## **Features**

### 1. File Upload
- Users can upload CSV files for processing.
- Validation is implemented to ensure correct file formats.

### 2. Account Management
- Users can manage account transfers through an intuitive form.
- Includes validation to ensure data integrity.

### 3. Modular Design
- Separated into apps for scalability and maintainability.
- Templates follow a DRY (Don't Repeat Yourself) approach with a base structure.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.10 or later
- Django 4.x
- SQLite3 (default database)

### **2. Installation Steps**

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd docspertHealth
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

---

## **Usage Instructions**

### **1. File Upload**
- Navigate to the upload page.
- Select a valid CSV file and click "Upload."
- If successful, a success message will be displayed.

### **2. Account Transfers**
- Go to the account transfer form.
- Fill in the required details and submit the form.

---

## **Testing**
Run the unit tests to ensure the application behaves as expected:
```bash
python manage.py test
```

---

## **Future Improvements**
- Add Docker support for containerized deployment.
- Implement role-based authentication.
- Extend the database model to support additional account-related features.

---

## **Contributing**
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your fork.
4. Submit a pull request for review.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.


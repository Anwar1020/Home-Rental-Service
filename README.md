# Home_Rental_Service

Welcome to our Home Rental Website! This platform allows Home owners to list their vacant homes available for rent, while individuals seeking a home can conveniently search for properties based on location.

## Features

### For Property Owners:
- **Property Listing**: Owners can post information about their vacant homes available for rent.
- **Property Details**: Provide comprehensive details about the property, including descriptions, images, and contact information.
- **Management**: Manage property listings, update information, or remove listings as needed.

### For Renters:
- **Search by Location**: Users can easily search for available properties based on location preferences.
- **Property Details**: View detailed information about each property, including images, descriptions, and contact information for inquiries.

## Technologies Used

- **Django**: Python-based web framework used for backend development.
- **HTML/CSS**: Frontend development for creating user interfaces and styles.
- **JavaScript**: Enhance user interactivity and functionalities.
- **MySQL**: Relational database management system for storing property and user data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Anwar1020/Home-Rental-Service.git
    ```

2. Browse to folder which contains manage.py file:

    ```bash
    cd Home_Rental_Service
    ```

3. Set up MySQL database:
    - Create a MySQL database and configure database settings in `settings.py`.
    - 'Mysql Configuration' described bellow this section.

4. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your web browser at `http://localhost:8000`.


...

## MySQL Configuration

This project uses MySQL as the database management system. Follow these steps to configure MySQL for the project:

1. **Install MySQL**: If you haven't already installed MySQL, download and install it from the [official MySQL website](https://dev.mysql.com/downloads/).

2. **Create Database**: Log in to MySQL and create a database for the project. You can use the command line or tools like phpMyAdmin. Replace `database_name` with your preferred database name:

    ```sql
    CREATE DATABASE database_name;
    ```

3. **Database Configuration in Django**:
    - Open `settings.py` file in your Django project.
    - Locate the `DATABASES` configuration section.
    - Update the `DATABASES` dictionary with your MySQL database settings:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'yourdatabase',
            'USER': 'yourmysqlusername',
            'PASSWORD': 'yourmysqlpassword',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

    Replace `'yourdatabase'`, `'yourmysqlusername'`, and `'yourmysqlpassword'` with your MySQL database name, username, and password respectively.





## Usage

1. Property Owners can create accounts and post details about their vacant homes for rent.
2. Renters can search for properties based on location preferences, view property details, and contact owners for inquiries.


## Acknowledgments

- Special thanks to the Django and open-source community for their valuable contributions.



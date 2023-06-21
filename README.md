## Prerequisites

- Python 3.x
- Django (version 4.x)

## Installation
#### Step 1(Set .env in proj folder)
```
cd NEXTSAVY/proj
nano .env
```
##### Note: Use .env variables(content) from .env_example file
#### Step 2(Make virtual environment)
```
cd NEXTSAVY
python3 -m venv env
```
#### Step 3(Activate virtual environment)
##### For Windows
```
cd NEXTSAVY
env\Scripts\activate
```
##### For Linux
```
cd NEXTSAVY
. env/bin/activate
```
#### Step 4(Install requirements.txt)
```
pip install -r requirements.txt
```
#### Step 5(Apply migrations)
```
python manage.py migrate
```
#### Step 6(Run server)
#
```
python manage.py runserver
```
## Project Structure

The project follows a standard Django project structure:

  -your_django_project/ - The project's root directory.
      -your_django_project/ - The main Django project directory.
        -settings.py - Django settings file.
        -urls.py - Main URL configuration file.
      -your_app/ - An example Django app included in the project.
        -models.py - App's models.
        -views.py - App's views.
        -urls.py - App's URL configuration.
      -manage.py - Django's command-line utility for administrative tasks.

## Approach

- This project follows a [MVC (Model-View-Controller)] architectural pattern to separate concerns and improve maintainability.
- It utilizes Django's built-in features such as models, views, and templates to implement different components of the application.
- The project follows best practices for code organization, readability, and maintainability.

## Data Modeling Decisions

- The project uses Django's [ORM (Object-Relational Mapping)]to define and interact with the database models.
- The database models are designed to represent the application's data entities and their relationships.
- Careful consideration has been given to the design of the database schema to ensure efficient storage and retrieval of data.
- The data modeling decisions are based on the specific requirements of the application and its expected usage patterns.


## Limitations

- This project is for demonstration purposes only and may not cover all real-world scenarios.
- It may not include advanced features or complex functionality.

## Risks

- The project may contain bugs or errors for different use-cases.
- Ensure proper testing and validation before if deploying to production.

## Scale

- This project is currently designed for small-size files and may not handle large data files.
- Performance optimizations and scalability improvements can be considered.

## Public API

- http://localhost:8000/view/<file_id> (Retrieve single file)

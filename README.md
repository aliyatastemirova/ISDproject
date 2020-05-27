# ISDproject

## Setup

### Installation
#### Requirements
- Python 3.8.*
- Pip
- Postgresql database
- All the required libraries installed (Installation described below)

## Documentation
### Environment setup
Setting up the environment with requirements.txt:
- run "pip install -r requirements.txt" or "pip install --user --requirement requirements.txt"
- If you want to update requirements file, add necessary packages and run "pip freeze > requirements.txt"

Setting up environment variables:
- check .env.example file in CoursePlatform/Courseplatform folder to see what you need to have in your .env file

Run usual django commands (manage.py file is in main CoursePlatform directory):
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

### About the website
This is an online course platform that allows users to publish/watch courses depending on their access.

Includes two django apps: 
- accounts app includes everything connected with users, user authentication, profiles and general pages (homepage),
login, logout views and templates, etc.
- courses app includes everything connected with courses: courses page, enrolling functionality, videos, course models, etc

And design/files directories:
- static directory: includes css, js, fonts, etc. necessary for templates
- templates in the main directory includes base design (scripts, header, footer)
- templates in accounts app includes all html templates includes all necessary designs for account-related pages
- templates in course app includes all html templates includes designs for course-related pages
- media directory is where uploaded files are saved (course thumbnails, profile pictures)

There are two types of users, apart from the superuser:
- Students: can create an account, browse courses, enroll into courses, watch videos, edit their profile details
- Partners: can create an account, do everything that a student can do, also have a limited access to the admin panel to create courses
Permissions for partners should be added manually through the admin panel, as we do not want to grant them automatically.
Each partner should be manually reviewed before granting them access to creating content.




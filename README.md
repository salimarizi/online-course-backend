# Online Course Backend with Django

Online course is a web-based platform that provides a Proof of Concept (POC) for courses and also features a simple integrated development environment (IDE). The platform is designed to cater to individuals who are seeking to learn new skills, improve their expertise, or enhance their knowledge. The platform provides an opportunity to learn from experienced instructors through online courses and engage with other learners in the community.

This project created with Django (including Django Rest Framework). The default database for this project is PostgreSQL, however it can be change to another database management system by simply change `settings.py` in folder `online_course_backend`

## Database Design
Below image is the main tables related to this (not including django default tables)
![database design](https://github.com/salimarizi/online-course-backend/blob/main/static/database_design.png?raw=true)

## How to run this project

In order to run this project, these is the step by step after cloning project:

### `pip install -r requirements.txt`

Install django and necessary libraries for this project.

### `python manage.py runserver`

Runs the app .\
Open [http://localhost:8000](http://localhost:8000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

## Available routes
### Web Routes
### `/admin`
It will guide to default admin dashboard provided by Django.

### API Routes
### `/api/courses` (GET)
API Endpoint to get all courses from database. Can also search specific course by `adding parameter 'q'` as query to search.

### `/api/courses/:course_id` (GET)
API Endpoint to get selected course based on id.

### `/api/exercise` (POST)
API Endpoint to store 'written code' and compile it to return the output (either the success output or error output)

More info about Project APIs can be view by visiting this [Postman Documentation](https://documenter.getpostman.com/view/2470070/2s93CHtuaN)
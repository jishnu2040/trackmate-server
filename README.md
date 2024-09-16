Task Manager Application Documentation
Overview
The Task Manager Application is designed to help users manage tasks effectively. Users can create, view, edit, and delete tasks, with functionalities for filtering and searching. The backend is built using Django REST Framework (DRF), and the frontend uses React to interact with the API.

Features
Task Management: Create, view, update, and delete tasks.
Search and Filter: Search tasks and filter by completion status.
Pagination: Handle large sets of tasks with pagination.
JWT Authentication: Secure API endpoints with JSON Web Tokens (JWT).
Responsive UI: Ensure a user-friendly interface across all devices.


Installation
Backend (Django)
Clone the Repository:


git clone https://github.com/jishnu2040/trackmate-server.git
cd trackmate-server

Create and Activate a Virtual Environment:

source env/bin/activate 

Install Dependencies:
pip install -r requirements.txt


Set Up Environment Variables: Create a .env
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/task_manager

Run the Server:
python manage.py runserver


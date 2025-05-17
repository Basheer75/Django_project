📘 Student Management System (Django)
This is a web-based Student Management System built with Django. It provides a platform to manage student records, parent details, and notifications efficiently. The system is designed for school administrators and staff to streamline student data entry, updates, and tracking.

🔑 Key Features
🔐 User Authentication – Login, registration, password reset

👨‍🎓 Student Module – Add, view, edit, delete student details

👨‍👩‍👧 Parent Module – Store and link parent information to students

🖼️ Student Image Upload – Upload and manage student profile images

🛎️ Notification System – Send and mark notifications (coming soon)

📄 Responsive UI – Clean interface using HTML templates

🧭 Slug URLs – SEO-friendly unique URLs for each student

🛠️ Tech Stack
Backend: Django 5

Frontend: HTML5, Bootstrap

Database: SQLite3

Language: Python 3.13

🚀 How to Run Locally

git clone https://github.com/YOUR_USERNAME/student-management-system.git
cd student-management-system
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

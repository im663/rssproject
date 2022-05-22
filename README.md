RSS Project
-----------
Personal RSS aggregator written in Django.

Requirements
------------
- Python 3
- Django

How to get it running
---------------------
- Clone the project:
git clone https://git.im663.com/rssproject

- Install the requirements with: pip install -r requirements.txt
- Enter the root of the directory and create a .env file which will hold the following:
SECRET_KEY = 'GENERATE A SECRET KEY AND PASTE IT INTO HERE'
- Inside the root directory of the project run:
python3 manage.py makemigrations base
python3 manage.py migrate
python3 manage.py createsuperuser # This is the moderator account

Go to:
http://localhost:8000 in your browser and click Login, you can then begin submitting new runs!

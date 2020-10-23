# BloodLines
Simple bloodbank app made with the help of Python's Django Web Framework and integrated with PostgreSQL.

A database application such as this can help bridge the gap between hospitals, blood banks and ordinary citizens by not only improving the connectivity between the three, but also greatly improving the efficiency in the urgent ‘demand and supply’ mechanisms which currently bog down the medical industry. Such an application, if structured and flawlessly executed on a large scale, has the potential to sustain a successful business model with respect to hospitals and blood banks which would be its primary sources of revenue.

# Install the Dependencies:
 - `pip install requirements.txt` Quick install everything
 OR
 - `pip install pillow` The Python Imaging Library adds image processing capabilities to your Python interpreter. [more](https://github.com/python-pillow/Pillow)
 - `pip install bcrypt` Good password hashing for your software and your servers . [more](https://pypi.org/project/bcrypt/)
 - `pip install argon2-cffi` Argon2 is a password-hashing function that summarizes the state of the art in the design of memory-hard functions and can be used to hash passwords for credential storage, key derivation, or other applications. [more](https://github.com/p-h-c/phc-winner-argon2)
 - `pip install psycopg2` Psycopg is the most popular PostgreSQL database adapter for the Python programming language. [more](https://github.com/psycopg/psycopg2)
 - `pip install django-crispy-forms`django-crispy-forms provides you with a `|crispy` filter and `{% crispy %}` tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way..[more](https://github.com/django-crispy-forms/django-crispy-forms)

# Start The App?
 - Download the repository and navigate into it.
 - Activate your **virtual environment** containing the Django web framework.
 - Install the above listed dependencies and run `pip freeze` to check all installed dependencies in your environment.
 - Run `python manage.py makemigrations` and `python manage.py migrate` to propagate changes you make in your models into your database schema.
 - Run command: `python manage.py runserver`
 - If a new browser tab does not open with the homepage then, copy and paste the link shown on your terminal onto a browser.



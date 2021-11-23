# Lab 4

## Startup steps

1. Make sure you are in `se_labs/lab4` directory

1. Create your virtual environment:

        mkdir venv
        cd venv
        python -m venv django
        source django/bin/activate #or source django/Scripts/activate in Windows

1. Go back to `se_labs/lab4` and start your app with:

        cd mysite
        pip install -r requirements.txt
        python manage.py runserver

1. If you encounter errors with database or migrations, fix them like we did in the 
previous lab. Hint: runserver errors will tell you what to do.

1. Add `lab4/venv/` to `.gitignore` file for easier commiting

## Work

We are continuing the django tutorial part 3 on [django docs](https://docs.djangoproject.com/en/3.1/intro/tutorial03/)
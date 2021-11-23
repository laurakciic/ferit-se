# Lab 5

## History of commands in Git Bash


#### Creating virtual env named `django`
- Virutal environment bypasses system paths (zaobilazi sistemske putanje)
```
python -m venv django
```

#### Activating virutal env
```
source django/Scripts/activate
```

#### Installing django framework
```
pip install django
```

#### Checking for correct installation
```
django-admin --version
```

#### Creating inital project
```
django-admin startproject myimgur
```
####
```
ls
```
####
```
cd myimgur/
```
####
```
ls
```

####  Running manage.py file responsible for running server
- winpty is only for windows (allows I/O in terminal)
```
winpty python manage.py runserver
```

####
```
cd ..
```
####
```
cd ..
```
####
```
git status
```
####
```
git add lv5
```
####
```
git status
```
####
```
git commit -m "add myimgur inital project to lv5"
```
####
```
git add .gitignore
```
####
```
git status
```

#### Merging this commit with previous commit
```
git commit --amend
```

####
```
git status
```

#### List of previously used commands in terminal
```
history
```

#### Clear terminal screen
```
clear
```

#### Prints packet versions 
```
pip freeze
```

#### Entering directory where we want to make `requirements.txt` file
```
cd lv5
```

#### Prints required packages in `requirements.txt`
```
pip freeze > requirements.txt
```

####
```
ls
```

#### Installation of required packages from `requirements.txt` file
```
pip install -r requirements.txt
```
###
# In new terminal 
###

```
cd lv5/
```

#### Activating django venv
```
source django/Scripts/activate
```

####
```
cd myimgur/
```

#### Apply migrations (database changes)
```
python manage.py migrate
```

#### Creating super user (admin)
```
winpty python manage.py createsuperuser
```

#### Add database 
```
git add db.sqlite3
```

#### 
```
python manage.py startapp images
```

#### Commiting changes...
```
...
```

#### 
```
python manage.py makemigrations
```

#### 
```
python manage.py migrate
```

#### 
```
git diff db.sqlite3
```
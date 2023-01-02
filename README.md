# Task-Rabbit
A online courier service where a customer can request from a service from a rabbit (courier) with authentication and payment processing for the services offered by the rabbit

## How to run
- Local Deployment
1. On your local machine, make sure you have Python and SQLite3 installed
2. Download, extract the zipped master file of this project and navigate to root directory of this project
3. On the terminal of your choice, using pip to install pipenv using the command `python -m pip install pipenv`
4. Create a virtual environment with the command `python -m pipenv shell`
5. In your virtual environment, run the command `python -m pip install pipenv`
6. Download the dependencies of the project using the command `pipenv install`
7. Create a admin user using the command `pipenv run python manage.py createsuperuser` and follow the prompts
7. Run the local server to view the project using the command `pipenv run python manage.py migrate && pipenv run python manage.py runserver`

1. CREATE DATABASE flask_test
2. Create .env file
3. Make migrations
	python manage.py db migrate
	python manage.py db upgrade

**Project Structure**

The application has two parts: web-page with input field and submit button for creating an order and telegram-bot. Bot publishes these orders to telegram channel, and sends information about order to user, who is ready to fulfill it.     
The *manage.py* file is the main file, where flask app is run, and bot initializes. Also, bot’s behavior is described here.   
The concept of blueprint is used in application. The blueprint is created in constructor of *app/main* package and is registered in *app* package constructor. Also, there are the date base configuration settings in *app* package constructor.   
The *model.py* file is used to create the models and work with database.   
The *views.py* file contains logic of application. There is a method for getting information about the order from web-site and sending it to bot.  
The *ajax.js* file is used for validating input field for phone number and sending requests to backend and changing *base.html* without reloading page.  
There is *template* folder for html files, and *static* folder for css and js files.   




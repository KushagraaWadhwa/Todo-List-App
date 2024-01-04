Todoastic
Welcome to My Kanban App called “TODOASTIC” which means (Todo+fantastic).
It’s a very interesting application with a very intuitive welcome page.
A very simple yet useful app to keep track of your data anywhere on the go.
First, we have a homepage where you enter your name and log into the website, wherein at
first you are shown a very beautiful welcome message and a link to proceed further into the
website.
Then there lands the main homepage of the website wherein you can add tasks by filling out
the form and the tasks get added in a neatly managed table even showing the time they
were created.
Also, I have provided three buttons alongside every task allowing you to perform Update,
Delete, and mark the task completed if you are done with the task.
Technologies used
• Flask for application code (Flask, SQL Alchemy)
• Jinja2 templates + Bootstrap for HTML generation and styling
• SQLite for data storage
DB Schema Design
4 columns: - SNo (Primary key as it uniquely identifies each tuple in the table), Title of the
task (Cannot be null value), Description (Cannot be null value), Created at (Showing time
and date at which the task was created)
The reason I chose my database table to be this way is because this kind of table provides all
the basic and needful information about the task.
API Design
I have created API’s for Updating tasks, deleting tasks and
Checking the progress of the tasks in this application.
Architecture and Features
The main project folder consists of mainly 2 folders namely, templates, script. In templates
folder I have created 7html files for the website functioning, which consists of a base
html file and using jinja templates I have made other templates using base.html. “static”
folder contains the image brand logo of the website. Addition to that there an app.py file
which operates the main functioning of the app and where all the flask code is written.
Also, there a db file named test.db which stores the data. The yaml files consists of the
configuration of the app.

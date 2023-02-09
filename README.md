<h1>TeamManagementApplication</h1>

<h2>Introduction</h2>
The TeamManagementApplication is a simple project that aims to implement a team-member management application. This application enables the user to view, edit, add, and delete team members. The application provides a simple and user-friendly interface to manage the team members efficiently.

<h2>Features</h2>
<p>Add Member: This page contains a form where the user can add new team members. The form requires the following information to be filled: Name, Email, Phone number, and Role (Admin or General).</p>

<p>Edit Member: This page contains a form where the user can edit the information of existing team members. The form is pre-populated with the current information of the selected member.</p>

<p>Delete Member: The delete option is only available for the members who have a role of "Admin". The delete option is shown on the Edit Member page.</p>

<h2>Requirements</h2>

<p>The following software and tools are required to run this application:</p>

<p>Python 3.x</p>
<p>Django 2.x</p>
<p>Semantic UI</p>
<p>JQuery</p>

<h2>Installation</h2>

<p>1.Clone the repository
  git clone https://github.com/Harika-Yeddula/Team_Management_Application</p>
<p>2.Change the directory
  cd TeamManagementApplication</p>
<p>3.Install the required packages
  pip install -r requirements.txt</p>
<p>4.Run the migrations
  python manage.py migrate</p>
<p>5.Run the development server
  python manage.py runserver</p>
<p>6.Open the application in your browser at http://127.0.0.1:8000/</p>

We can also open the project in pycharm, migrate the models using the following commands
1. makemigrations appname
2. sqlmigrate appname file name added under Migrations folder
3. migrate 
<p>We can see the DB configuration using the admin configuration provided by django i.e models migrated and the data added to them can be viewed on http://127.0.0.1:8000/admin</p>

<h2>Conclusion</h2>
The TeamManagementApplication is a simple and efficient way to manage the team members. The application provides a user-friendly interface to add, edit, and delete members, making it an ideal solution for small to medium-sized teams.



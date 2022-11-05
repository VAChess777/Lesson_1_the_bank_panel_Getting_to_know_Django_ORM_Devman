# The project "Security Control Panel" 

1) The program displays information on the "security panel" about active employee passes.
2) The program displays information about the employee's time in the place of interest to us.
3) The program displays information about employees who are currently in the place of interest to us.

### Software environment and installation:

Python3 should already be installed.

### Program installation:

Download the code: [https://github.com/VAChess777/Lesson_1_the_bank_panel_Getting_to_know_Django_ORM_Devman](https://github.com/VAChess777/Lesson_1_the_bank_panel_Getting_to_know_Django_ORM_Devman), or clone the `git` repository to a local folder:
```
https://github.com/VAChess777/Lesson_1_the_bank_panel_Getting_to_know_Django_ORM_Devman
```

### Installing dependencies:
 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bach
pip install -r requirements.txt
```

### About environment variables:

The program ```main.py``` has an environment variable `os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')`, which is responsible for configuring access to the database. The setup is carried out in the program `settings.py`

### How to run the program:

Run the script ```main.py``` with the command:
```bach
$ python main.py
```
Log in to your browser at [127.0.0.1:8000](http://127.0.0.1:8000), and you will see the information of the 'security console.'

### How the program works:

The program consists of 7 script:

```main.py``` - the main program that runs the script.   
```active_passcards_view.py``` - the program is located in the datacenter folder. The program shows how many active passes are available.                                             
```storage_information_view.py``` - the program is located in the datacenter folder. The program shows information about employees who are in the vault, and how long they are there.                           
```passcard_info_view.py``` - the program is located in the datacenter folder. The program calculates information about how many visits to the repository the employee of interest had, and was this visit suspicious.   
```settings.py``` - the program is located in the project folder. Responsible for setting up access to the employee database.   
```models.py``` - the program is located in the datacenter folder. The program is responsible for data models and their fields
```urls.py``` - the program is located in the project folder. Responsible for setting up links to the 'security console' pages
            
### Features works of the program:

The `active_passcards_view.py` program contains the functions:

* The `active_passcards_view` function - get active employee passes from the database.

The `storage_information_view.py` program contains the functions:

* The `storage_information_view` function - calculates information about how many visits to the repository the employee of interest had, and was this visit suspicious.
* The `get_duration` function - gets the difference between the start of the visit and the time when the employee left the object.
* The `format_duartion` function - formats the information received from the function `get_duration`.

The `passcard_info_view.py` program contains the functions:

* The `passcard_info_view` function - receives information about the visits of each employee. Calculates whether this visit was suspicious.
* The `get_object_or_404` function - checks the correctness of the entered passcard number.
* The `is_visit_long` function - compares the employee's stay time with the time we are interested in visiting the object.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
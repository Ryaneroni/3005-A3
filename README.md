1/1 File -> main.py

Installs:
pip install psycopg2

******If any info differs in your postgres database you must change it in the connReqs Variable***********
(Current Database Setup Below)
host = localhost, dbname (database name) = A3, user = postgres, password = postgres

Operation:
Ensure database has been created and populated before operation
Install pyscopg2 using the command above
Navigate to the folder where you placed my file, and run using Python.

e.g (In folder with the file) 
python main.py

A main menu will be provided, enter one of the available functions with your data (type quit to exit)

Functions:
getAllStudents()
addStudent(first_name, last_name, email, enrollment_date)
updateStudentEmail(student_id, new_email)
deleteStudent(student_id)
quit


Development Data
Created on Windows 11 (stable release as of 2024-03-06)
Python 3.12.2
git version 2.44.0.windows.1

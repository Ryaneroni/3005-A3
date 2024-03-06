import psycopg2

connReqs = "host='localhost' dbname='A3' user='postgres' password='postgres'"

connection = psycopg2.connect(connReqs)

cursor = connection.cursor()

exitFlag = True
while exitFlag == True:
    print("\nFunctions:\ngetAllStudents() - getAllStudents(): Retrieves and displays all records from the students table. ")
    print("addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table. ")
    print("updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id. ")
    print("deleteStudent(student_id): Deletes the record of the student with the specified student_id. \n")
    print("*Type quit to leave*")
    
    userInput = input("Please Enter Input: ")
    if(userInput.lower() == "quit"):
        exitFlag = False
    
    elif(userInput == "getAllStudents()"):
        cursor.execute("SELECT * FROM Students")
        records = cursor.fetchall()
        for record in records:
            print(record)
    
    elif("addStudent(" in userInput and userInput[-1] == ")"):
        tobeAdded = (userInput.split("("))
        details = tobeAdded[1].strip(")")
        stuffs = details.split(",")

        for i in range(0, len(stuffs)):
            stuffs[i] = stuffs[i].replace(" ", "")

        insertStatement = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{}', '{}', '{}', '{}');".format(stuffs[0], stuffs[1], stuffs[2], stuffs[3])
        cursor.execute(insertStatement)
        connection.commit()

    elif("updateStudentEmail(" in userInput and userInput[-1] == ")"):
        tobeUpdated = (userInput.split("("))
        emails = tobeUpdated[1].strip(")")
        inputList = emails.split(",")
        if(" " in inputList[1] or " " in inputList[0]):
            inputList[1] = inputList[1].replace(" ", "")
            inputList[0] = inputList[0].replace(" ", "")
        studentNumber = inputList[0]
        new_email = inputList[1]
        
        update_query = ("""UPDATE students SET email = '{}' WHERE student_id = {};""").format(new_email, studentNumber)
        cursor.execute(update_query)
        connection.commit()

    
    elif("deleteStudent(" in userInput and userInput[-1] == ")"):
        tobeDeleted = userInput.split("(")
        studentNumber = tobeDeleted[1].replace(")", "")

        delete_query = "DELETE FROM students WHERE student_id = {};".format(studentNumber)
        cursor.execute(delete_query)
        connection.commit()


cursor.close()
connection.close()
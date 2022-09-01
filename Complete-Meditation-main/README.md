# Complete-Meditation

# CERN Experiment Database

## Description
To create an API for a CERN experiment database – designed to allow users connected with CERN to login into a system with upload and download experiment data functionality with constrictions on access based on user privilege; the learning outcome from the project was to demonstrate Secure Software Development (SSD) based on the OWASP top ten security vulnerabilities. 
## 1. Implementation
The CERN experiment database API was programmed in Python3, utilizing Python SQLite3 module to interact with SQLite databases and with Flask providing the framework to connected each module. Code written in IDE's Visual code studio and PyCharm.
## 2. Architecture 
We have used Flask to build a web application microservice. 
## 3. Features
### User funtionality
* User menu (command line input)
* Sign up/login
  
Sign up and login steps take apropriate inpurs to create a user account 
or to allow for access to the database respectively. These functionalities
are implemented by `log_in()` and `sing_up` functions in `Input_checker.py` file.
* Upload/download (experiment data)

Users can upload/download their files. The whole process is done using `user_download()`, `user_upload()`, `user_delete_file()` and `user_list_files()` functions.
### Security Features
Selected to demostrate SSD and based on the OWASP top ten security vulnerabilities this project incoporates the following security features.
* Authentication
  
Authentication part of the software ensures that only authorized individuals 
have access to the system. In our implementation, during the login step 
(`log_in()` in `Inpur_chekre.py`), a user provides their username and password. 
These data are also stored in the database. The application uses a hashing 
algorithm (`hashing()` in `Authentication_checker.py`) on the input-password and
compares it with a hashed password stored in the database (search takes place 
based on username as a primary key). If these two passwords are the same, then 
logging-in is successful and `log_in()` returns a user object.

* Hashing  
  
For authentication, we used built-in hashlib library to protect the password by 
SHA-2 cryptographic hash function that transforms each password with a random 
length into a sequence 256 bits and all secured hashed passwords will be stored
in the database.

* Data encryption

Data is sent to the Encryptor class that encrypts the data with a salted password that generates a key in PBKDF2, as CERN requires FIPS-140 compliance. OWASP recomends internal hashing, for example SHA-256. Iteration count is 7000100, but can be altered. The slowless of the code is to minimise the attack surface of brute force and dictionary attacks. The encryption standard is AES with mode CBC that is a block cipher, that both ciphers the chosen data and encrypts it. The data is readable with the same derived key. 

* Parametrised Queries

Parametrised queries seperate the data from the SQL statement to be compliled. As the query is translated placeholders `("?")`  will be used instead of parameters (column value) and the parameter value would be supplied at the time of execution. For example ; `(name, format, subject) VALUES(?, ?, ?)`. This helps prevent SQL injection attacks where actors inject malicious code to try change the intention of the query.

* Authorisation
## 4. Installation
### Dependencies 
The programme requirements :
* Python 3.10
* Flask 2.2.2 
* SQLite3
* Pycryptodome
* readerwriterlock
### How to run
Run `'python server.py'` for a startup flask service listening to 8080 port. The server enables https with self-signed ssl certificatoin,  binding on 127.0.0.1. If you use a browser to send the request, it could indicate a safety risk - but you can use client.py to send command to the server side. Execute ``client.py`` to demostrate download (change variable for file_name). To demostrate upload for security reasons file upload just supports PDF, TXT and ZIP.
## 5. Project files
List of files and brief description of functionality
* `Encryptor.py` defines `Encryptor` class, minimise brute force attacks 
* `client.py`
* `database_cern.py` defines initial connection to database
* `flask_cert.pem` holds flask certificate 
* `flask_private-key.pem` Private key
* `plaeholder.txt`
* `requirements.txt`
* `server.py`module to forward valid requests to one defined handler
* `session.py` module focusing on session management
* `Authentication.py` creates new user and/or new user object
* `Authentication_checker.py`contains password hashing function, user authentication checker fuction and password strength function
* `Classes.py` defines User class, Administrator class and Experiment class a created or loaded experiment
* `Input_checker.py` includes `log_in` fuction which checks username and password, and  `sing_up` checker function that examines inputs provided by the
    user before the sign-up details are passed through and a new user is added to the database.
* `database.py` creates a database connection to a SQLite database
* `database_file.db`
* `database_managment.py` controls SQL fuctions for database management
* `main.py` module includes function to start the script linked to the the authentication module via (login and sign up) and prints the user menu
* `main_user.py` a part of the main.py module, helps create user menu
* `AuthorisationDataBase.py` creates database to store authorisation data
* `authorisation.py` defines authorisation class 
* `unittests.py` Unittests for Authentication part of the software
* `crud.py` executes crud commands on database, utilises parametrised queries
* `crud_server.py` utilises JSON for communication to and from server
* `db_and_table.py` connection to `cern.db` and creation of userfiles table using SQLite3 
* `test_crud_insert.py` CRUD unit test

## 6. Tests
Unittest has been used for testing.
| Test number | Function | Input/condition | Expected result | Actual result | Screen reference |
| --- | ----------- | --- | ----------- | --- | ----------- |
| 1 | Print object salt | newVar = obj.salt/print(newVar) | first line of appendix1 | first line of appendix1 | 1 |
| 2 | Print derived key | print(obj.PBKDF2Key) | second line of appendix1 | second line of appendix1 | 1 |
| 3 | print ciphered data | print(obj.ciphered_data) | third line of appendix1 | third line of appendix1 | 1 |
| 4 | Unittests for Authentication | Built-in inputs | Run 24 tests OK | Run 24 tests OK | 2 |
| 5 | Unittests for authorisation | permission verify | all testing passed | all testing passed | 3 |
| 6 | Unittests for AuthorisationDataBase | read and write permission data | all testing passed | all testing passed | 4 |
| 7 | Unittests for session | connect client request to user | all testing passed | all testing passed | 5 |
 
## 7. References
Great Learning Team (2021). README File – Everything you Need to Know [online] Available from:
https://www.mygreatlearning.com/blog/readme-file/ [accessed 28th August 2022]

Pynative.com (2021). Python MySQL Execute Parameterized Query using Prepared Statement. [online] Available from:
https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/

## 8. Appendix
Screen reference 1

![Screenshot 2022-08-29 at 21 09 27](https://user-images.githubusercontent.com/67603121/187289115-41281ee2-d02f-4c26-91d6-f41995e13ba8.png)

Screen reference 2

![Authentication_Unittests](https://user-images.githubusercontent.com/88317386/187291810-9f3c56d6-e2c2-4c75-a1bc-d3acada50d9b.jpg)



Screen reference 3
![image](https://user-images.githubusercontent.com/94125132/187293697-3743db8c-af0a-4c5d-a1e8-20271d33fcdf.png)

Screen reference 4
![image](https://user-images.githubusercontent.com/94125132/187293886-ff701017-fe46-4f20-8021-2196aec0a4b9.png)

Screen reference 5
![image](https://user-images.githubusercontent.com/94125132/187294390-0c45d74a-5617-46c2-9a51-c64db2f679b1.png)

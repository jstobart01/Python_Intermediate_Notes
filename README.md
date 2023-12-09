# Python_Intermediate_Notes
## Notes from Intermediate Python Course
### This is for uploading my results from python tutorial
### LESSON 01 - Hello, World!
Hello, World! -> welcome to Python
### LESSON 02 - Print Statement
Just contains a welcome message using standard Python3 print statements
### LESSON 03 - Basic 'if' statement
Contains a basic example of an 'if' statement on one line.
### LESSON 04 - Data Types
Examples of the following:
- Concatenation
- Casting a number to a string
- Multiline strings
- Escape special characters
- String methods
- String index values
- Boolean Data Type
- Numeric Data Types
    - Integer
    - Float
    - Complex
- Built-in funcitons for numbers
- Casting a string to a number
### LESSON 11 - Scope
Notes on handling scope in Python
### LESSON 12 - Closure
Notes on how to utilize closure to eliminate use of global variables
### LESSON 13 - F-Strings
Notes on how to format strings an different ways:
- Standard print method
- %s method
- format method
- f-string method (preferred)
### LESSON 17 - Lambda functions
Examples of how to use lambda functions
### LESSON 18 - Classes & Objects
Shows how to create classes & objects; including class inheritance and polymorphism
### LESSON 19 - Errors & Exceptions
Shows how to handle erros and create your own responses.
### LESSON 20 - Object Oriented Programming (OOP)
Builds a bank account app to demonstrate OOP.
### LESSON 21 - PIP & Virtual Enviroments
PIP is used to install packages not initially included with python
1. To install a package
$ py -m pip install {package name} (eg. requests)

2. To see what packages are installed already
$ py -m pip list

3. To choose which version of a package to use
$ py -m pip install {package name}=={revision} (eg. requests==2.30.0)

4. To update to latest version of package
$ py -m install -U {package name}

5. To uninstall a package
$ py -m uninstall {package name}

6. To see details about a package
$ py -m pip show requests

7. To create a list of requirements
$ py -m pip freeze > requirements.txt

Virtual Enviroment
$ py -m venv .venv (creates the virtual environment)
$ source .venv/Scripts/activate (activates the virtual enviroment)
$ deactivate (deactivates the virtual environment)

Never include the API_KEY in your development files. (should be inside your .env file)
### LESSON 22 - File Operations
R - Read
A - Append
W - Write (Overwrite)
X - Create

### LESSON 23 - Final Project
Static folder: holds any static file (e.g. CSS, JS, images etc.)
Templates: stores the HTML files

HTML Tip for VSCode: On a new html file type ! and then hit tab. This will auto-generate a skeleton for an HTML file.

For this project I used Flask.
- To install Flask use $ py -m pip install Flask
- You can also install multiple packages by doing something like this $ py -m pip install requests python-dotenv Flask

Tip: If you install a new package don't forget to re-create a new requirements file (i.e. pip freeze > requirements.txt). This will update the current one.
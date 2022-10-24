# CS50-Python

My solutions to Harvard's CS50 Python course

Course Description: Learn about functions, arguments, and return values (oh my!); variables and types; conditionals and Boolean expressions; and loops. Learn how to handle exceptions, find and fix bugs, and write unit tests; use third-party libraries; validate and extract data with regular expressions; model real-world entities with classes, objects, methods, and properties; and read and write files. Hands-on opportunities for lots of practice. Exercises inspired by real-world programming problems.

Week 0 - Functions, Variables

    Indoor Voice - convert input to lowercase
    Playback Speed - replace ' ' with '...'
    Making Faces - replace :) and :( with emojis
    Einstein - calculates e = mc^2
    Tip Calculator - calulates a tip given % tip and total bill

Week 1 - Conditionals

    Deep Thought - matches a response to certain user input
    Home Federal Savings Bank - returns different answers depending on user input
    File Extensions - determines filetype of a user input
    Math Interpreter - solves a user input math equation
    Meal Time - splits user input to determine if its mealtime

Week 2 - Loops

    camelCase - contverts camelCase str to camel_case str
    Coke Machine - adds valid coin inputs to buy a 50 cent bottle of coke
    Just setting up my twttr - removes vowels from user input string
    Vanity Plates - checks if desired vanity plate is valid given a variety of conditions
    Nutrition Facts - returns calorie content of a fruit from user input

Week 3 - Exceptions

    Fuel Gauge - Determines % gas tank fullness, checks input for ValueError and ZeroDivisionError
    Felipe's Taqueria - Creates a running tally of a menu order, terminates on ctl+D, ignores invalid menu entries
    Grocery List - creates a gocery list from user input, terminates on ctl+D, catches any KeyErrors
    Outdates - converts MM/DD/YYYY and Month Day, Year to YYYY-MM-DD, continually asks for proper input

Week 4 - Libraries

    Emojize - uses emoji library to return input as emoji
    Frank, Ian and Glen's Letters - Renders text in figlet fonts chosen by user's command line arg
    Adieu, Adieu - uses inflect library to print a list of names as "name, name, ... and name"
    Guessing Game - uses random library to make a number guessing game
    Little Professor - generates addition problems of varying difficulty based on user input
    Bitcoin Price Index - uses requests and json libraries to pull BTC price from site

Week 5 - Unit Tests

    Testing my twittr - tests prior function under various cases
    Back to the Bank - tests prior function under various cases
    Re-requesting a vanity plate - tests prior function under various cases
    Refueling - uses pytest to check for ZeroDivisionErrors and ValueErrors

Week 6 - File I/O

    Lines of Code - calculates lines of code in a python file, ignoring comments and blank lines, only accepts python files
    Pizza Py - makes ascii art menu from a csv menu file, exits if file not entered, not found or not a csv file
    Scourgify - accepts a csv with ["Lastname, Firstname", House] and outputs a csv with [Firstname, Lastname, House]
    CS50 P-Shirt - accepts an original image file and output image file, pastes an image over the original and saves to the output image file

Week 7 - Regular Expressions

    Numb3rs - determines if user input a valid IPv4 address, with separate unit test
    Watch on Youtube - parses an embedded URL and returns a shareable URL
    Working 9 to 5 - accepts work hours in "9:00 AM to 5:00 PM" and "9 AM to 5 PM" format and converts to military time, checks for invalid formats and impossible times
    Regular, um, expressions - counts how many times "um" is said in an input. ignores when 'um' is in a word like "yum"
    Response Validation - uses validator_collection library to check if an email is in a valid email address format

Week 8 - Object-Oriented Programming

    Seasons of Love - calculates how many minutes have passed since a given date, returns answer in words a la "five hundred twenty-five thousand six hundred mintues"
    Cookie Jar - creates a cookie jar class with specified capacity and deposit/withdraw methods and properties for capacity and cookies currently in the jar
    CS50 Shirtificate - creates a PDF class using fpdf library. Includes a shirt image overlayed with "{name} took CS50"

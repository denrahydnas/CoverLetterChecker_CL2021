# CoverLetterChecker_CL2021
Code Louisville Python Cohort Project 2021
I'm going to create a program that will compare a cover letter to a job listing and verify keywords and a few other quantifiable checks. It will:

==> allow User to submit Job Listing text, which is then parsed for keywords, compared to existing keyword list (ex: https://www.jobscan.co/blog/resume-words/#resume-keywords_)
==> allow user to see parsed keyword list or submit existing Cover Letter
==> allow user to add keyword to list if omitted
==> check cover letter and job listing match - job title, company name, etc
==> compare cover letter to keywords in job listing, return match results
==> check cover letter for overused words, suggest synonyms (use MW API (https://dictionaryapi.com/products/api-collegiate-thesaurus)?)
==> check cover letter for passive voice, percentage of sentences beginning with I, etc. 


Features List:

==> Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program

==> Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program

==> Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

==> Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code. For example, you could create a function that reads how many items there are in a text file, returns that value, and later uses that value to execute a loop a certain number of times.

==> Analyze text and display information about it (ex: how many words in a paragraph)

==> Connect to an external/3rd party API and read data into your app

MAYBE: Create a web app version of it using Flask








These Items are in the Project requirements but I'm not using them at this time - leaving them here for future reference:

Implement a log that records errors, invalid inputs, or other important events and writes them to a text file
Create a class, then create at least one object of that class and populate it with data. The value of at least one object must be used somewhere in your code
Implement a regular expression (regex) to ensure a field either a phone number or an email address is always stored and displayed in the same format
Connect to an external/3rd party API and read data into your app
Create 3 or more unit tests for your application
Build a conversion tool that converts user input to another type and displays it (ex: converts cups to grams)
Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event)
Visualize data in a graph, chart, or other visual representation of data
“Stretch” Features
These count too! But they will require going outside of Treehouse to learn about and may be more challenging
Implement a “scraper” that can be fed a type of file or URL and pull information off of it. For example, a web scraper that lets you provide any website URL and it will find certain keywords on the page
Implement optical character recognition (OCR) that you can upload PDFs to and it will generate the text 
Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display

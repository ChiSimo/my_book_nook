# My Book Nook - Terminal App

A terminal-based app to track books you're reading or have read. 
The app runs in the terminal and allows you to add books, mark them as read, and view your personal library. 

📚 Welcome to My book Nook 📚
-----------------------------

What Does It Do?
1. Add books with title, author, year, personal review and date
2. View your current book list 
3. Mark books ad read
4. Save your books to a JSON file so nothing is lost


How To Run It - Setup

1. Make sure Python3 is installed
2. Open your Terminal
3. Navigate the folder containing main.py
4. Install dependencies:

     pip3 install colorama

     python3 main.py

Dependencies

colorama  -  Makes the text colorful to make the app more fun and easier to use
datetime  -  Adds a date for each book added
json      -  Saves and load book data from a file

File List
1. main.py  -  The main application 
2. books.json - Auto-generated file that stores the books when are created in the point "1"
3. README.md  - The Help File

License 
All external libraries used are publicly available
1. colorama is licensed under the BDS License
2. JSON and DateTime are Python standard libraries

# personal-library-manager 📚
A Python-based command-line application to manage your personal book collection, track reading progress, and organize your reading materials.

## Features ✨
Add new books to your collection with details like title, author, year, genre

Remove books you no longer want to track

Search books by title or author

Update book details if you need to make changes

View all books in your collection with complete details

Track reading progress with completion statistics

Persistent storage - all data saved to a JSON file

## Installation ⚙️
Make sure you have Python 3.x installed

Clone this repository or download the ```main.py``` file

No additional dependencies required!

## Usage 🚀
Run the application with:
```
python main.py
```
 ## Menu Options:
Add a new book - Enter book details to add to your collection

Remove a book - Delete a book by title

Search for books - Find books by title or author

Update book details - Modify information for an existing book

View all books - See your complete collection

View reading progress - Check your reading statistics

Exit - Quit the application

## Data Storage 💾
All book data is automatically saved to books_data.json in the same directory. The file will be created automatically when you add your first book.

## Example Book Entry 📖
```json

{
        "title": "Eloquent JavaScript",
        "author": " Marijn Haverbeke",
        "year": "2011 (Updated in 2018)",
        "genre": "JavaScript Programming",
        "read": false
    },
```
## Contributing 🤝
Contributions are welcome! Please open an issue or pull request for any improvements.



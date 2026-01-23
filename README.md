# To-Do List CLI

A command-line To-Do List application built in Python with SQLite. Created as a hands-on learning project to practice database operations, SQL, and Python fundamentals.

## Purpose

This project was built from scratch to practice:

- **SQL CRUD Operations** - CREATE, READ, UPDATE, DELETE
- **Database Design** - Table schema with proper data types
- **Python Fundamentals** - Functions, loops, user input
- **Modular Code Structure** - Separation of concerns across files

## Project Structure

```
To-Do-Task-CLI-Project/
├── config.py      # Database configuration
├── database.py    # All database operations (CRUD)
├── main.py        # Main menu loop and user interface
└── README.md
```

## Database Schema

```
┌──────────┬──────────────────┬──────────────────────┬───────────────────────────────┐
│ id       │ Task             │ Status               │ created_at                    │
│ INTEGER  │ TEXT             │ TEXT                 │ TIMESTAMP                     │
│ PK AUTO  │ NOT NULL         │ DEFAULT 'No'         │ DEFAULT CURRENT_TIMESTAMP     │
├──────────┼──────────────────┼──────────────────────┼───────────────────────────────┤
│ 1        │ "Buy groceries"  │ "No"                 │ 2026-01-19 17:00:00           │
│ 2        │ "Walk the dog"   │ "Yes"                │ 2026-01-19 17:05:00           │
└──────────┴──────────────────┴──────────────────────┴───────────────────────────────┘
```

## Features

- **View Tasks** - Display all tasks with ID, description, and completion status
- **Add Task** - Create a new task
- **Mark Complete** - Update a task's status to "Yes"
- **Delete Task** - Remove a task by ID
- **Persistent Storage** - Tasks saved in SQLite database

## How to Run

```bash
# Clone the repository
git clone https://github.com/Nicolasg7777/To-Do-Task-CLI-Project.git
cd To-Do-Task-CLI-Project

# Run the application
python main.py
```

## Usage Example

```
===== To-Do List =====
1. View tasks
2. Add Task
3. Mark task complete
4. Delete task
5. Exit

Enter choice (1-5): 2
What is the task you would like to add? Buy groceries
Task Successfully Added.

Enter choice (1-5): 1
This is list:
1. Buy groceries - Status: No

Enter choice (1-5): 3
Which Task would you like to change? 1

Enter choice (1-5): 1
This is list:
1. Buy groceries - Status: Yes
```

## Skills Practiced

| Concept | Implementation |
|---------|----------------|
| SQL CREATE | Table with PRIMARY KEY, AUTOINCREMENT, DEFAULT values |
| SQL INSERT | Parameterized queries with `?` placeholders |
| SQL SELECT | Fetching all rows with `fetchall()` |
| SQL UPDATE | Modifying specific rows with WHERE clause |
| SQL DELETE | Removing rows by ID |
| Python Functions | Modular code with clear responsibilities |
| User Input | Menu-driven interface with input validation |

## Learning Notes

This project includes detailed comments documenting my thought process and learning journey. Key takeaways:

- `cursor.execute()` runs SQL commands
- `conn.commit()` saves changes (required for INSERT, UPDATE, DELETE)
- `conn.close()` closes the database connection
- Parameterized queries (`?`) prevent SQL injection
- `fetchall()` returns a list of tuples

## Author

**Nicolas Garcia**
Personal learning project for Python and SQL skill development.

## License

This project is for educational purposes.

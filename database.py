
# We are going to to be using sqlite3 since its already implemented into python.

import sqlite3
from config import DATABASE_NAME

def get_connect():
    '''
        this is where we connect to teh databse.

        i will go ahead and tell you my thought process and how it is that i solved this.

        - so right off the bat i got stuck on my return of this funciton to basically return that the 
        connection was connected.

        i went ahead and searched sqlite3 where i got some documnetation on how to create a test
        database connection.

        which it tells you to do the following.

        import sqlite3

        # Check SQLite version
        print(f"SQLite version: {sqlite3.sqlite_version}")
        print(f"SQLite module version: {sqlite3.version}")

        # Create a test database connection
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('SELECT SQLITE_VERSION()')
        print(f"Database engine version: {cursor.fetchone()[0]}")
        conn.close()

        but then i realized that i would have to be calling the conn everywhere that i wanted 
        the databse to be connecting to.

        so i looked at the AI agent code in order to maybe come up with a efficent way of doing it
        and found out that the get_connection function is easier to just get called anywhere
        by making it a return to that fucntion? you can correct me if i am using bad termonlogy.

        based on this we then just return sqlite3.connect(DATABASE_NAME)
    '''
    return sqlite3.connect(DATABASE_NAME)


'''
    this is where we can go ahead and create our tables.

    1. where ID is going to be one.
    2. where Task.
    3. status.

'''

# Creating our Table.
'''
    already forgot how to create so i will be looking at the sqlite3 documentation.
    forgot that we need to have an initiallize database function.
    which i found out by looking at the AI agent code. sorry again.

'''

# Initializing Databse function

def Initialize_database():

    conn = get_connect()
    cursor = conn.cursor()

    '''
        really had to think about this for like 30 seconds on what does cursor do?
        i ended up pausing and thinking about it and making sure i understood exactly what was happening.
        and ended up in the conclusion that cursor calls the conn variable? again please correct my terminallogy
        or maybe its a fuction.

        regardles i knows that cursor is calling the 'conn' that then calls the get_connet() function that
        we defined earlier. that then calls cursor() which means everytime we use cursor we are calling it to 
        the databse that then connects to the databse to make those changes.

        moving on until i become stuck.

        was again stuck in terms of creating table where then i just went back to sqlite3 doc
        where i learned how to create it.

        seems like i forgot to do CRUD after creating my schema model? again correct my terminology
        if its wrong.

        i did the ?, ?, ?, ? becuase of it being auto incriminted and it being inserted by 
        uer input? i could be wrong there but i think this is the right way.


    '''
    # Creating ID Table
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Task TEXT NOT NULL,
                   Status TEXT NOT NULL DEFAULT 'No',
                   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    


    '''
        if you could explain why this is needed that would be great so i can learn faster.
        i think it commits all in terms of creating the table if does not exist by the way 

        and i think it then closes the the connection so that its not running in the back and everything is
        run efficiently.
    '''
    conn.commit()
    conn.close()

def list_tasks():
    # this will show the user the tasks.
    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tasks')
    
    tasks = cursor.fetchall()

    # we dont need a commit here becuase commit is only for insert,update and delete.
    conn.close()
    return tasks

    
# Creating Actions and the first action is add.
def Add_task(Task):
    
    conn = get_connect()
    cursor = conn.cursor()

    
    cursor.execute(
            'INSERT INTO tasks (Task) VALUES (?)',
            (Task,)
        )
    conn.commit()
    conn.close()
    

'''
    i dont really understand why we need to add task_id? why cant it just be task? is it beucase itll be based
    on the id? so itll be task_id or would it be task.id?
'''

def Update_task(task_id):
    conn = get_connect()
    cursor = conn.cursor()

    # First we need to choose which row we want to change the status of.
    cursor.execute(
        'UPDATE tasks SET Status = ? WHERE id = ?',
        ('Yes',task_id)
    )

    conn.commit()
    conn.close()

def Delete_task(task_id):

    conn = get_connect()
    cursor = conn.cursor()

    # delete task by picking that ID
    cursor.execute(
        'DELETE FROM tasks WHERE id = ?',
        (task_id,)
    )

    conn.commit()
    conn.close()


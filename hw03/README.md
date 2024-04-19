# HW03 Structuring Data and Querying It

Before starting this Assignment, make sure to read all the required materials for this module, which can be found in the corresponding module Discussion.

## Essentials to Keep in Mind

What differentiates a _relational database management system_ (RDBMS)? Just looking at SQLite, one of smallest DB implementations...

- **Performance & Scale**
  - [Max DB size: 281Tb](https://www.sqlite.org/limits.html)
  - Max row size: 1Gb
- **Referential Integrity**
  - [Foreign Key Support](https://www.sqlite.org/foreignkeys.html)
  - `PRAGMA foreign_keys=ON`
  - ON DELETE and ON UPDATE
- **Data Constraints**
  - [STRICT Tables](https://sqlite.org/stricttables.html)
- **Complex Queries & Automation**
- **Security & Reliability**
  - Atomicity, Consistency, Isolation, Durability (ACID)

## Key Concepts

- RDBMS are designed to store data in a structured manner using tables, which makes it easy to organize, query and analyze data.
- RDBMS provide mechanisms for ensuring data integrity, such as enforcing constraints and relationships between tables, which helps to prevent data inconsistencies and errors.
- RDBMS ensure consistency of data across the entire database, which helps to avoid data duplication and redundancy.
- RDBMS allows for the creation of indexes, which can improve query performance and speed up data retrieval.
- RDBMS such as SQLite are designed to handle large datasets, while applications like Excel can become slow and unwieldy as the amount of data grows.
- With SQLite, you can use SQL to query and manipulate data in a variety of ways, whereas Excel is primarily focused on working with spreadsheets and performing basic calculations.
- SQLite is a popular and widely used relational database management system (RDBMS) that is lightweight and efficient.
- SQLite stores data in a file-based format, which means that it does not require a separate server process and can be easily incorporated into an application.
- SQLite supports standard SQL commands for querying and manipulating data, making it easy to learn and use for those with a background in SQL.
- To use sqlite3 in Python, you need to import the module and create a connection to the SQLite database file.

## Additional Resources

- [SQLite Databases With Python](https://www.youtube.com/watch?v=byHcYRpMgI4) (90ish mins)
- [Python SQLite Tutorial](https://www.youtube.com/watch?v=pd-0G0MigUA) (30ish mins)

## Our Handy Graphical "Database Client"

    > sqlite_web database.sqlite3

## #NeverForget

    SELECT *
      FROM movies
    LEFT OUTER JOIN map_movie_celeb
      ON map_movie_celeb.movie_id = movies.id
    LEFT OUTER JOIN celebs
      ON map_movie_celeb.celeb_id = celebs.id
    WHERE movies.id = '/m/the_wizard_of_oz_1939'

# Completing the Homework

Create a `hw03` project/folder that demonstrates the following:

- Contains a Python script named `hw03.py`.
- Reads data from a `hw03.sqlite3` database.
- Runs a query against the database using a `WHERE` clause.
- Performs a `CREATE TABLE`, `INSERT`, and `UPDATE` to the database.
- Leverages `pipenv` (and a `Pipfile`) to manage its dependencies. (If any.)
- Provides a `screenshot.jpg` of the script running successfully.
- Does not directly copy examples from the book or class.

Save a screenshot of your app _(successfully running)_ to `screenshot.jpg` in your project folder. (You can use `WIN+SHIFT+S` for easy access to the Windows built-in screenshot tool.)

Bundle your project folder into a `bundle.docx` file by simply placing [`bundle`](https://github.com/seansbox/pybundler/raw/main/bundle.exe) in your project folder and running it. The required files, such as \*.py, Pipfile, screenshot.jpg, etc., will be automatically included. Finally, submit the `bundle.docx` file to _Canvas_.

# HW04 Mapping Objects and Speaking Excel

_Before starting this Assignment, make sure to read all the required materials for this module, which can be found in the corresponding module Discussion._

## In A Nutshell

In this module, we explore Object Relational Mappers (ORMs) with a focus on SQLAlchemy. ORMs simplify interactions between a Python application and a relational database, streamlining data management and manipulation. ORMs do a whole lot of heavy lifting for you, such as creating tables, inserting data, and querying data... without writing any SQL by hand. We will also explore how to read and write Excel files using the `openpyxl` library.

## Why ORMs?

1. **_Abstraction and Object-Oriented Programming (OOP)._** ORMs allow you to work with database tables as if they were Python objects, making it easier to understand and work with complex data relationships in an object-oriented way.

2. **_Database Agnosticism._** ORMs abstract the underlying database system, allowing you to switch between different database backends with minimal code changes.

3. **_Code Reusability and Maintainability._** ORMs encourage a modular, reusable code structure, making it easier to maintain and modify your application over time.

4. **_Enhanced Security._** ORMs can help protect against common security vulnerabilities, such as SQL injection attacks, by automatically escaping and sanitizing user input.

5. **_Productivity and Rapid Development._** ORMs simplify and automate common database tasks, such as creating tables, writing queries, and managing transactions, allowing you to focus on application logic and speeding up development.

6. **_Query Language Independence._** ORMs allow you to write database queries using Python syntax rather than raw SQL, making it easier to read and write code and reducing the need to learn multiple query languages.

7. **_Built-in Features and Community Support._** Popular ORMs like SQLAlchemy and Django ORM come with a wealth of built-in features and a strong community of developers, providing extensive documentation, plugins, and support.

SQLAlchemy is a popular Python library for working with relational databases. It provides a full suite of well-integrated components for mapping between Python objects and database tables, creating and executing SQL statements, and handling transactions.

The main features of SQLAlchemy include:

- Support for a wide range of databases, including SQLite, PostgreSQL, MySQL, and others.
- Powerful and flexible query API with support for filters, joins, and other SQL constructs.
- Transaction management, connection pooling, and other optimizations for efficient database access.
- Extensibility through custom data types, functions, and other components.

As part of the ISIT 360 Database Application Development course, you will learn the basics of how to design and implement both SQL and non-SQL databases, as well as write queries that filter, sort, and summarize table data. SQLAlchemy can be used to achieve these objectives, but your choice whether to use it will depend on your specific application requirements and preferences.

## Additional Resources

# Completing the Homework

Create a `hw04` project/folder that demonstrates the following:

- Meets the technical requirements outlined below:
  - Demonstrates use of `SQLAlchemy` ORM to define at least two models.
  - Utilizes a ForeignKey to link the two models. (Either a One-to-Many or a Many-to-Many relationship.)
  - Inserts data into the database using the ORM.
  - Queries data from the database using the ORM.
  - Demonstrates use of the `openpyxl` library to read and write an Excel file. Yeah, weird to do this in the same project, but it's a good exercise and we're trying to finish two chapters in one assignment.
- Leverages pipenv (and a Pipfile) to manage its dependencies.
- Includes a screenshot.jpg of the app successfully running. (You can use `WIN+SHIFT+S` for easy access to the Windows built-in screenshot tool.)
- Does not directly copy examples from the book or class.

Bundle your project folder into a `bundle.docx` file by simply placing [`bundle`](https://github.com/seansbox/pybundler/raw/main/bundle.exe) in your project folder and running it. The required files, such as \*.py, Pipfile, screenshot.jpg, etc., will be automatically included. Finally, submit the `bundle.docx` file to _Canvas_.

import sqlite3
import csv

# Paths to the CSV files
db_path = "db.sqlite3"
db_tables = {
    # Table names and their CSV file names
    # Follows the Django table naming convention
    "movies_genre": "default_data/genres.csv",
    "movies_celeb": "default_data/celebs.csv",
    "movies_movie": "default_data/movies.csv",
    "movies_movie_celebs": "default_data/map_movie_celebs.csv",
    "movies_movie_genres": "default_data/map_movie_genres.csv",
}

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# Import data from CSV files into the database
def insert_csv_data(table_name, csv_file):
    # Read the CSV file to get the columns and data
    with open(csv_file, "r", encoding="utf-8-sig") as csvfile:
        csvreader = csv.DictReader(csvfile)
        columns = csvreader.fieldnames
        placeholders = ", ".join("?" * len(columns))
        columns_str = ", ".join(columns)

        # Insert data into the table
        for row in csvreader:
            values = [row[col] for col in columns]
            cursor.execute(f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})", values)


try:
    # Start a transaction
    conn.execute("BEGIN TRANSACTION")

    # Insert data into the tables
    for table_name, csv_file in db_tables.items():
        insert_csv_data(table_name, csv_file)

    # Commit the transaction
    conn.commit()
except Exception as e:
    # Rollback the transaction if any insertion fails
    conn.rollback()
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    conn.close()

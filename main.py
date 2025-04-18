import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="book_db",
    user="postgres",
    password="admin123"  
)

cur = conn.cursor()
#drop table if exists
cur.execute("DROP TABLE IF EXISTS books")

# Create the books table
cur.execute("""
    CREATE TABLE books (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100),
        author VARCHAR(100),
        year INT
    )
""")

conn.commit()
print("Table created successfully!")




books = [
    ("Harry Potter", "J.K. Rowling", 1997),
    ("The Hobbit", "J.R.R. Tolkien", 1937),
    ("1984", "George Orwell", 1949),
    ("The Alchemist", "Paulo Coelho", 1988)
]

cur.executemany("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", books)

conn.commit()
print("Books inserted successfully!")

cur.execute("SELECT * FROM books")
rows = cur.fetchall()

for row in rows:
    print(row)


#update
cur.execute("UPDATE books SET year = 1950 WHERE title = '1984'")

conn.commit()
print("Book updated successfully!")

#delete
cur.execute("DELETE FROM books WHERE title = 'The Alchemist'")

conn.commit()
print("Book deleted successfully!")

cur.close()
conn.close()

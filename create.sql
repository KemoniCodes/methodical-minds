
CREATE TABLE books
(
    book_id SERIAL PRIMARY KEY,
    isbn VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    year INTEGER NOT NULL
);

INSERT INTO books
    (isbn, title, author, year)



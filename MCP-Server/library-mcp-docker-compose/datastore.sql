CREATE DATABASE IF NOT EXISTS library;
USE library;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    department VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create books table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(50) UNIQUE,
    genre VARCHAR(100),
    available_copies INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample students
INSERT INTO students (first_name, last_name, email, department)
VALUES
('John', 'Doe', 'john.doe@example.com', 'Computer Science'),
('Emma', 'Watson', 'emma.watson@example.com', 'Electronics'),
('Rahul', 'Sharma', 'rahul.sharma@example.com', 'Mechanical'),
('Priya', 'Reddy', 'priya.reddy@example.com', 'Information Technology'),
('David', 'Miller', 'david.miller@example.com', 'Civil');

-- Insert sample books
INSERT INTO books (title, author, isbn, genre, available_copies)
VALUES
('Clean Code', 'Robert C. Martin', '9780132350884', 'Programming', 5),
('The Pragmatic Programmer', 'Andrew Hunt', '9780201616224', 'Programming', 3),
('Database System Concepts', 'Abraham Silberschatz', '9780073523323', 'Database', 4),
('Design Patterns', 'Erich Gamma', '9780201633610', 'Software Engineering', 2),
('Introduction to Algorithms', 'Thomas H. Cormen', '9780262033848', 'Algorithms', 6);

-- Verify data (optional)
SELECT * FROM students;
SELECT * FROM books;
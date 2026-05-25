from connect_db import execute_query
import datetime
from typing import Any

def issue_book(issued_by_librarian_id:int, student_id: int, book_id: int, date: str, status: str, issue_condition: str, transaction_type: str, quantity: int) -> str:
    
    """Get number of copies"""
    query = "SELECT copy_id FROM book_copies WHERE book_id = %s AND status = %s LIMIT 1;"
    params = (book_id, status)
    copy_id = execute_query(query,params)[0][0]
    print(copy_id)

    """Create loan transaction"""
    issued_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    due = datetime.datetime.now() + datetime.timedelta(days=15)
    due_time = due.strftime("%Y-%m-%d %H:%M:%S.%f")
    #print(issued_time)
    #print(due_time)
    #issued_at = issued_time.strftime("%Y-%m-%d %H:%M:%S")
    #due_at = due_time.strftime("%Y-%m-%d %H:%M:%S")

    query = "INSERT INTO loan_transactions (copy_id, borrower_user_id, issued_by_librarian_id, issued_at, due_at, issue_condition,status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    params = (copy_id, student_id, issued_by_librarian_id, issued_time, due_time, issue_condition, transaction_type)
    execute_query(query,params)

    """Capture newly created loan_id"""
    query = "SET @loan_id = LAST_INSERT_ID();"
    execute_query(query)

    """Mark copy as unavailable"""
    query = "UPDATE book_copies SET status = %s WHERE copy_id = %s"
    params = (transaction_type, copy_id)

    execute_query(query, params)

    """Reduce available book count"""
    query = "UPDATE books SET available_copies = available_copies - %s WHERE book_id = %s"
    params = (quantity, book_id)
    execute_query(query, params)


    """Add ledger entry"""
    query = "INSERT INTO book_ledger_entries (book_id, copy_id, loan_id, entry_type, entry_date, quantity) VALUES(%s,%s,@loan_id,%s,%s,%s)"
    params = (book_id, copy_id, 'ISSUE', issued_time, quantity)
    execute_query(query, params)
    print("Book  Issued Successfully!")
    return f'Book {book_id} Issued Successfully!'

    




if __name__ == "__main__":
    issue_book(1, 1, 1, '2026-05-24', 'AVAILABLE', 'Good', 'ISSUED', 1)
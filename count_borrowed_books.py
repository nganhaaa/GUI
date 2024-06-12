import psycopg2

def count_borrowed_books(member_account_id):
    try:
        conn = psycopg2.connect("dbname=kkk user=postgres password=236204")
        cursor = conn.cursor()

        # Truy vấn SQL để đếm số lượng phiếu mượn sách của thành viên và chưa trả
        cursor.execute("SELECT COUNT(*) FROM Borrowing_Receipts WHERE member_account_id = %s AND status = 'Borrowing'", (member_account_id,))
        count = cursor.fetchone()[0]

        return count

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

    finally:
        if conn:
            cursor.close()
            conn.close()

# Sử dụng hàm để lấy số lượng sách đang mượn của thành viên có account_id là 'your_member_account_id'
member_account_id = 'your_member_account_id'
borrowed_books_count = count_borrowed_books(member_account_id)
print("Number of borrowed books:", borrowed_books_count)

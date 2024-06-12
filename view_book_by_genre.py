import tkinter as tk
from tkinter import ttk
import psycopg2

def search_books_by_genre():
    # Xóa tất cả các hàng trong cây trước khi thêm kết quả tìm kiếm mới
    for row in tree.get_children():
        tree.delete(row)

    # Lấy thể loại sách từ ô nhập liệu
    genre_name = entry_genre.get()

    try:
        conn = psycopg2.connect("dbname=kkk user=postgres password=236204")
        cursor = conn.cursor()

        # Tìm kiếm sách theo thể loại
        cursor.execute("SELECT * FROM Books b JOIN Book_Genre bg ON b.book_id = bg.book_id JOIN Genres g ON bg.genre_id = g.genre_id WHERE g.genre_name = %s", (genre_name,))
        books = cursor.fetchall()

        # Hiển thị kết quả tìm kiếm trên cây
        for book in books:
            tree.insert('', 'end', values=book)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if conn:
            cursor.close()
            conn.close()

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Search Books by Genre")

# Nhãn và ô nhập liệu cho thể loại sách
label_genre = tk.Label(root, text="Genre:")
label_genre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_genre = tk.Entry(root)
entry_genre.grid(row=0, column=1, padx=5, pady=5)
entry_genre.focus()  # Đặt con trỏ vào ô nhập liệu thể loại sách mặc định

# Nút tìm kiếm
btn_search = tk.Button(root, text="Search", command=search_books_by_genre)
btn_search.grid(row=0, column=2, padx=5, pady=5)

# Tạo cây để hiển thị kết quả tìm kiếm
tree = ttk.Treeview(root, columns=("Book ID", "Book Name", "Genre", "Publisher", "Publication Year", "Available", "Quantity", "Price"))
tree.heading("#0", text="Index")
tree.column("#0", width=50)
tree.heading("Book ID", text="Book ID")
tree.heading("Book Name", text="Book Name")
tree.heading("Genre", text="Genre")
tree.heading("Publisher", text="Publisher")
tree.heading("Publication Year", text="Publication Year")
tree.heading("Available", text="Available")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")
tree.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()

print("Manajemen Perpustakaan Kelompok 48")
# Modul 1-2: Variabel dan Tipe Data
books = [
    {"id": 1, "title": "Python Dasar", "author": "John Doe", "available": True},
    {"id": 2, "title": "Algoritma", "author": "Jane Smith", "available": False},
    {"id": 3, "title": "Kalkulus", "author": "Isaac Newton", "available": True}
    
]

# Modul 3: Function
# Function dengan return type dan berparameter
def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None

# Function non-return type, tanpa parameter
def display_welcome_message():
    print("=== Perpustakaan Sederhana ===")
    print("1. Cari Buku | 2. Buku Tersedia | 3. Tambah Buku | 4. Keluar")

# Modul 4: Class dan Method
class Library:
    def __init__(self, book_list):
        self.books = book_list

    # Method non-return type, berparameter
    def add_book(self, title, author):
        if not title or not author:
            print("Error: Judul dan author wajib!")
            return
        new_book = {"id": len(self.books) + 1, "title": title, "author": author, "available": True}
        self.books.append(new_book)
        print(f"Buku '{title}' ditambahkan!")

    # Method dengan return type, tanpa parameter
    def get_available_books(self):
        available = []
        for book in self.books:
            if book["available"]:
                available.append(book)
        return available

# Program Utama: Perulangan while dan pengkondisian if-elif
def main():
    library = Library(books)
    display_welcome_message()
    
    while True:
        choice = input("\nPilih (1-4): ").strip()
        
        if choice == "1":
            title = input("Judul buku: ").strip()
            found = search_book(title)
            if found:
                status = "Tersedia" if found["available"] else "Dipinjam"
                print(f"{found['title']} oleh {found['author']} - {status}")
            else:
                print("Buku tidak ditemukan!")
        
        elif choice == "2":
            avail = library.get_available_books()
            if avail:
                print("\nBuku Tersedia:")
                for book in avail:
                    print(f"- {book['title']} oleh {book['author']}")
            else:
                print("Tidak ada buku tersedia.")
        
        elif choice == "3":
            title = input("Judul baru: ").strip()
            author = input("Author: ").strip()
            library.add_book(title, author)
        
        elif choice == "4":
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan salah!")

if __name__ == "__main__":
    main()

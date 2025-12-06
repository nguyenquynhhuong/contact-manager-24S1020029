phonebook = []

def add_contact():
    name = input("Nhập tên: ")
    phone = input("Nhập số điện thoại: ")

    phonebook.append({
        'name': name,
        'phone': phone
    })

    print("✔ Đã thêm liên hệ.")


def view_contacts():
    if not phonebook:
        print("Danh bạ trống.")
        return

    print("\n--- DANH BẠ ---")
    for i, c in enumerate(phonebook, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")


def search_contact():
    pass

def main():
    while True:
        print("\n--- DANH BẠ ĐIỆN THOẠI ---")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Tìm kiếm")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

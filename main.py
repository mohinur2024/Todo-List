from database import create_table
from models import add_task, list_tasks, mark_done, delete_task
from tabulate import tabulate

def show_tasks():
    tasks = list_tasks()
    if not tasks:
        print("📝 Hozircha hech qanday vazifa yo‘q.")
        return
    table = [[t[0], t[1], "✅" if t[2] else "❌"] for t in tasks]
    print(tabulate(table, headers=["ID", "Vazifa", "Holat"]))

def main():
    create_table()
    while True:
        print("\n=== TODO LIST ===")
        print("1. Vazifa qo‘shish")
        print("2. Vazifalarni ko‘rish")
        print("3. Vazifani bajarildi deb belgilash")
        print("4. Vazifani o‘chirish")
        print("5. Chiqish")

        choice = input("Tanlov: ")

        if choice == "1":
            title = input("Vazifa nomi: ")
            add_task(title)
            print("✅ Vazifa qo‘shildi.")
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            task_id = input("Bajarilgan vazifa ID sini kiriting: ")
            mark_done(task_id)
            print("✅ Vazifa bajarildi.")
        elif choice == "4":
            task_id = input("O‘chirish uchun ID: ")
            delete_task(task_id)
            print("🗑️ Vazifa o‘chirildi.")
        elif choice == "5":
            print("Chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov.")

if __name__ == "__main__":
    main()

# file: todo.py
# To-do list sederhana (simpan di todos.txt)

FILENAME = "todos.txt"

def load_todos():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        return []

def save_todos(todos):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for t in todos:
            f.write(t + "\n")

def show_todos(todos):
    if not todos:
        print("Tidak ada tugas.")
    else:
        for i, t in enumerate(todos, start=1):
            print(f"{i}. {t}")

def main():
    todos = load_todos()
    while True:
        print("\n=== To-Do List ===")
        show_todos(todos)
        print("\nPerintah: add, done <no>, del <no>, quit")
        cmd = input("> ").strip()
        if cmd == "quit":
            save_todos(todos)
            print("Tersimpan. Keluar.")
            break
        elif cmd == "add":
            text = input("Tugas baru: ").strip()
            if text:
                todos.append(text)
                save_todos(todos)
                print("Ditambahkan.")
        elif cmd.startswith("done ") or cmd.startswith("del "):
            parts = cmd.split()
            if len(parts) == 2 and parts[1].isdigit():
                idx = int(parts[1]) - 1
                if 0 <= idx < len(todos):
                    removed = todos.pop(idx)
                    save_todos(todos)
                    print(f"Terhapus: {removed}")
                else:
                    print("Nomor tugas tidak ada.")
            else:
                print("Perintah tidak valid.")
        else:
            print("Perintah tidak dikenali.")

if __name__ == "__main__":
    main()

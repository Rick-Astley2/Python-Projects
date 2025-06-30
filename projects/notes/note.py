from csv import DictReader, DictWriter
import os

FILENAME = "note.csv"

def main():
    user_input = input("Type 'w' to write a note or 'r' to read notes: ").strip().lower()
    if user_input == "w":
        add_note()
    elif user_input == "r":
        read_notes()
    else:
        print("Invalid input. Please type 'w' or 'r'.")

def read_notes():
    if not os.path.exists(FILENAME):
        print("No notes found.")
        return

    with open(FILENAME, "r", newline='') as notepad:
        reader = DictReader(notepad)
        print("\n--- Notes ---")
        for row in reader:
            print(f"- {row['note']}")

def add_note():
    user_note = input("Enter a note: ")
    
    file_exists = os.path.exists(FILENAME)
    is_empty = not file_exists or os.path.getsize(FILENAME) == 0

    with open(FILENAME, "a", newline='') as notepad:
        writer = DictWriter(notepad, fieldnames=["note"])
        if is_empty:
            writer.writeheader()
        writer.writerow({"note": user_note})
    
    print("Note added.")

if __name__ == "__main__":
    main()

from csv import DictReader, DictWriter

def main():
    user_input = input("Type w or r: ").strip().lower()
    if user_input == "w":
        add_note()
    if user_input == "r":
        read_notes()


def read_notes():
    with open("note.csv", "r") as notepad:
        reader = DictReader(notepad)
        for row in reader:
            for key, value in row.items():
                print(f"{key}: {value}")
    
        
def add_note():    
    with open("note.csv", "a") as notepad:
        user_note = input("Enter a note: ")
        writer = DictWriter(notepad, fieldnames=[user_note])
        print("Note added.")
        if notepad.tell() == 0:
            writer.writeheader()
        writer.writerow({user_note: user_note})
if __name__ == "__main__":
    main()
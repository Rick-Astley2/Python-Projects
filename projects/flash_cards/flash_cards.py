from csv import DictReader


def main():
    read_flash_cards()


def read_flash_cards():
    with open("cards.csv", "r") as cards:
        
        reader = DictReader(cards)
        for row in reader:
            front = row["Front"].strip()
            back = row["Back"].strip()
            
            print(f"\nQuestion: {front}")
            correct = False

            for i in range(3):
                answer = input("").title()
                if answer != back:
                    print("Incorrect")
                elif answer == back:
                    print("Correct")
                    correct = True
                    break
            if not correct:
                print(back)
                
                

if __name__ == "__main__":
    main()
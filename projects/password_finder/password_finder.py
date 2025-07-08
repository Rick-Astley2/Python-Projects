def main():
    while True:
        password = input("Enter a 4 digit password. ")
        if len(password) >= 5:
            print("To many digits")
        if len(password) <= 3:
            print("To few digits")
            
        try:
            password = int(password)
        except ValueError:
            print("invalid character")
        
        if password == password:
            break
            
    crack_code = 999
   
    while True:
        crack_code += 1
        if crack_code == password:
            print(f"{password} found your password")
            break
        elif crack_code != password:
            print(f"{crack_code}\r")
        

if __name__ == "__main__":
    main()
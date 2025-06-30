import time

def main():
    seconds = 0
    minutes = 0
    hours = 0
    while True:
        time.sleep(1)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")

if __name__ == "__main__":
    main()
import random
import time 

def main():
    symbol = ["🍒", "🍋", "🔔", "💎", "7️⃣", "🍀"]
    weight = [40, 25, 15, 10, 5, 5]
    start_time = time.time()
    
    while True:
        s1 = random.choices(symbol, weights=weight)[0]
        s2 = random.choices(symbol, weights=weight)[0]
        s3 = random.choices(symbol, weights=weight)[0]
        
        time.sleep(0.1)  # Sleep for 0.1 seconds to slow down the loop
        
        if s1 == s2 == s3:
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            print(f"\nJackpot! {s1}:{s2}:{s3}")
            print(f"Time taken: {elapsed_time:.2f} seconds")           
            break
        else:
            print(f"{s1}:{s2}:{s3}", end="\r")

if __name__ == "__main__":
    main()


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def menu():
    print("\n--- Temperature Converter ---")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Exit")
    
    choice = input("Enter choice (1-2): ")
    if choice == '2':
        return False
        
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"Result: {celsius_to_fahrenheit(c)}°F")
    else:
        print("Invalid Choice")
    return True

if __name__ == "__main__":
    running = True
    while running:
        running = menu()

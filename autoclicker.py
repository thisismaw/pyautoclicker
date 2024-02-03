import pyautogui
import time
import keyboard  # Import the keyboard library

def get_mouse_position():
    print("Hover the mouse to the desired position and press CTRL+C to save the position.")
    try:
        while True:
            x, y = pyautogui.position()
            print(f'X: {x} Y: {y}', end='\r')
            time.sleep(0.1)
    except KeyboardInterrupt:
        return (x, y)

def main():
    x, y = get_mouse_position()
    print(f"\nSelected Position: X: {x} Y: {y}")
    confirmation = input(f"Are you sure you want to start auto-clicking at this position? (yes/no): ")
    if confirmation.lower() == 'yes':
        print(f"Starting auto-clicker at X: {x} Y: {y}. Press 'q' to stop.")
        while True:
            pyautogui.click(x, y)
            time.sleep(0.01)  # Short delay to prevent CPU overuse
            if keyboard.is_pressed('q'):  # Check if 'q' is pressed
                print("\nAuto-clicking stopped by 'q' key.")
                break  # Exit the loop
    else:
        print("Auto-clicking canceled.")

if __name__ == "__main__":
    main()

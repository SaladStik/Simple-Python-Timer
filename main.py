import time
import tkinter

root = tkinter.Tk()
root.geometry("200x200")  # Set the window size to 200x200

root.title("Timer App")

label = tkinter.Label(root, font=50, text="Waiting for input")
timeLabel = tkinter.Label(root, font=15, text="Enter the time in seconds: ")
timeEntered = tkinter.Entry(root)

def start_timer():
    try:
        countdown_time = int(timeEntered.get())
        while countdown_time > 0:
            time.sleep(1)
            countdown_time -= 1
            label.config(text=str(countdown_time))
            root.update()
        label.config(text="Time's up!")
        root.bell()
    except ValueError:
        label.config(text="Please enter a valid number")

button = tkinter.Button(root, text="start timer", command=start_timer)

label.pack()
timeLabel.pack()
timeEntered.pack()
button.pack()
root.mainloop()

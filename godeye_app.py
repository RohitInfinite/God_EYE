import tkinter as tk
import threading
import godeye_core
import voice_activation

system_running = False


def start_system():

    global system_running

    if system_running:
        return

    system_running = True

    status_text.set("SYSTEM ONLINE")
    status_label.config(fg="#19e3ff")

    start_btn.config(bg="#1b2636", fg="#6c7a89")
    stop_btn.config(bg="#ff3b3b", fg="white")

    threading.Thread(target=godeye_core.main, daemon=True).start()


def stop_system():

    global system_running

    if not system_running:
        return

    system_running = False

    godeye_core.running = False

    status_text.set("SYSTEM OFFLINE")
    status_label.config(fg="#ff5b5b")

    start_btn.config(bg="#18d4d8", fg="black")
    stop_btn.config(bg="#1b2636", fg="#6c7a89")


root = tk.Tk()
root.title("GOD-EYE")
root.geometry("820x650")
root.configure(bg="#040c14")
root.resizable(False, False)

canvas = tk.Canvas(root, width=820, height=650, bg="#040c14", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# grid background
for x in range(0, 820, 40):
    canvas.create_line(x, 0, x, 650, fill="#071f22")

for y in range(0, 650, 40):
    canvas.create_line(0, y, 820, y, fill="#071f22")

# title
canvas.create_text(
    410,
    120,
    text="GOD-EYE",
    fill="#e8ffff",
    font=("Orbitron", 42, "bold")
)

canvas.create_text(
    410,
    160,
    text="AI ASSISTIVE NAVIGATION",
    fill="#19e3ff",
    font=("Orbitron", 12)
)

# status text
status_text = tk.StringVar()
status_text.set("SYSTEM OFFLINE")

status_label = tk.Label(
    root,
    textvariable=status_text,
    fg="#ff5b5b",
    bg="#0b1622",
    font=("Orbitron", 11),
    padx=20,
    pady=10
)

status_label.place(x=260, y=210, width=300)

# voice commands title
canvas.create_text(
    410,
    300,
    text="VOICE COMMANDS",
    fill="#6a7f97",
    font=("Orbitron", 10)
)

cmd1 = tk.Label(
    root,
    text='•   "Hey God"                Wake System',
    fg="#19e3ff",
    bg="#0b1622",
    font=("Consolas", 11),
    padx=20,
    pady=10
)

cmd1.place(x=240, y=330, width=340)

cmd2 = tk.Label(
    root,
    text='•   "Stop Navigation"        End Active Route',
    fg="#19e3ff",
    bg="#0b1622",
    font=("Consolas", 11),
    padx=20,
    pady=10
)

cmd2.place(x=240, y=380, width=340)

# buttons
start_btn = tk.Button(
    root,
    text="START SYSTEM",
    command=start_system,
    font=("Orbitron", 12, "bold"),
    bg="#18d4d8",
    fg="black",
    bd=0
)

start_btn.place(x=240, y=460, width=340, height=45)

stop_btn = tk.Button(
    root,
    text="STOP SYSTEM",
    command=stop_system,
    font=("Orbitron", 12, "bold"),
    bg="#1b2636",
    fg="#6c7a89",
    bd=0
)

stop_btn.place(x=240, y=520, width=340, height=45)


# voice listener thread
voice_activation.set_callbacks(start_system, stop_system)

threading.Thread(
    target=voice_activation.listen,
    daemon=True
).start()

root.mainloop()
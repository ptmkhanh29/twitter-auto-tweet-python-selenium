import tkinter as tk
import json
import subprocess

def create_app():
    root = tk.Tk()
    root.title("Twitter Account Information")

    labels = ["Username", "Password", "Start", "End", "Email", "Password Email", "Status", "Verify Phone Number"]

    accounts = ["Account 1", "Account 2", "Account 3"]
    for i in range(3):
        tk.Label(root, text=accounts[i]).grid(row=i+1, column=0)

    entry_widgets = {"Account 1": {}, "Account 2": {}, "Account 3": {}}

    for i, account in enumerate(accounts):
        row = i + 1
        for j, label in enumerate(labels):
            if i == 0:
                tk.Label(root, text=label).grid(row=0, column=j+1)
            entry = tk.Entry(root)
            entry.grid(row=row, column=j+1, padx=5, pady=5)
            entry_widgets[account][label.lower().replace(" ", "_")] = entry

    submit_button = tk.Button(root, text="Submit", command=lambda: submit_info(entry_widgets))
    submit_button.grid(row=4, columnspan=8, pady=20)

    root.mainloop()

def submit_info(entry_widgets):
    data = {"Account": []}
    for account, widgets in entry_widgets.items():
        account_data = {}
        is_filled = False
        for label, widget in widgets.items():
            value = widget.get()
            if value:
                is_filled = True
                if label in ["start", "end"]:
                    value = int(value) if value.isdigit() else 0
                account_data[label] = value
        
        if is_filled:
            data["Account"].append(account_data)

    if data["Account"]:
        json_data = json.dumps(data)
        
        print("Data is being sent to main.py")

        subprocess.run(["python", "main.py", json_data])
    else:
        print("No account information was entered.")

create_app()

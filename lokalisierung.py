import tkinter as tk
from tkinter import messagebox
import re


def process_variables():
    input_text = input_textbox.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Помилка", "Вставне значення")
        return

    try:

        lines = input_text.split("\n")
        results = []
        for line in lines:
            if ":" not in line:
                results.append(f"Помилка: '{line}' - неправильний формат")
                continue
                 
            #регулярні вирази
            match = re.match(r'^(.+?):\s*"(.*?)"$', line.strip())
            if not match:
                results.append(f"Помилка: '{line}' - неправильний формат (очікується `імя: \"значення\"`)")
                continue

            variable_name, variable_value = match.groups()
            choice = choice_var.get()
            if choice == '1':
                results.append(f"Назва перемінної: {variable_name.strip()}")
            elif choice == '2':
                results.append(f"Значення перемінної: {variable_value.strip()}")
            else:
                results.append("Помилка: неправильний вибір.")
        
        output_textbox.delete("1.0", tk.END)
        output_textbox.insert(tk.END, "\n".join(results))

    except Exception as e:
        messagebox.showerror("Помилка", f"Сталася помилка: {e}")


root = tk.Tk()
root.title("Обробка змінних")

tk.Label(root, text="Введи змінну (кожна з нового рядка, наприклад ua_country: \"abcd\"):").pack(pady=5)
input_textbox = tk.Text(root, height=10, width=50)
input_textbox.pack(pady=5)

choice_var = tk.StringVar(value='1')
tk.Label(root, text="Що потрібно вивести?").pack(pady=5)
tk.Radiobutton(root, text="Назва перемінної", variable=choice_var, value='1').pack()
tk.Radiobutton(root, text="Значення перемінної", variable=choice_var, value='2').pack()

# Кнопка 
tk.Button(root, text="Обробити", command=process_variables).pack(pady=10)

# результат
tk.Label(root, text="Результат:").pack(pady=5)
output_textbox = tk.Text(root, height=10, width=50, state=tk.NORMAL)
output_textbox.pack(pady=5)

root.mainloop()


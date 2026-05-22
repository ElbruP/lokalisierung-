import tkinter as tk
from tkinter import messagebox
import re


def process_variables():

    input_text = input_textbox.get("1.0", tk.END).strip()

    if not input_text:
        messagebox.showerror(
            "Помилка",
            "Вставне значення"
        )
        return

    try:

        lines = input_text.split("\n")

        results = []

        for line in lines:

            if ":" not in line:

                results.append(
                    f"Помилка: '{line}' - неправильний формат"
                )

                continue

            match = re.match(
                r'^(.+?):\s*"(.*?)"$',
                line.strip()
            )

            if not match:

                results.append(
                    f"Помилка: '{line}' - неправильний формат"
                )

                continue

            variable_name, variable_value = match.groups()

            choice = choice_var.get()

            if choice == '1':

                results.append(
                    f"Назва перемінної: {variable_name.strip()}"
                )

            elif choice == '2':

                results.append(
                    f"Значення перемінної: {variable_value.strip()}"
                )

            else:

                results.append(
                    "Помилка: неправильний вибір."
                )

        output_textbox.delete("1.0", tk.END)

        output_textbox.insert(
            tk.END,
            "\n".join(results)
        )

    except Exception as e:

        messagebox.showerror(
            "Помилка",
            f"Сталася помилка: {e}"
        )



def generate_template():

    template = template_textbox.get(
        "1.0",
        tk.END
    ).strip()

    replace_text = replace_textbox.get().strip()

    values_text = values_textbox.get(
        "1.0",
        tk.END
    ).strip()

    if not template:

        messagebox.showerror(
            "Помилка",
            "Встав шаблон"
        )

        return

    if not replace_text:

        messagebox.showerror(
            "Помилка",
            "Встав текст для заміни"
        )

        return

    if not values_text:

        messagebox.showerror(
            "Помилка",
            "Встав значення"
        )

        return

    lines = [
        line.strip()
        for line in values_text.splitlines()
        if line.strip()
    ]

    result = ""

    for line in lines:

        generated = template.replace(
            replace_text,
            line
        )

        result += generated + "\n\n"

    template_output_textbox.delete(
        "1.0",
        tk.END
    )

    template_output_textbox.insert(
        tk.END,
        result
    )



def copy_template_result():

    result = template_output_textbox.get(
        "1.0",
        tk.END
    ).strip()

    if not result:

        messagebox.showwarning(
            "Увага",
            "Немає результату"
        )

        return

    root.clipboard_clear()

    root.clipboard_append(result)

    messagebox.showinfo(
        "Успіх",
        "Результат скопійовано"
    )



root = tk.Tk()

root.title(
    "Universal Template Replacer"
)

root.geometry("1100x950")

root.configure(bg="#f5f5f5")



title_label = tk.Label(
    root,
    text="Обробка змінних + Генератор шаблонів",
    font=("Arial", 18, "bold"),
    bg="#f5f5f5"
)

title_label.pack(pady=15)



# ==========================================
# СТАРА СИСТЕМА
# ==========================================

old_system_label = tk.Label(
    root,
    text="Стара система обробки змінних",
    font=("Arial", 14, "bold"),
    bg="#f5f5f5"
)

old_system_label.pack(pady=10)



tk.Label(
    root,
    text='Введи змінну (наприклад ua_country: "abcd")',
    bg="#f5f5f5"
).pack(pady=5)



input_textbox = tk.Text(
    root,
    height=10,
    width=120,
    font=("Consolas", 11)
)

input_textbox.pack(pady=5)



choice_var = tk.StringVar(value='1')



tk.Label(
    root,
    text="Що потрібно вивести?",
    bg="#f5f5f5"
).pack(pady=5)



radio_frame = tk.Frame(
    root,
    bg="#f5f5f5"
)

radio_frame.pack()



tk.Radiobutton(
    radio_frame,
    text="Назва перемінної",
    variable=choice_var,
    value='1',
    bg="#f5f5f5"
).pack(side=tk.LEFT, padx=10)



tk.Radiobutton(
    radio_frame,
    text="Значення перемінної",
    variable=choice_var,
    value='2',
    bg="#f5f5f5"
).pack(side=tk.LEFT, padx=10)



tk.Button(
    root,
    text="Обробити змінні",
    command=process_variables,
    bg="#2d89ef",
    fg="white",
    width=30,
    height=2
).pack(pady=10)



tk.Label(
    root,
    text="Результат:",
    font=("Arial", 12, "bold"),
    bg="#f5f5f5"
).pack(pady=5)



output_textbox = tk.Text(
    root,
    height=10,
    width=120,
    font=("Consolas", 11)
)

output_textbox.pack(pady=5)



# ==========================================
# НОВА СИСТЕМА
# ==========================================

new_system_label = tk.Label(
    root,
    text="Універсальний генератор шаблонів",
    font=("Arial", 14, "bold"),
    bg="#f5f5f5"
)

new_system_label.pack(pady=20)



tk.Label(
    root,
    text="Шаблон:",
    bg="#f5f5f5"
).pack(pady=5)



template_textbox = tk.Text(
    root,
    height=12,
    width=120,
    font=("Consolas", 11)
)

template_textbox.pack(pady=5)



template_textbox.insert(
    tk.END,
    """ua-country {
c:TEXT
localization_key = ua_country_TEXT
}"""
)



tk.Label(
    root,
    text="Який текст замінювати:",
    bg="#f5f5f5"
).pack(pady=5)



replace_textbox = tk.Entry(
    root,
    width=80,
    font=("Consolas", 11)
)

replace_textbox.pack(pady=5)



replace_textbox.insert(0, "TEXT")



tk.Label(
    root,
    text="Значення (кожне з нового рядка):",
    bg="#f5f5f5"
).pack(pady=5)



values_textbox = tk.Text(
    root,
    height=10,
    width=120,
    font=("Consolas", 11)
)

values_textbox.pack(pady=5)



values_textbox.insert(
    tk.END,
    "PRC\nGBR\nHND"
)



button_frame = tk.Frame(
    root,
    bg="#f5f5f5"
)

button_frame.pack(pady=10)



tk.Button(
    button_frame,
    text="Згенерувати шаблон",
    command=generate_template,
    bg="#2d89ef",
    fg="white",
    width=30,
    height=2
).pack(side=tk.LEFT, padx=5)



tk.Button(
    button_frame,
    text="Копіювати результат",
    command=copy_template_result,
    bg="#2d89ef",
    fg="white",
    width=30,
    height=2
).pack(side=tk.LEFT, padx=5)



tk.Label(
    root,
    text="Результат шаблону:",
    font=("Arial", 12, "bold"),
    bg="#f5f5f5"
).pack(pady=5)



template_output_textbox = tk.Text(
    root,
    height=15,
    width=120,
    font=("Consolas", 11)
)

template_output_textbox.pack(pady=5)



root.mainloop()


import tkinter as tk
from tkinter import messagebox


def generate_template():

    template = template_textbox.get("1.0", tk.END).strip()

    replace_text = replace_textbox.get().strip()

    input_text = values_textbox.get("1.0", tk.END).strip()

    if not template:
        messagebox.showerror("Помилка", "Встав шаблон")
        return

    if not replace_text:
        messagebox.showerror(
            "Помилка",
            "Встав текст для заміни"
        )
        return

    if not input_text:
        messagebox.showerror(
            "Помилка",
            "Встав значення"
        )
        return

    lines = [
        line.strip()
        for line in input_text.splitlines()
        if line.strip()
    ]

    result = ""

    for line in lines:

        generated = template.replace(
            replace_text,
            line
        )

        result += generated + "\n\n"

    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, result)


def process_variables():

    input_text = values_textbox.get(
        "1.0",
        tk.END
    ).strip()

    if not input_text:
        messagebox.showerror(
            "Помилка",
            "Встав значення"
        )
        return

    lines = input_text.split("\n")

    results = []

    choice = choice_var.get()

    for line in lines:

        if ":" not in line:

            results.append(
                f"Помилка: '{line}' - неправильний формат"
            )

            continue

        try:

            variable_name = line.split(":")[0]

            variable_value = (
                line.split(":")[1]
                .strip()
                .replace('"', '')
            )

            if choice == "1":

                results.append(
                    variable_name.strip()
                )

            elif choice == "2":

                results.append(
                    variable_value.strip()
                )

        except:

            results.append(
                f"Помилка: '{line}'"
            )

    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(
        tk.END,
        "\n".join(results)
    )


def copy_result():

    result = output_textbox.get(
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


def clear_all():

    template_textbox.delete("1.0", tk.END)

    replace_textbox.delete(0, tk.END)

    values_textbox.delete("1.0", tk.END)

    output_textbox.delete("1.0", tk.END)


root = tk.Tk()

root.title(
    "Universal Template Replacer"
)

root.geometry("1000x850")

root.configure(bg="#f5f5f5")

title_label = tk.Label(
    root,
    text="Універсальний генератор шаблонів",
    font=("Arial", 18, "bold"),
    bg="#f5f5f5"
)

title_label.pack(pady=15)

template_label = tk.Label(
    root,
    text="1. Шаблон",
    font=("Arial", 12, "bold"),
    bg="#f5f5f5"
)

template_label.pack()

template_textbox = tk.Text(
    root,
    height=12,
    width=110,
    font=("Consolas", 11)
)

template_textbox.pack(pady=8)

template_textbox.insert(
    tk.END,
    """ua-country {
c:TEXT
localization_key = ua_country_TEXT
}"""
)

replace_label = tk.Label(
    root,
    text="2. Який текст замінювати",
    font=("Arial", 12, "bold"),
    bg="#f5f5f5"
)

replace_label.pack()

replace_textbox = tk.Entry(
    root,
    width=80,
    font=("Consolas", 11)
)

replace_textbox.pack(pady=8)

replace_textbox.insert(0, "TEXT")

values_label = tk.Label(
    root,
    text="3. Значення",
    font=("Arial", 12, "bold"),
    bg="#f5f5f5"
)

values_label.pack()

values_textbox = tk.Text(
    root,
    height=10,
    width=110,
    font=("Consolas", 11)
)

values_textbox.pack(pady=8)

values_textbox.insert(
    tk.END,
    "PRC\nGBR\nHND"
)

variables_label = tk.Label(
    root,
    text="4. Обробка змінних",
    font=("Arial", 12, "bold"),
    bg="#f5f5f5"
)

variables_label.pack(pady=10)

choice_var = tk.StringVar(value="1")

radio_frame = tk.Frame(
    root,
    bg="#f5f5f5"
)

radio_frame.pack()

tk.Radiobutton(
    radio_frame,
    text="Назва перемінної",
    variable=choice_var,
    value="1",
    bg="#f5f5f5"
).pack(side=tk.LEFT, padx=10)

tk.Radiobutton(
    radio_frame,
    text="Значення перемінної",
    variable=choice_var,
    value="2",
    bg="#f5f5f5"
).pack(side=tk.LEFT, padx=10)

button_frame = tk.Frame(
    root,
    bg="#f5f5f5"
)

button_frame.pack(pady=15)

generate_button = tk.Button(
    button_frame,
    text="Згенерувати шаблон",
    command=generate_template,
    bg="#2d89ef",
    fg="white",
    width=25,
    height=2
)

generate_button.pack(
    side=tk.LEFT,
    padx=5
)

process_button = tk.Button(
    button_frame,
    text="Обробити змінні",
    command=process_variables,
    bg="#2d89ef",
    fg="white",
    width=25,
    height=2
)

process_button.pack(
    side=tk.LEFT,
    padx=5
)

copy_button = tk.Button(
    button_frame,
    text="Копіювати результат",
    command=copy_result,
    bg="#2d89ef",
    fg="white",
    width=25,
    height=2
)

copy_button.pack(
    side=tk.LEFT,
    padx=5
)

clear_button = tk.Button(
    button_frame,
    text="Очистити",
    command=clear_all,
    bg="#d9534f",
    fg="white",
    width=20,
    height=2
)

clear_button.pack(
    side=tk.LEFT,
    padx=5
)

result_label = tk.Label(
    root,
    text="Результат",
    font=("Arial", 12, "bold"),
    bg="#f5f5f5"
)

result_label.pack(pady=10)

output_textbox = tk.Text(
    root,
    height=15,
    width=110,
    font=("Consolas", 11)
)

output_textbox.pack(pady=10)

root.mainloop()


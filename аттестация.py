import tkinter as tk
import random
import string

def generate_password():
    """Генерирует пароль на основе выбранных пользователем параметров."""
    try:
        length = int(length_entry.get())
    except ValueError:
        password_label.config(text="Введите корректную длину")
        return

    chars = ""
    if use_letters.get():
        chars += string.ascii_letters
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation

    if not chars:
        password_label.config(text="Выберите хотя бы один тип символов")
        return

    if length <= 0:
        password_label.config(text="Длина должна быть положительной")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_label.config(text=f"Пароль: {password}")

def copy_to_clipboard():
    """Копирует сгенерированный пароль в буфер обмена."""
    password_text = password_label.cget("text")
    if password_text.startswith("Пароль: "):
        password = password_text[8:]
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update() # Важно для корректного копирования

# Создание главного окна
root = tk.Tk()
root.title("Генератор паролей")

# Поле ввода длины
tk.Label(root, text="Длина пароля:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
length_entry = tk.Entry(root)
length_entry.insert(0, "12") # Значение по умолчанию
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Флажки для выбора типа пароля
use_letters = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Буквы", variable=use_letters).grid(row=1, column=0, columnspan=2, padx=5, pady=2, sticky="w")
tk.Checkbutton(root, text="Цифры", variable=use_digits).grid(row=2, column=0, columnspan=2, padx=5, pady=2, sticky="w")
tk.Checkbutton(root, text="Символы", variable=use_symbols).grid(row=3, column=0, columnspan=2, padx=5, pady=2, sticky="w")

# Кнопка генерации
generate_button = tk.Button(root, text="Сгенерировать", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

# Метка для вывода пароля
password_label = tk.Label(root, text="Введите длину и нажмите 'Сгенерировать'")
password_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Кнопка копирования (по желанию)
copy_button = tk.Button(root, text="Копировать", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Запуск главного цикла Tkinter
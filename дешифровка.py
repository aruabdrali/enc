import tkinter as tk
from tkinter import messagebox

def read_first_10_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    sentences = content.split('. ')
    first_10_sentences = sentences[:10]
    first_10_sentences = [sentence.strip() for sentence in first_10_sentences if sentence.strip()]

    return '\n'.join(first_10_sentences)

def encrypt_text():
    text = entry_text.get()
    old_alphabet = entry_old_alphabet.get()
    new_alphabet = entry_new_alphabet.get()

    if len(old_alphabet) != len(new_alphabet):
        messagebox.showerror("Ошибка", "Количество букв в старом и новом алфавитах не совпадает")
    else:
        translation_table = str.maketrans(old_alphabet, new_alphabet)
        encrypted_text = text.translate(translation_table)
        messagebox.showinfo("Расшифрованный текст", encrypted_text)


# Создание главного окна
window = tk.Tk()
window.title("Моя программа")

# Создание элементов интерфейса
label_filepath = tk.Label(window, text="Путь к файлу:")
entry_filepath = tk.Entry(window, width=30)
button_read = tk.Button(window, text="Прочитать предложения", command=lambda: entry_text.insert(tk.END, read_first_10_sentences(entry_filepath.get())))

label_text = tk.Label(window, text="Отрывок шифр-текста:")
entry_text = tk.Entry(window, width=30)
label_old_alphabet = tk.Label(window, text="Старый алфавит:")
entry_old_alphabet = tk.Entry(window, width=30)
label_new_alphabet = tk.Label(window, text="Новый алфавит:")
entry_new_alphabet = tk.Entry(window, width=30)
button_encrypt = tk.Button(window, text="Расшифровать текст", command=encrypt_text)

# Размещение элементов в окне
label_filepath.pack()
entry_filepath.pack()
button_read.pack()

label_text.pack()
entry_text.pack()
label_old_alphabet.pack()
entry_old_alphabet.pack()
label_new_alphabet.pack()
entry_new_alphabet.pack()
button_encrypt.pack()

# Запуск главного цикла
window.mainloop()

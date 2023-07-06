import tkinter as tk
import matplotlib.pyplot as plt
import string

# Создаем словарь для шифрования
alphabet = {
    'а': 'б', 'б': 'в', 'в': 'г', 'г': 'д', 'д': 'е', 'е': 'ё', 'ж': 'з',
    'з': 'и', 'и': 'й', 'й': 'к', 'к': 'л', 'л': 'м', 'м': 'н', 'н': 'о',
    'о': 'п', 'п': 'р', 'р': 'с', 'с': 'т', 'т': 'у', 'у': 'ф', 'ф': 'х',
    'х': 'ц', 'ц': 'ч', 'ч': 'ш', 'ш': 'щ', 'щ': 'ъ', 'ы': 'ь', 'ь': 'э',
    'э': 'ю', 'ю': 'я', 'я': 'а'
}

# Функция для шифрования сообщения и сохранения в файл
def encrypt_and_save():
    original_message = input_text.get("1.0", "end-1c")  # Получаем текст из текстового поля
    encrypted_message = ''
    for char in original_message:
        if char.lower() in alphabet:
            encrypted_message += alphabet[char.lower()]
        else:
            encrypted_message += char
    
    # Сохраняем зашифрованное сообщение в файл
    filename = "encrypted_message.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(encrypted_message)
    
    # Выводим зашифрованное сообщение в текстовое поле вывода
    output_text.delete("1.0", "end")  # Очищаем текстовое поле вывода
    output_text.insert("1.0", encrypted_message)  # Выводим зашифрованное сообщение

# Функция для анализа частоты встречаемости букв в зашифрованном тексте
def analyze_frequency():
    data = output_text.get("1.0", "end-1c")  # Получаем текст из текстового поля вывода

    data = data.lower()

    freq = {}
    for char in ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'):
        freq[char] = 0

    for char in data:
        if char in freq:
            freq[char] += 1

    sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=False))

    output_text.delete("1.0", "end")  # Очищаем текстовое поле вывода

    output_text.insert("1.0", "Частота встречаемости каждой буквы в зашифрованном тексте:\n")
    for char in sorted_freq:
        output_text.insert("end", f"{char}: {sorted_freq[char]}\n")

    plt.bar(sorted_freq.keys(), sorted_freq.values())
    plt.xlabel("Буквы")
    plt.ylabel("Частота встречаемости")
    plt.title("График частоты встречаемости каждой буквы в зашифрованном тексте")
    plt.show()

# Создаем графическое окно
window = tk.Tk()
window.title("Шифрование и анализ частоты")
window.geometry("400x400")

# Создаем текстовое поле для ввода
input_text = tk.Text(window, height=5, width=50)
input_text.pack()

# Создаем кнопку для шифрования и сохранения
encrypt_button = tk.Button(window, text="Зашифровать и Сохранить", command=encrypt_and_save)
encrypt_button.pack()

# Создаем кнопку для анализа частоты
frequency_button = tk.Button(window, text="Анализ частоты", command=analyze_frequency)
frequency_button.pack()

# Создаем текстовое поле для вывода
output_text = tk.Text(window, height=10, width=50)
output_text.pack()

# Запускаем главный цикл обработки событий
window.mainloop()

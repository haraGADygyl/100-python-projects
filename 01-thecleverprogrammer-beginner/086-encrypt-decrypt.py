from tkinter import messagebox, simpledialog, Tk


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    even_letters = []

    for i in range(len(message)):
        if is_even(i):
            even_letters.append(message[i])

    return even_letters


def get_odd_letters(message):
    odd_letters = []

    for i in range(len(message)):
        if not is_even(i):
            odd_letters.append(message[i])

    return odd_letters


def swap_letters(message):
    swapped_letters = []

    if not is_even(len(message)):
        message += 'x'


    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    for i in range(len(message) // 2):
        swapped_letters.append(odd_letters[i])
        swapped_letters.append(even_letters[i])

    return ''.join(swapped_letters)


def get_task():
    return simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')


def get_message():
    return simpledialog.askstring('Message', 'Enter your message')


root = Tk()
while True:
    task = get_task()

    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Encrypted message is', encrypted)

    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Decrypted message is', decrypted)
    else:
        break

root.mainloop()

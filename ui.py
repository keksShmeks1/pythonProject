import tkinter as tk

from createTable import create_schedule_table


class AddressListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Список адресов")

        # Список адресов
        self.addresses = []

        # Метка
        self.label = tk.Label(self.master, text="Введите адрес:")
        self.label.pack()

        # Поле ввода
        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack()

        # Кнопка добавления адреса
        self.add_button = tk.Button(self.master, text="Добавить", command=self.add_address)
        self.add_button.pack()

        # Кнопка создания таблицы
        self.create_table_button = tk.Button(self.master, text="Создать таблицу", command=self.create_table)
        self.create_table_button.pack()

        # Список адресов
        self.listbox = tk.Listbox(self.master, width=60)
        self.listbox.pack()

        # Кнопка очистки списка
        self.clear_button = tk.Button(self.master, text="Очистить", command=self.clear_addresses)
        self.clear_button.pack()

    def add_address(self):
        address = self.entry.get()
        self.addresses.append(address)
        self.listbox.insert(tk.END, address)
        self.entry.delete(0, tk.END)

    def clear_addresses(self):
        self.addresses = []
        self.listbox.delete(0, tk.END)

    def create_table(self):
        create_schedule_table(self.addresses)



if __name__ == "__main__":
    root = tk.Tk()
    app = AddressListGUI(root)
    root.mainloop()
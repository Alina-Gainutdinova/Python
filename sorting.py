import tkinter as tk


root = tk.Tk()
root.title('Программа сортировки алгоритма')
root.geometry('800x600')

entry = tk.Entry(root, width=7)
entry.grid(row=1, column=1)

entry_widgets = []


def create_cells():
    text = entry.get()
    count = int(text)
    # current_column = 2
    for i in range(count):
        entry_widget = tk.Entry(root, justify='center', width=6)
        entry_widget.grid(row=3, column=i, padx=0, pady=0, sticky='nw')
        entry_widgets.append(entry_widget)
        # current_column += 1


choice_cell_count = tk.Label(root, text='Введите количество ячееек: ')
choice_cell_count.grid(row=1, column=0, sticky='w')


btn1 = tk.Button(root, text='Enter', command=create_cells)
btn1.grid(row=1, column=2, sticky='e', padx=3, pady=1)


root.mainloop()

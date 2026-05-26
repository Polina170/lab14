import tkinter as tk
class IceCreamStand:
    def __init__(self):
        self.flavors = ["Ванильное", "Шоколадное", "Фисташковое"]
    def add(self, f):
        if f and f not in self.flavors:
            self.flavors.append(f); return True
            return False
    def remove(self, f):
        if f in self.flavors:
            self.flavors.remove(f); return True
            return False
def update():
    listbox.delete(0, tk.END)
    [listbox.insert(tk.END, f) for f in shop.flavors]
def add_f():
    if shop.add(entry.get().strip()):
        update(); entry.delete(0, tk.END)
def rem_f():
    if listbox.curselection():
        shop.remove(listbox.get(listbox.curselection()[0])); update()
root = tk.Tk()
root.title("Мороженое")
listbox = tk.Listbox(root); listbox.pack()
entry = tk.Entry(root); entry.pack()
tk.Button(root, text="+", command=add_f).pack()
tk.Button(root, text="-", command=rem_f).pack()
shop = IceCreamStand()
update()
root.mainloop()
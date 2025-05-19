import tkinter as tk
from tkinter import ttk
import pickle

# Load model and data
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def recommend_book_gui():
    selected = book_var.get()
    book_id = list(book_names).index(selected)
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    result.delete(0, tk.END)
    for i in suggestions[0]:
        book = book_names[i]
        if book != selected:
            result.insert(tk.END, book)

# GUI layout
root = tk.Tk()
root.title("Book Recommender")

book_var = tk.StringVar()
book_menu = ttk.Combobox(root, textvariable=book_var, values=list(book_names), width=60)
book_menu.pack(pady=10)

btn = tk.Button(root, text="Get Recommendations", command=recommend_book_gui)
btn.pack(pady=5)

result = tk.Listbox(root, width=80, height=10)
result.pack(pady=10)

root.mainloop()

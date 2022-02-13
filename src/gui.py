import tkinter as tk

ingredients = ["milk", "rabbit", "juice", "calamari", "hot dog", "orange", "penis"]
window = None
sv = None

# load all ingredient buttons
def loadIngredientButtons():
    for ing in ingredients:
        pass
# on text box change
def textBoxChanged(a, b, c):
    # update ingredients list
    loadIngredientButtons()

def loadIngredientScreen():
    sv.trace_add("write", textBoxChanged)
    searchBar = tk.Entry(window, width=20, bg="white", fg="black", textvariable=sv)
    searchBar.pack()


if __name__ == "__main__":
    window = tk.Tk()
    sv = tk.StringVar()
    window.title("Recipe Recommender 1.0")
    window.geometry("500x800")
    loadIngredientScreen()
    window.mainloop()






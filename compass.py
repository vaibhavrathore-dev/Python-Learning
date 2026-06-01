import tkinter as tk
from PIL import Image, ImageTk

# direction → angle mapping
directions = {
    "N": 0,
    "E": -90,
    "S": -180,
    "W": -270,
    "NE": -45,
    "NW": 45,
    "SE": -135,
    "SW": 135
}

class CompassApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compass App")

        # load image
        self.original_img = Image.open("compass.jpg")
        self.img = ImageTk.PhotoImage(self.original_img)

        self.label = tk.Label(root, image=self.img)
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.btn = tk.Button(root, text="Rotate", command=self.rotate)
        self.btn.pack()

    def rotate(self):
        direction = self.entry.get().upper()

        if direction in directions:
            angle = directions[direction]

            rotated = self.original_img.rotate(angle)
            self.img = ImageTk.PhotoImage(rotated)

            self.label.config(image=self.img)
            self.label.image = self.img
        else:
            print("Invalid direction! Use N, S, E, W, NE, NW, SE, SW")

root = tk.Tk()
app = CompassApp(root)
root.mainloop()
import tkinter as tk

class DrawingApp:
    def __init__(self, master, scale=10):
        self.master = master
        master.title("Digit Recognition")

        self.scale = scale
        self.size = 28
        self.canvas = tk.Canvas(master, bg="black", width=self.size*self.scale, height=self.size*self.scale)
        self.canvas.pack()

        self.old_x, self.old_y = None, None
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.end_draw)

    def start_draw(self, event):
        self.old_x, self.old_y = event.x, event.y

    def draw(self, event):
        if self.old_x is not None and self.old_y is not None:
            # Draw a thick line for visibility
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, 
                                    width=self.scale * 2, fill="white", capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x, self.old_y = event.x, event.y

    def end_draw(self, event):
        self.old_x, self.old_y = None, None

root = tk.Tk()
app = DrawingApp(root, scale=10)  # visually 280x280, but conceptually 28x28
root.mainloop()
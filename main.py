from tkinter import *
from mainWindow import *
import mainWindow
from mainFunction import calculation_value
import fileManager
from fileManager import TrajectoryObject

window = Tk
data = []
displayedItems = []


def remove_item_and_file(item: TrajectoryObject):
    global data
    if item_exists(item):
        remove_item(item)
    fileManager.remove_item_file(item)


def item_exists(item: TrajectoryObject):
    global displayedItems
    for displayed in displayedItems:
        if displayed.timeStamp == item.timeStamp:
            return True
    return False


def remove_item(item: TrajectoryObject):
    global displayedItems
    index = 0
    found = False
    for displayed in displayedItems:
        if displayed.timeStamp == item.timeStamp:
            found = True
            break
        index = index + 1
    if found:
        displayedItems.pop(index)


def save():
    global data
    h = float(mainWindow.input_1.get())
    V = float(mainWindow.input_2.get())
    a = float(mainWindow.input_4.get())
    g = float(mainWindow.input_3.get())
    step = float(mainWindow.input_5.get())
    newObject = fileManager.write_to_file(h, V, g, a, step)
    data.append(newObject)
    mainWindow.populate_save_points(data)


def calculate():
    item: TrajectoryObject = TrajectoryObject()
    item.height = float(mainWindow.input_1.get())
    item.velocity = float(mainWindow.input_2.get())
    item.angle = float(mainWindow.input_4.get())
    item.gravity = float(mainWindow.input_3.get())
    item.step = float(mainWindow.input_5.get())
    calculate_item(item, True, 0)


def calculate_item(item: TrajectoryObject, isPrimary: bool, index: int):
    start = True
    x_val = []
    y_val = []
    x = 0
    y = 0
    while (y > 0 or start) and len(x_val) < 10000000:
        start = False
        y = calculation_value(x, item.height, item.velocity, item.angle, item.gravity)
        x_val.append(x)
        y_val.append(y)
        x = x + item.step
    mainWindow.set_values(x_val, y_val, isPrimary, index)


def main():
    global window, data
    data = fileManager.read_files()
    window = create_window()
    mainWindow.populate_save_points(data)
    window.mainloop()


if __name__ == "__main__":
    main()
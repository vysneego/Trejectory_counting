from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main import calculate, calculate_item, displayedItems, item_exists, remove_item, remove_item_and_file, save
from fileManager import TrajectoryObject
from random import randint
from functools import partial

from main import remove_item_and_file

colors = []

for i in range(200):
    colors.append('#%06X' % randint(0, 0xFFFFFF))

graphWindow = Frame
button_1 = Button
input_1 = Entry
input_2 = Entry
input_3 = Entry
input_4 = Entry
input_5 = Entry
graph = plt.Figure
graph_plot = plt.Figure().add_subplot(111)
bar1 = FigureCanvasTkAgg
graph_pl = FigureCanvasTkAgg
item = TrajectoryObject


def display_item(item: TrajectoryObject) -> None:
    """
    Displays the item on the graph
    """
    global displayedItems
    if item_exists(item):
        remove_item(item)
    else:
        displayedItems.append(item)
    redraw_lines()


def redraw_lines() -> None:
    """
    Redraws the lines on the graph
    """
    clear_bar_chart()
    create_graph()

    calculate()
    colorIndex = 1
    for item in displayedItems:
        colorIndex = colorIndex + 1
        calculate_item(item, False, colorIndex)

    finish_graph()


def reset() -> None:
    """
    Resets the inputs to default values
    """
    global input_1, input_2, input_3, input_4, input_5
    input_1.delete(0, END)
    input_2.delete(0, END)
    input_3.delete(0, END)
    input_4.delete(0, END)
    input_5.delete(0, END)

    input_1.insert(0, 20)
    input_2.insert(0, 20)
    input_3.insert(0, 9.8)
    input_4.insert(0, 30)
    input_5.insert(0, 0.1)


def load_item(item: TrajectoryObject) -> None:
    """
    Loads the item to the inputs
    """
    global input_1, input_2, input_3, input_4, input_5
    input_1.delete(0, END)
    input_2.delete(0, END)
    input_3.delete(0, END)
    input_4.delete(0, END)
    input_5.delete(0, END)

    input_1.insert(0, item.height)
    input_2.insert(0, item.velocity)
    input_3.insert(0, item.gravity)
    input_4.insert(0, item.angle)
    input_5.insert(0, item.step)


def populate_save_points(data) -> None:
    """
    Populates the list of saved points
    """
    global rightFrame

    for widget in rightFrame.winfo_children():
        widget.destroy()
        myList = Listbox(rightFrame)

    for item in data:
        pane = PanedWindow(myList)
        Checkbutton(pane, text='Display', variable=item, onvalue=1, offvalue=0,
                    command=partial(display_item, item)).grid(row=0, column=0)
        Button(pane, text='Load', padx=10, pady=10, command=partial(load_item, item)).grid(row=0, column=2)
        Label(pane, text=str(item.timeStamp), padx=10, pady=10).grid(row=0, column=1)
        Button(pane, text='Remove', padx=10, pady=10, command=partial(remove_item_and_file, item)).grid(row=0, column=3)
        pane.pack()

    myList.pack(side=LEFT, fill=BOTH)
    scroll = Scrollbar(rightFrame, command=myList.yview)
    scroll.pack(side=RIGHT, fill=Y)
    myList.configure(yscrollcommand=scroll.set)


def populate_inputs(window: Tk) -> None:
    """
    Populates the inputs
    """
    global input_1, input_2, input_3, input_4, input_5
    window.grid(row=0, column=0, padx=10, pady=10)
    Label(window, text="Height:", padx=10, pady=10).grid(row=0)
    Label(window, text="Velocity:", padx=10, pady=10).grid(row=1)
    Label(window, text="Gravity:", padx=10, pady=10).grid(row=2)
    Label(window, text="Degree:", padx=10, pady=10).grid(row=3)
    Label(window, text="Step:", padx=10, pady=10).grid(row=4)
    Label(window, text="m", padx=10, pady=10).grid(row=0, column=2)
    Label(window, text="m/s", padx=10, pady=10).grid(row=1, column=2)
    Label(window, text="m/s^2", padx=10, pady=10).grid(row=2, column=2)
    Label(window, text="degress", padx=10, pady=10).grid(row=3, column=2)
    input_1 = Entry(window)
    input_1.insert(0, 20)
    input_2 = Entry(window)
    input_2.insert(0, 20)
    input_3 = Entry(window)
    input_3.insert(0, 9.8)
    input_4 = Entry(window)
    input_4.insert(0, 30)
    input_5 = Entry(window)
    input_5.insert(0, 0.1)
    input_1.grid(row=0, column=1, padx=10, pady=10)
    input_2.grid(row=1, column=1, padx=10, pady=10)
    input_3.grid(row=2, column=1, padx=10, pady=10)
    input_4.grid(row=3, column=1, padx=10, pady=10)
    input_5.grid(row=4, column=1, padx=10, pady=10)


def populate_buttons(window: Tk) -> None:
    """
    Populates the buttons
    """
    global button_1, button_2, button_3
    window.grid(row=0, column=0, padx=10, pady=10)
    button_1 = Button(window, text="Calculate", command=redraw_lines)
    button_2 = Button(window, text="Save", command=save)
    button_3 = Button(window, text="Reset", command=reset)
    button_1.grid(row=0, column=0, padx=20, pady=10)
    button_2.grid(row=0, column=1, padx=20, pady=10)
    button_3.grid(row=0, column=2, padx=20, pady=10)


def populate_graph(window: Tk) -> None:
    """
    Populates the graph
    """
    global graphWindow
    graphWindow = window
    create_graph()

    set_values([], [], False, 0)

    finish_graph()


def clear_bar_chart() -> None:
    """
    Clears the graph
    """
    global bar1
    bar1.get_tk_widget().pack_forget()


def create_graph() -> None:
    """
    Creates the graph
    """
    global graph, graph_plot
    graph = plt.Figure(figsize=(5, 5), dpi=100)
    graph_plot = graph.add_subplot(111)


def finish_graph() -> None:
    """
    Finishes the graph
    """
    global graph, graph_plot, bar1, graphWindow
    bar1 = FigureCanvasTkAgg(graph, graphWindow)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    graph_plot.set_title('Trajectory')


def set_values(x_val, y_val, main: bool, index) -> None:
    """
    Sets the values on the graph
    :param x_val:
    :param y_val:
    :param main:
    :param index:
    :return: None
    """
    global graph_plot, graph_pl

    if main:
        lStyle = 'solid'
    else:
        lStyle = 'dashed'

    graph_pl, = graph_plot.plot(x_val, y_val, color=colors[index], linestyle=lStyle)


def create_window() -> Tk:
    """
    Creates the main window
    :return: Tk
    """
    global rightFrame
    window = Tk()
    window.title("Trajectory calculator")
    window.geometry('1200x800')
    window.configure(width=1200, height=800)
    window.pack_propagate(0)
    leftFrame = Frame(window, width=800, height=300, )
    leftFrame.pack_propagate(0)
    leftFrame.pack(fill='both', side='left', expand='True')

    rightFrame = Frame(window, width=400, height=800, highlightbackground='darkGrey', highlightthickness=3)
    rightFrame.pack_propagate(0)
    rightFrame.pack(fill='both', side='right', expand='True')

    leftTopFrame = Frame(leftFrame, width=800, height=300, highlightbackground='darkGrey', highlightthickness=3)
    leftTopFrame.pack_propagate(0)
    leftTopFrame.pack(fill='both', side='top', expand='True')
    leftBottomFrame = Frame(leftFrame, width=800, height=500, highlightbackground='darkGrey', highlightthickness=3)
    leftBottomFrame.pack_propagate(0)
    leftBottomFrame.pack(fill='both', side='bottom', expand='True')

    fr_1 = Frame(leftTopFrame)
    populate_inputs(fr_1)
    fr_1.pack()

    fr_2 = Frame(leftTopFrame)
    populate_buttons(fr_2)
    fr_2.pack()

    fr_3 = Frame(rightFrame)
    fr_3.pack()
    window.configure(bg='lightgray')

    fr_4 = Frame(leftBottomFrame)
    populate_graph(fr_4)
    fr_4.pack()

    return window
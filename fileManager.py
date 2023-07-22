import glob
import os
import time
import calendar
import mainWindow

readDir = 'saved'


class TrajectoryObject:
    height: float
    angle: float
    gravity: float
    velocity: float
    step: float
    timeStamp: int


def write_to_file(height: float, velocity: float, gravity: float, angle: float, step: float):
    current_GMT = time.gmtime()
    curTimestamp = calendar.timegm(current_GMT)
    f = open('' + readDir + '\\' + str(curTimestamp) + ".txt", "x")
    f.write(str(height))
    f.write('\n')
    f.write(str(velocity))
    f.write('\n')
    f.write(str(gravity))
    f.write('\n')
    f.write(str(angle))
    f.write('\n')
    f.write(str(step))
    f.write('\n')
    f.write(str(curTimestamp))
    f.close()
    newObject = TrajectoryObject()
    newObject.height = height
    newObject.velocity = velocity
    newObject.gravity = gravity
    newObject.angle = angle
    newObject.step = step
    newObject.timeStamp = curTimestamp
    return newObject


def remove_item_file(item: TrajectoryObject):
    global data, displayedItems

    try:
        os.remove(os.getcwd() + "\\" + readDir + "\\" + str(int(item.timeStamp)) + ".txt")
        mainWindow.populate_save_points(data)
    except:
        print("File Doesn't Exist")


def read_files():
    global readDir
    data = []
    files = glob.glob(os.getcwd() + "\\" + readDir + "\\*.txt")
    for file in files:
        with open(file) as f:
            lines = f.readlines()
            if len(lines) == 6:
                newObject = TrajectoryObject()
                newObject.height = float(lines[0].replace('\n', ''))
                newObject.velocity = float(lines[1].replace('\n', ''))
                newObject.gravity = float(lines[2].replace('\n', ''))
                newObject.angle = float(lines[3].replace('\n', ''))
                newObject.step = float(lines[4].replace('\n', ''))
                newObject.timeStamp = int(lines[5].replace('\n', ''))
                data.append(newObject)
    return data
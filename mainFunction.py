import math as Math


def calculation_value(howFarObjectTraveled: float, height: float, velocity: float, angle: float, g: float):
    rad = angle_as_radian(angle)
    return height + (howFarObjectTraveled * Math.tan(rad)) - (g * Math.pow(howFarObjectTraveled, 2)) / (
                2 * Math.pow(velocity, 2) * Math.pow(Math.cos(rad), 2));


def angle_as_radian(angle: float):
    return Math.pi * angle / 180
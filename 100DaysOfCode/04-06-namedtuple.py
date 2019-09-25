from collections import namedtuple
# namedtuple: A compromize between a tuple & dictionary

# via tuple
rgb_colors = (55, 140, 200)
print("Red:{}".format(rgb_colors[0])) # Red
print("Green:{}".format(rgb_colors[1])) # Green
print("Blue:{}".format(rgb_colors[2])) # Blue

# via dictionary
print("")
rgb = {"red":55, "green":140, "blue":200}
print("Red:{}".format(rgb["red"])) # Red
print("Green:{}".format(rgb["green"])) # Green
print("Blue:{}".format(rgb["blue"])) # Blue

# via namedtuple(class without methods)
print("")
Colors = namedtuple('Colors',['red','green','blue'])
rgbcolors = Colors(55,140,200)
print("Red:{}".format(rgbcolors.red))
print("Green:{}".format(rgbcolors.green))
print("Blue:{}".format(rgbcolors.blue))

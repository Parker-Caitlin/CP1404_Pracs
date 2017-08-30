"""
CP1404 Prac
Hex colours in a dictionary
"""

HEX_COLOURS = {"AliceBlue": "#f0f8ff", "brown1": "#ff4040", "coral1": "#ff7256", "DarkOliveGreen1": "#caff70",
               "DarkOrchid1": "#bf3eff", "DarkSlateBlue": "#483d8b", "DeepPink4": "#8b0a50", "DeepSkyBlue4": "#00688b",
               "gray2": "#050505", "HotPink": "#ff69b4"}

for key in HEX_COLOURS:
    print(key)

colour = input("Please enter a colour name: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Please enter a colour name: ")
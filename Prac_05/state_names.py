"""
CP1404 Prac
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for key in STATE_NAMES:
    print(key, "is", STATE_NAMES.get(key))

# state = input("Enter short state: ").upper()
# while state != "":
#     if state in STATE_NAMES:
#         print(state, "is", STATE_NAMES[state])
#     else:
#         print("Invalid short state")
#     state = input("Enter short state: ").upper()

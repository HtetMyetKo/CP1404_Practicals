HEX_CODES = {"aliceblue": "#f0f8ff", "bistre": "##3d2b1f", "black": "#000000", "blond": "#faf0be", "brown": "#a52a2a", "gray": "#bebebe", "greenlizard": "#a7f432", "hotpink": "#ff69b4", "khaki": "#f0e68c", "yellowgreen": "#9acd32"}

print(HEX_CODES)


color = input("Enter color: ").lower()
while color != "":
    if color in HEX_CODES:
        print(color, "is", HEX_CODES[color])
    else:
        print("Invalid color.")
    color = input("Enter color: ").lower()
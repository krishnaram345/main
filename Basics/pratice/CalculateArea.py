

height=int(input("Enter the height: "))
width=int(input("Enter the width: "))


def calculate_area (height, width):
    area = (1/2)*width*height
    print(area)
    print("Traingle area is ",area)
    return area




if __name__ == "__main__":
    print("In Main method of",__name__)
    calculate_area(height, width)


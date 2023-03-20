
class House: 
  # constructor method/funtions are called methods
  # variables in classes are attributes
  def __init__(self, windows, width, length, color, floors, occupants):
    # self.area = area
    # area(self.length, self.width)
    self.windows = windows
    self.width = width
    self.length = length
    self.color = color
    self.floors = floors
    self.occupants = occupants
      
  def area(self, width, length):
    return width * length

redHouse = House(3, 15, 20, "red", 2, True)
print(redHouse)
print(redHouse.area(34, 56))
import math

class Rectangle:
  def __init__(self, w, h) -> None:
    self.width = w
    self.height = h
  
  def set_width(self, w) -> None:
    self.width = w

  def set_height(self, h) -> None:
    self.height= h
  
  def get_area(self) -> int:
    return self.width * self.height

  def get_perimeter(self) -> int:
    return self.width * 2 + self.height * 2

  def get_diagonal(self) -> float:
    return math.sqrt((self.width ** 2) + (self.height ** 2))

  def get_picture(self) -> str:
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    output = ""
    for i in range(self.height):
      output += "*" * self.width + "\n"
    return output
    
  def get_amount_inside(self, obj) -> int:
    thisArea = self.get_area
    if self.width < obj.width or self.height < obj.height:
      return 0
    #how many time can you fit w and h? 
    maxW = math.floor(self.width / obj.width)
    maxH = math.floor(self.height / obj.height)
    return maxW * maxH

  def __str__(self) -> str:
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
  def __init__(self, w) -> None:
    self.width = w
    self.height = w
    self.side = w
  
  def set_width(self, w) -> None:
    self.width = w
    self.height= w
    self.side = w

  def set_height(self, h) -> None:
    self.width = h
    self.height= h
    self.side = h
  
  def set_side(self, s) -> None:
    self.side = s
    self.width = s
    self.height = s

  def __str__(self) -> str:
    return f"Square(side={self.side})"
import math

class MapGenerator :
  def __init__(self, width, height, hexSize = 20, orientation = 'point'):
    self.width = width
    self.height = height
    self.hexSize = hexSize
    self.cells = {}

  def offsetToAxial(self, col, row):
    q = col - (row - (row & 1)) // 2
    r = row
    return (q, r)

  def axialToOffset(self, q, r):
    col = q + (r - (r & 1)) // 2
    row = r
    return (col, row)
  
  def isValidHex(self, q, r):
    col, row  = self.axialToOffset(q, r )
    return col >= 0 and col < self.width and row >= 0 and row < self.height
  
  def axialToPixelFlat(self, q, r):
    x = self.hexSize * (3/2 * q)
    y = self.hexSize * (math.sqrt(3) * (r + q / 2))
    return (x, y)
  
  def axialToPixelSpaced(self, q, r, size, spacing = 1.1):
    x = size * (3/2 * q) * spacing
    y = size * (math.sqrt(3) * (r + q / 2)) * spacing
    return {x, y}
  



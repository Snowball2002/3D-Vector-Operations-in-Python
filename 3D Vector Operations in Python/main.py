
def print_hi(name):
   
    print(f'Hi, {name}')  


if __name__ == '__main__':
    print_hi('PyCharm')


class Vector:
	def __init__(self, xcoord, ycoord, zcoord): #Creates a vector
		self.x = xcoord
		self.y = ycoord
		self.z = zcoord

	def add(self, v):
		x = self.x + v.x
		y = self.y + v.y
		z = self.z + v.z
		return Vector(x, y, z)

	def dotProduct(self, v): 
		return self.x * v.x + self.y * v.y + self.z * v.z


v1 = Vector(1,1,1)
v2 = Vector(2,3,1)
print(v1.add(v2))
print(v1.dotProduct(v2))



import termcolor

class board:

	def __init__(self):
		self.w = 11
		self.l = 5
		self.grid = [ [ 0 ]  * self.w] *self.l

	def printboard(self):
		for l in self.grid:
			print(l)

class part:

# term color
	# black
	# red
	# green
	# yellow
	# blue
	# magenta
	# cyan
	# white
	# light_grey
	# dark_grey
	# light_red
	# light_green
	# light_yellow
	# light_blue
	# light_magenta
	# light_cyan
	lblue = 'light_blue'
	teal = 'light_cyan'
	green = 'green'
	dred = 'light_red'
	dblue = 'dark_grey'
	mint = 'light_green'
	blue = 'blue'
	purple = 'black'
	orange = 'white'
	red = 'red'
	yellow = 'yellow'
	pink = 'magenta'

	colors = [lblue, teal, green, dred, dblue, mint, blue, purple, orange, red, yellow, pink]

	shapes = []

	shapes.append( [[1,1], [1, 0]] )

	shapes.append( [[1 ,1, 1], [0, 1, 0]] )
	shapes.append( [[1 ,1, 1], [1, 0, 1]] )
	shapes.append( [[0 ,1, 1], [1, 1, 0]] )
	shapes.append( [[1 ,1, 1], [1, 0, 0]] )
	shapes.append( [[1 ,1, 1], [1, 1, 0]] )

	shapes.append( [[1 ,1, 1], [1, 0, 0], [1, 0, 0]] )
	shapes.append( [[0 ,1, 1], [1, 1, 0], [1, 0, 0]] )
	shapes.append( [[0 ,1, 0], [1, 1, 1], [1, 0, 0]] )


	shapes.append( [[1 ,1, 1, 1], [1, 0, 0, 0]] )
	shapes.append( [[1 ,1, 1, 1], [0, 1, 0, 0]] )
	shapes.append( [[0 ,1, 1, 1], [1, 1, 0, 0]] )

	def __init__(self, id):
		self.shape = part.shapes[id]
		self.color = part.colors[id]


	def printpart(self):
		for l in self.shape:
			termcolor.cprint(l, self.color)

			# print(l)
		print(self.color)




for i in range(len(part.shapes)):
	print(i)
	part(i).printpart()
b = board()
print(b.printboard())


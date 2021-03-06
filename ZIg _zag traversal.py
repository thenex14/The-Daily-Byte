class Node():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


class BinarysearchTree():

	def __init__(self):
		self.root = None


	def insert(self,data):
		if self.root is None:
			self.root = Node(data)
			return 
		else:
			self._insert(data,self.root)

	def _insert(self,data,cur_node):
		if cur_node.data < data:
			if cur_node.right is None:
				cur_node.right = Node(data)
			else:
				self._insert(data,cur_node.right)

		elif cur_node.data > data:
			if cur_node.left is None:
				cur_node.left = Node(data)
			else:
				self._insert(data,cur_node.left)

		else:
			print("No dubplicate values allowed in this tree :(")

	def zig_zag_order(self):

		# intitialise two stacks cur and next

		cur = list()
		next = list()

		# append the first( root node) node to cur

		cur.append(self.root)

		# we need a boolean to flag on and off the direction to traverse
		# left to right or right to left, set it to True

		LR = True

		each_level = []
		zig_zag = []

		while cur:

			node = cur.pop()
			# need to print it level by level , so use a list eachlevel
			each_level.append(node.data)


			if LR:
				# If LR is True push left -> right  to next(very important)
				if node.left:
					next.append(node.left)
				if node.right:
					next.append(node.right)

			else:
				# push right -> left

				if node.right:
					next.append(node.right)
				if node.left:
					next.append(node.left)


			# if cur becomes empty  a level is traversed completely

			if len(cur) == 0:
				zig_zag.append(each_level)
				cur,next = next,cur
				each_level = []
				LR = not LR

		return zig_zag


athul = BinarysearchTree()
for i in [21,89,65,18,98,13,45,67,109,77,34,691]:
	athul.insert(i)


print(athul.zig_zag_order())


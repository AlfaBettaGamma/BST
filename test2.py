from wibe_and_deep import BST, BSTNode, BSTFind

class my_test:
	def test1(self):
		A1 = BSTNode(10, 15, None)
	#	A2 = BSTNode(9, 38, None)
	#	A3 = BSTNode(7, 60, None)
	#	A4 = BSTNode(5, 33, None)
	#	A5 = BSTNode(8, 20, None)
	#	A6 = BSTNode(12, 70, None)
	#	A7 = BSTNode(10, 44, None)
	#	A8 = BSTNode(16, 28, None)
	#	A9 = BSTNode(15, 42, None)
	#	A10 = BSTNode(15, 42, None)
	#	A11 = BSTNode(13, 64, None)
	#	A12 = BSTNode(11, 62, None)
	#	A13 = BSTNode(14, 58, None)
	#	A14 = BSTNode(25, 67, None)
	#	A15 = BSTNode(22, 47, None)
	#	A16 = BSTNode(30, 74, None)

		tree = BST(A1)
		tree.AddKeyValue(9, 38)
		tree.AddKeyValue(8, 20)
		tree.AddKeyValue(12, 70)
		tree.AddKeyValue(10, 44)
		tree.AddKeyValue(16, 28)
		tree.AddKeyValue(15, 42)
		tree.AddKeyValue(13, 64)
		tree.AddKeyValue(11, 62)
		tree.AddKeyValue(14, 58)
		tree.AddKeyValue(25, 67)
		tree.AddKeyValue(22, 47)
		tree.AddKeyValue(30, 74)

		print('количество узлов - ', tree.Count())

		print('обход в ширину - ', tree.WideAllNodes())
		print('обход в глубину - ', tree.DeepAllNodes(0))


test = my_test()
test.test1()
from test import BST, BSTNode, BSTFind

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
		print(tree.FindNodeByKey(7).NodeHasKey)
		print(tree.FindNodeByKey(9).NodeHasKey)
		tree.AddKeyValue(15, 42)
		print(tree.FindNodeByKey(15).NodeHasKey)
		print(tree.FindNodeByKey(19).NodeHasKey)
		tree.DeleteNodeByKey(15)

		print('______________________________')

		print(tree.FindNodeByKey(7).NodeHasKey)
		tree.AddKeyValue(7, 60)
		print(tree.FindNodeByKey(7).NodeHasKey)

		print('______________________________')

		print(tree.FindNodeByKey(5).NodeHasKey)
		tree.AddKeyValue(5, 33)
		print(tree.FindNodeByKey(5).NodeHasKey)

		print('______________________________')
		print('количество узлов до - ', tree.Count())
		print(tree.FindNodeByKey(9).NodeHasKey)
		tree.AddKeyValue(9, 38)
		print('количество узлов после - ', tree.Count())

		print('_______________________________')
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
		print(tree.FinMinMax(tree.Root ,True).NodeValue)
		print(tree.FinMinMax(tree.Root ,False).NodeValue)
		

		print('______________________________')
		print(tree.FindNodeByKey(12).NodeHasKey)
		tree.DeleteNodeByKey(12)
		print(tree.FindNodeByKey(12).NodeHasKey)



		print('количество узлов - ', tree.Count())


test = my_test()
test.test1()
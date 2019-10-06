class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Lvl = 0  # уровень узла относительно корня


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node):
        self.Root = node # корень дерева, или None
        self.lvl = 0

    def FindNodeByKey(self, key):
        node = BSTFind()
        node.Node = self.Root
        while node.Node.NodeKey != key:
            if key >= node.Node.NodeKey:
                if node.Node.RightChild is None:
                    break
                node.Node = node.Node.RightChild
            else:
                if node.Node.LeftChild is None:
                    node.ToLeft = True
                    break
                node.Node = node.Node.LeftChild
        else:
            node.NodeHasKey = True
        # ищем в дереве узел и сопутствующую информацию по ключу
        return node# возвращает BSTFind

    def AddKeyValue(self, key, val):
        node = self.FindNodeByKey(key)
        nextNode = BSTNode(key, val, None)
        if node.NodeHasKey is False:
            if node.ToLeft is False:
                self.lvl = nextNode.Lvl + 1 + nextNode.Lvl
                nextNode.Lvl = self.Lvl
                node.Node.RightChild = nextNode
            else:
                self.lvl = nextNode.Lvl + 1 + nextNode.Lvl
                nextNode.Lvl = self.lvl
                node.Node.LeftChild = nextNode
            nextNode.Parent = node.Node
            return True
        else:
            return False
        # добавляем ключ-значение в дерево
        # если ключ уже есть
  
    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if FindMax is True:
            while node.RightChild is None:
                node = node.RightChild
        else:
            while node.LeftChild is None:
                node = node.LeftChild
        # ищем максимальное/минимальное (узел) в поддереве
        return node
	
    def DeleteNodeByKey(self, key):
        node = self.FindNodeByKey(key)
        if node.NodeHasKey is True:
            if node.Node.RightChild is not None and node.Node.LeftChild is not None:
                successor = self.FinMinMax(node.Node.RightChild, False)
                if successor.RightChild is not None:
                    successor = successor.RightChild
                    successor.Parent.RightChild = None
                else:
                    successor.Parent.LeftChild = None
            else:
                if node.Node.RightChild is not None:
                    successor = node.Node.RightChild
                    node.Node.RightChild = successor.RightChild
                    node.Node.LeftChild = successor.LeftChild
                elif node.Node.LeftChild is not None :
                    successor = node.Node.LeftChild
                    node.Node.RightChild = successor.RightChild
                    node.Node.LeftChild = successor.LeftChild
                else:
                    successor = node.Node
                    if successor.Parent.RightChild == successor:
                        successor.Parent.RightChild = None
                    else:
                        successor.Parent.LeftChild = None
            successor.Parent = None
            node.Node.NodeKey = successor.NodeKey
            node.Node.NodeValue = successor.NodeValue
            return True
        else:
        # удаляем узел по ключу
            return False # если узел не найден

    def Count(self):
        node = self.Root
        res = [None, self.Root]
        while node is not None:
            if node.LeftChild not in res and node.LeftChild is not None:
                node = node.LeftChild
            elif node.RightChild not in res and node.RightChild is not None :
                node =  node.RightChild
            if node not in res:
                res.append(node)
            if node.LeftChild is None and node.RightChild is None:
                node =  node.Parent
            elif node.RightChild in res and node.LeftChild in res :
                node = node.Parent
        result = 0
        for i in res:
            if i is not None:
                result += 1
        return result # количество узлов в дереве
class BSTNode:
    
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


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
        return node # возвращает BSTFind

    def AddKeyValue(self, key, val):
        node = self.FindNodeByKey( key)
        downNode = BSTNode(key, val, None)
        if node.NodeHasKey is False:
            if node.ToLeft is False:
                node.Node.RightChild = downNode
            else:
                node.Node.LeftChild = downNode
            downNode.Parent = node.Node
            return True
        else:
            return False
        # добавляем ключ-значение в дерево
        # если ключ уже есть
  
    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if FindMax is True:
            while node.RightChild is not None:
                node = node.RightChild
        else:
            while node.LeftChild is not None:
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
                    node.Node.LeftChild = successor.LeftChild
                    node.Node.RightChild = successor.RightChild
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


    def WideAllNodes(self):
        def width(lvl, Mylist):
            if lvl == 0:
                Mylist = [self.Root]
            for i in Mylist[lvl:]:
                if i.LeftChild is not None:
                    Mylist.append(i.LeftChild)
                if i.RightChild is not None:
                    Mylist.append(i.RightChild)
                lvl += 1
            if lvl != len(Mylist):
                width(lvl, Mylist)
            return Mylist
        return width(0, [])

    def DeepAllNodes(self, order):
        def Deep(order, node, Mylist):
            if node == 0:
                node = self.Root

            def leftBranch():
                if node.LeftChild is not None:
                    Deep(order, node.LeftChild, Mylist)

            def rightBranch():
                if node.RightChild is not None:
                    Deep(order, node.RightChild, Mylist)

            def middleBranch():
                if node is not Mylist:
                    Mylist.append(node)

            actions = [leftBranch, middleBranch, rightBranch]
            if order == 0:
                for i in actions:
                    i()
            elif order == 1 :
                actions[0]()
                actions[2]()
                actions[1]()
            elif order == 2 :
                actions[1]()
                actions[0]()
                actions[2]()
            myList = Mylist
            Mylist = []
            return myList
        Mylist = []
        return Deep(order, self.Root, Mylist)

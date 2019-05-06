
class BinaryTree:
    def __init__(self):
        self.nodes=None
    def AddNode(self,val):
        if self.nodes is None:
            self.nodes = Node(None,None,val)
        else:
            if self.nodes.val > val :
                if  self.nodes.left is None:
                    self.nodes.left = Node(None,None,val)
                else:
                    self.nodes.left.AddNode(self.nodes.left,val)
            elif self.nodes.val < val :
                if  self.nodes.right is None:
                    self.nodes.right = Node(None,None,val)
                else:
                    self.nodes.right.AddNode(self.nodes.right,val)
    def PrintTree(self):
         if self.nodes is None:
             print('Tree is Empty')
         else:
             self.nodes.PrintNode()
             if not self.nodes.left is None:
                 print("Left node val"+str(self.nodes.left.val))
             if not self.nodes.right is None:
                 print("Right node val"+str(self.nodes.right.val))




        


def main():
    #nd= Node(None,None,10);
    #nd.PrintNode();
    #input
    tree=BinaryTree()
    try:
       while (True):
        ipt = int(input('Enter a node value to add'))
        tree.AddNode(ipt);
    except:
        tree.PrintTree()
        return

    



class Node:
    def __init__(self, left,right,val):
        self.left = left
        self.right = right
        self.val = val
    def PrintNode(self):
        print(self.val)

main()


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)
    
    def deepth(self):
        return self._goDeep(self)
        
    def _goDeep(self, node):
        if (not node):
            return 0
        
        return max( 1 + self._goDeep(node.left), 1 + self._goDeep(node.right))

    # find the node with the value
    def find_bfs(self, value):
        return self._bfs_search(self, value)
        
    def _bfs_search(self, node, val):
        while (node):
            if (node.value==val):
                break
            node = node.left if (node.value > val) else node.right
        return node
    
    def find_dfs(self, value):
        return self._dfs_search(self, value)
    
    def _dfs_search(self, node, val):
        if (node is None or node.value == val):
            return node
            
        # go left if val is smaller
        return self._dfs_search(node.left, val) if (node.value > val) else self._dfs_search(node.right, val)
    

    # inserting a new node
    def insertNode(self, val: int):
        self = self._dfs_insert(self, val)
            
    def _dfs_insert(self, node, val):
        if (node is None):
            return Node(val)
        
        else:
            if (node.value < val):
                node.right = self._dfs_insert(node.right, val)
            else:
                node.left = self._dfs_insert(node.left, val)
        
        return node
        
    
    def showTree(self):

        tree_deep = self.deepth()

        current_level = [self]
        level_num = 0
        while current_level:
            level_num +=1

            pre = '-' * ((tree_deep - level_num ) * 3 - 2 )
            intval = ' ' * ((tree_deep - level_num ) * 2 +1 )
            print(pre + intval.join(str(node if(node) else '*') for node in current_level))
            next_level = list()
            for n in current_level:
                #if n.left:
                if (n):
                    next_level.append(n.left)
                    #if n.right:
                    next_level.append(n.right)
                else:
                    next_level.append(None)
                    next_level.append(None)

            # only continue if there is node in the next level
            if (any(next_level)):
                current_level = next_level
            else:
                current_level = []
    
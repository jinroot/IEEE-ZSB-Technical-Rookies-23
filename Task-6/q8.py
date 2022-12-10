def insert(self, val):
    #Enter you code here.
    if self.root == None:
        self.root = Node(val)
    else:
        current = self.root
        while True:
            if val<current.info:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    break
            elif val>current.info:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    break
            else:
                break
if not root:
            return 0
        
        # Recursively calculate left and right depths
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
 

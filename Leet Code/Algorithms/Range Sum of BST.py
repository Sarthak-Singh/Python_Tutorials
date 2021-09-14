def rangeSumBST(root, low, high):
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
            if low <= node.val <= high:
                total += node.val
    return total


print(rangeSumBST([10,5,15,3,7,None,18], 7, 15))

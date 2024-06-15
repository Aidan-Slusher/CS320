class BTreeNode:
    def __init__(self, keys=None, children=None, max_size=4):
        self.keys = keys or []
        self.children = children or []
        self.max_size = max_size

    def __repr__(self):
        return f"BTreeNode(keys={self.keys}, children={self.children})"


class BTree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        if value is None:
            return False
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if node is None:
            return False
        if value in node.keys:
            return True
        elif node.children:
            for i, key in enumerate(node.keys):
                if value < key:
                    return self._contains(node.children[i], value)
            return self._contains(node.children[-1], value)
        return False

    def insert(self, value):
        if value is None:
            return False
        if not self.contains(value):
            self.root = self._insert(self.root, value)
            return True
        return False

    def _insert(self, node, value):
        if node is None:
            return BTreeNode(keys=[value])

        if len(node.keys) < node.max_size - 1:  # Room in current node
            node.keys.append(value)
            node.keys.sort()
            return node
        else:  # Split node and push up middle value
            node.keys.append(value)
            node.keys.sort()
            middle_index = len(node.keys) // 2
            middle_value = node.keys[middle_index]
            left_child = BTreeNode(keys=node.keys[:middle_index], children=node.children[:middle_index + 1], max_size=node.max_size)
            right_child = BTreeNode(keys=node.keys[middle_index + 1:], children=node.children[middle_index + 1:], max_size=node.max_size)
            node.keys = [middle_value]
            node.children = [left_child, right_child]
            return node

    def delete(self, value):
        if value is None:
            return False
        if self.contains(value):
            self.root = self._delete(self.root, value)
            return True
        return False

    def _delete(self, node, value):
        if node is None:
            return None

        if value in node.keys:  # Value is in current node
            if len(node.keys) > (node.max_size - 1) // 2:  # Sufficient keys, just remove
                node.keys.remove(value)
                return node
            else:  # Need to borrow or merge
                # First try to borrow from right sibling
                right_sibling_index = None
                for i, key in enumerate(node.keys):
                    if value < key:
                        right_sibling_index = i
                        break
                if right_sibling_index is None:
                    right_sibling_index = len(node.keys) - 1
                if right_sibling_index < len(node.children) - 1 and len(node.children[right_sibling_index + 1].keys) > (node.max_size - 1) // 2:
                    right_sibling = node.children[right_sibling_index + 1]
                    borrowed_key = right_sibling.keys.pop(0)
                    node.keys[right_sibling_index] = borrowed_key
                    return node
                # Try borrowing from left sibling
                left_sibling_index = right_sibling_index - 1
                if left_sibling_index >= 0 and len(node.children[left_sibling_index].keys) > (node.max_size - 1) // 2:
                    left_sibling = node.children[left_sibling_index]
                    borrowed_key = left_sibling.keys.pop(-1)
                    node.keys[left_sibling_index] = borrowed_key
                    return node
                # Merge with a sibling
                if right_sibling_index < len(node.children) - 1:
                    node.keys.pop(right_sibling_index)
                    merged_node = node.children.pop(right_sibling_index + 1)
                else:
                    node.keys.pop(left_sibling_index)
                    merged_node = node.children.pop(left_sibling_index)
                node.keys.extend(merged_node.keys)
                node.children.extend(merged_node.children)
                return node
        else:  # Value is not in current node, descend to child
            for i, key in enumerate(node.keys):
                if value < key:
                    node.children[i] = self._delete(node.children[i], value)
                    return node
            node.children[-1] = self._delete(node.children[-1], value)
            return node

    def traverse(self):
        if self.root is None:
            return None
        return self._traverse(self.root)

    def _traverse(self, node):
        result = []
        if node.children:
            for i, child in enumerate(node.children):
                result.extend(self._traverse(child))
                if i < len(node.keys):
                    result.append(node.keys[i])
            result.extend(self._traverse(node.children[-1]))
        else:
            result.extend(node.keys)
        return result

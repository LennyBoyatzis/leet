class DoubleLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache():
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DoubleLinkedNode(), DoubleLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node):
        """
        Always add the new node right after head
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        """
        Remove an existing node from the linked list
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def move_to_head(self, node):
        """
        Move certain node in between the head
        """
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        """
        Pop the current tail
        """
        res = self.tail.prev
        self.remove_node(res)
        return res

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1

        self.move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            newNode = DoubleLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)

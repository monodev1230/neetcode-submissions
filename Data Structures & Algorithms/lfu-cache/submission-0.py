from collections import defaultdict

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:

    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add(self,node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size > 0:
            node = self.tail.prev
            self.remove(node)
            return node
        return None


class LFUCache:

    def __init__(self,capacity:int):
        self.capacity = capacity
        self.keyMap = {}
        self.freqMap = defaultdict(DLL)
        self.minFreq = 0

    def get(self,key:int)->int:

        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]
        self.update(node)

        return node.value

    def put(self,key:int,value:int)->None:

        if self.capacity == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            self.update(node)
            return

        if len(self.keyMap) == self.capacity:
            list = self.freqMap[self.minFreq]
            removed = list.remove_last()
            del self.keyMap[removed.key]

        node = Node(key,value)
        self.keyMap[key] = node

        self.minFreq = 1
        self.freqMap[1].add(node)

    def update(self,node):

        freq = node.freq
        list = self.freqMap[freq]

        list.remove(node)

        if freq == self.minFreq and list.size == 0:
            self.minFreq += 1

        node.freq += 1

        self.freqMap[node.freq].add(node)
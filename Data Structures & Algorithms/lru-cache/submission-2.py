class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    def __init__(self, capacity: int):
        
        self.kvMap = {}
        self.knMap = {}
        self.capacity = capacity
        self.curr = 0
        self.lStart = Node(0)
        self.lEnd = Node(0)
        self.lStart.nxt = self.lEnd
        self.lEnd.prev = self.lStart
        print(self.knMap)
        print(self.kvMap)

    def get(self, key: int) -> int:
        #print("get " + str(key))
        #print(self.knMap)
        #print(self.kvMap)
        if key in self.kvMap:
            node = self.knMap[key]
            p = node.prev
            n = node.nxt
            p.nxt = n
            n.prev = p
            p = self.lEnd.prev
            p.nxt = node
            node.prev = p
            node.nxt = self.lEnd
            self.lEnd.prev = node
            return self.kvMap[key]
            # bring existing node to end
        return -1

    def put(self, key: int, value: int) -> None:
        print("put " + str(key) + ": " + str(value))
        #print(self.knMap)
        #print(self.kvMap)
        if key in self.kvMap:
            self.kvMap[key] = value
            node = self.knMap[key]
            node.val = key
            p = node.prev
            n = node.nxt
            p.nxt = n
            n.prev = p
            p = self.lEnd.prev
            p.nxt = node
            node.prev = p
            node.nxt = self.lEnd
            self.lEnd.prev = node
            # bring existing node to end

        else:
            if self.curr < self.capacity:
                self.curr += 1
                self.kvMap[key] = value
                self.knMap[key] = Node(key)
                node = self.knMap[key]
                p = self.lEnd.prev
                p.nxt = node
                node.prev = p
                node.nxt = self.lEnd
                self.lEnd.prev = node
                #append new node to end
            else:
                self.kvMap[key] = value
                if self.lStart.nxt != self.lEnd:
                    d_key = self.lStart.nxt.val
                    print("    " + str(self.knMap.keys()))
                    d_node = self.knMap[d_key]
                    self.printNode(self.lStart)
                    self.lStart.nxt = d_node.nxt
                    d_node.nxt.prev = self.lStart
                    if d_key in self.kvMap:
                        del self.kvMap[d_key]
                        del self.knMap[d_key]
                self.kvMap[key] = value
                self.knMap[key] = Node(value)
                node = self.knMap[key]
                p = self.lEnd.prev
                p.nxt = node
                node.prev = p
                node.nxt = self.lEnd
                self.lEnd.prev = node

                #append new node to end
                #remove least recently used node from the start

    def printNode(self, node):
        ll = ""
        while node:
            ll += str(node.val)
            ll += "->"
            node = node.nxt
        print("    " + str(ll))
        return
        

        

class Node(object):
    
    def __init__(self, value, nxt = None):
        self.data = value
        self.next_node = nxt
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, n):
        self.next_node = n
        
    def get_data(self):
        return self.data
    
    def set_data(self, value):
        self.data = value
        
        
class LinkedList(object):
    
    def __init__(self, r = None):
        self.root = r
        self.size = 0
        
    def get_size(self):
        print("a lista tem o tamanho", self.size)
        return self.size
    
    def add_node(self, val):
        new_node = Node(val, self.root)
        self.root = new_node
        self.size += 1
        
    def remove_node(self, val):
        print("removendo", val)
        current_node = self.root
        previus_node = None
        while current_node:
            if current_node.get_data() == val:
                if previus_node:
                    previus_node.set_next(current_node.get_next())
                else:
                    self.root = current_node
                self.size -= 1
                return True #data deleted
            else:
                previus_node = current_node
                current_node = current_node.get_next()
        return False #not deleted
    
    def find_node(self, val):
        current_node = self.root
        while current_node:
            if current_node.get_data() == val:
                print("valor", val, "encontrado")
                return val
            else:
                current_node = current_node.get_next()
        print("valor", val,"nao encontrado")
        return None
    
    def show_list(self):
        print("mostrando a lista")
        current_node = self.root
        while current_node:
            print(current_node.get_data())
            current_node = current_node.get_next()
        return None
    
    def bubble_sort(self):
        print("ordenando a lista")
        list_size = self.get_size()
        node_a = self.root
        node_b = node_a.get_next()
        while list_size > 2:
            while node_b:
                if node_a.get_data() > node_b.get_data():
                    # a esta fora de ordem e precisa ser trocado com b
                    #print("a estava fora da ordem", node_a.get_data(), node_b.get_data())
                    temp = node_a.get_data()
                    node_a.set_data(node_b.get_data())
                    node_b.set_data(temp)
                    node_a = node_b
                    node_b = node_b.get_next()
                else:
                    # b jah eh maior que a e esta na ordem correta
                    #print("ja esta na ordem", node_a.get_data(), node_b.get_data())
                    node_a = node_b
                    node_b = node_b.get_next()
            list_size -= 1
            node_a = self.root
            node_b = node_a.get_next()
        self.show_list()
    
myList = LinkedList()
myList.add_node(7)
myList.add_node(5)
myList.add_node(1)
#myList.show_list()
#myList.find_node(3)
#myList.find_node(5)
#myList.remove_node(5)
#myList.show_list()
myList.add_node(6)
myList.add_node(2)
myList.add_node(8)
myList.add_node(0)
myList.show_list()
#myList.get_size()
myList.bubble_sort()

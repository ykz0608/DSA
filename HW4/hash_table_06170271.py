from Cryptodome.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    from Cryptodome.Hash import MD5

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
        if node:
            if node.val !=input_num:
                node.next=ListNode(input_num) 
            elif node.next:
                if node.val != input_num:
                    node = node.next
                else:
                    return
            else:
                return
        else:
            node = ListNode(input_num)
            self.data[rem] = node
               
    def remove(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]
         
        if node:
            if node.val == input_num:
                node = node.next
                self.data[rem] = node
            elif node.next:
                if node.next.val == input_num:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                return None
                       
    def hash_t(self, key):
        test = MD5.new()
        test.update(key.encode('utf-8'))
        num = int(test.hexdigest(),16)
        return num 
        
                        
    def contains(self, key):
        input_num = MyHashSet.hash_t(self, key)
        rem = input_num%self.capacity
        node = self.data[rem]

        if node == None:
            return False
        else:
            if node.val==input_num:
                return True
            elif node.val != input_num:
                node = node.next
                if node == None:
                    return False
                return True
            else :
                return False
            
        
        

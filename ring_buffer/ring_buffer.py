# it's a queue....you add item to the tail and drop items from the head
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []
        self.oldest = None

    def append(self, item):
        length = self.size
        capacity = self.capacity
        # at less than full capacity, you can append items without dropping older items  
        if length < capacity:
            self.storage.append(item)
            self.size += 1
            self.oldest = 0
        # if already at capacity
        else:
          # remove oldest item from start
            self.storage.pop(self.oldest)
          # add new item to end            
            self.storage.insert(self.oldest, item)
          # set new oldest
            if self.oldest == capacity - 1:
                self.oldest = 0
            else:
                self.oldest += 1

    def get(self):
        buffer_list = self.storage
        return buffer_list


# buffer = RingBuffer(5)
# for i in range(50):
#     buffer.append(i)
# print('oldest:', buffer.oldest)
# print(buffer.storage)
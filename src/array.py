class DynamicArray:
    def __init(self, size):
        self.count = 0
        self.size = size
        # Create array containing empty values with pre-set size
        self.storage = [None] * size

    def append(self, value): 
        # Resize if we need to 
        if self.count == self.size:
            # Happens when count equals size!
            self.resize()

        # Assign the item[index] to value
        self.storage[self.count] = value
        # Increment count by one
        self.count += 1

    def insert(self, value, idx): 
        # Resize if count equals size
        if self.count == self.size:
            self.resize()
        
        # Use a for loop to scoot elements over by 1
        for i in range(self.count, idx, -1):
            # -1 means the loop goes backwards
            self.storage[i] = self.storage[i - 1]
            # Assigning i to i - 1 moves each element back
        # Assign value to its new index (1 behind previous)
        self.storage[idx] = value
        # Increment the count to accomodate inserted element
        self.count += 1

    def resize(self):
        # Best practice = double array size when it is full
        self.size = self.size * 2
        # Create a new array and assign newly doubled size
        temp_storage = [None] * self.size
        # Use a for loop to copy elements to new array
        for i in range(self.count):
            # Can also be (self.size // 2)
            temp_storage[i] = self.storage[i]
        # Assign new array to self.storage (completes replacement)
        self.storage = temp_storage
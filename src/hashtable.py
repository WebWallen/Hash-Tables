# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Capacity available isiden the hash table
        self.storage = [None] * capacity # Pre-allocate the array with planned capacity
        self.count = 0 # How many elements are currently in the hash table

    def _hash(self, key):
        # Return a hash with the (key) as an argument
        return hash(key)

    def _hash_djb2(self, key):
        # Make sure it's a string
        new_key = str(key)
        # Assign prime number to salt (this = typical)
        our_salt = 5381
        # Run a for loop to scramble each letter
        for char in new_key:
            # Assign hash value to salted, scrambled value
            hash_value = (our_salt << 5) + our_salt + ord(char)
        return hash_value

    def _hash_mod(self, key):
        # Pass key to hash method and modulus by capacity to get an index that fits
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        # Hash the key to get an index value and assign to index
        index = self._hash_mod(key)
        # Create a new node to hold the LinkedPair key and value
        new_node = LinkedPair(key, value)

        # If this storage index position is available (None)...
        if self.storage[index] is None:
            # Assign the new node to storage index position
            self.storage[index] = new_node
            # Increment the count +1 to account for new node
            self.count += 1
        # Otherwise (hashed index is unavailable)...
        else:
            # Create a temporary container for the current storage index
            current_index = self.storage[index]
            # If the key argument and current key are the same...
            if current_index.key == key:
                # Update the value of current index
                current_index.value = value
                # Return to exit the program logic
                return
            # Otherwise (the keys don't match)...
            else:
                # While there is a "next" to compare with...
                while current_index.next is not None:
                    # If the key is the same (just like above)...
                    if current_index.key == key:
                        # Update the index value to match new value
                        current_index.value == value
                        # Return to exit the program logic
                        return
            # Assign new node to current index.next (means the keys didn't match and we found an unoccupied index)
            current_index.next = new_node
            # Increment the count +1 to account for new node
            self.count += 1
                
    def remove(self, key):
        # Hash the key to get an index and assign to index
        index = self._hash_mod(key)
        # Pass [index] to self.storage and assign to current index
        current_index = self.storage[index]
        # Assign previous to none (pointer will be modified later)
        prev = None
        # While there's a current index (not None) and its key doesn't match the one passed in...
        while current_index is not None and current_index.key != key:
            # Change previous pointer to current index (step 1 of restarting loop)
            prev = current_index
            # Change current_index to previous' next pointer (step 2 of restarting loop)
            current_index = prev.next 
        # If the current index is none (completed every loop and found no matches)...
        if current_index is None:
            # Print an error saying it's not found
            print(f"Key {key} not found")
        # Otherwise (it does exist)...
        else:
            # If there isn't a previous pointer (found the element on LL head)...
            if prev is None:
                # Reassign head storage index to the current index's next pointer
                self.storage[index] = current_index.next
            # Otherwise (there is a previous pointer, i.e. it's not on the head)...
            else:
                # Change previous' next pointer (holding initial index position) to current_index.next (where the loop ended)
                prev.next = current_index.next
            # Print a message to confirm the key was removed
            print(f"Key {key} removed!")

    def retrieve(self, key):
        # Hash the key to get an index and assign to index
        index = self._hash_mod(key)
        # While the storage [index] is not none (search incomplete)...
        while self.storage[index] is not None:
            # Assign storage index to current
            current = self.storage[index]
            # While the current index is not none (still searching)...
            while current is not None:
                # If the current key matches the one passed in...
                if current.key == key:
                    # Return the current value
                    return current.value
                # Otherwise, assign current to its next pointer (continue searching)
                current = current.next
            # Return none (search complete)
            return None

    def resize(self):
        # Assign current (self.) storage to old_storage
        old_storage = self.storage
        # Multiply current capacity by 2 and reassign
        self.capacity = self.capacity * 2
        # Reassign [None] * self.capacity to self.storage (preallocates the memory with updated limit)
        self.storage = [None] * self.capacity
        # Assign None to current (will need to iterate through the elements)
        current = None
        # For all the stuff in our old storage...
        for stuff in old_storage:
            # Assign current stuff to "current"
            current = stuff
            # While current is not none (resizing incomplete)...
            while current is not None:
                # Insert the current key and value to new storage contaier
                self.insert(current.key, current.value)
                # Attach the next pointer to current and reassign (continues loop)
                current = current.next
        # Assign count to 0 because it needs to be recalculated for new storage container
        self.count = 0
        # For the pairs of stuff in current (self.) storage...
        for paired_stuff in self.storage:
            # Assign paired stuff to this_pair (needed so we can loop through each pair)
            this_pair = paired_stuff
            # While this_pair is not none (resizing incomplete)...
            while this_pair is not None:
                # Increment the hashtable count by one to account for added pair
                self.count += 1
                # Attach the next pointer to this_pair and reassign (continues loop)
                this_pair = this_pair.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

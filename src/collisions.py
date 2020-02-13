import random

def how_many_loops_before_collision(loops, array_length):
    # Begin for loop for range of loops passed as an argument
    for i in range(loops):
        # Assign 0 to tries so the counter variable is initialized
        tries = 0
        # Assign an empty set to tried so we have a place to stick indexes
        tried = set()
        # While it's true there are more loops left to run...
        while True:
            # Assign a random number to random_key
            random_key = random.random()
            # Hash the random key, modulo by array length, and assign to hash_index
            hash_index = hash(random_key) % array_length
            # If the hash index hasn't been inserted inside tried yet...
            if hash_index not in tried:
                # Add the hash index to the tried set
                tried.add(hash_index)
                # Increment counter variable tries +1
                tries += 1
            # Otherwise (the hash index has already been listed in the tried set)
            else:
                # Break the loop and...
                break
        # ...print a statement specifying the array length and the number of tries that occured before we had a collisiong
        print("We had {} buckets and {} hashes before a collision".format(array_length, tries))

# how_many_loops_before_collision(10, 100)

# "Buckets" means where the nodes pile up on same LL
def longest_linked_list_chain(keys, buckets, loops): 
    # For each iteration in the range of loops...
    for i in range(loops):
        # Assign an empty dictionary to key counts (needed to track output)
        key_counts = {}

        # For each iteration in the range of buckets (array positions)...
        for i in range(buckets):
            # Assign this iteration of key_counts to 0 (will be modified below)
            key_counts[i] = 0

        # For each iteration in the range of keys...
        for i in range(keys):
            # Create a random key with the str and random methods, then assign to random_key
            random_key = str(random.random())
            # Hash the random key and modulus by buckets to create (then assign) a hash_index
            hash_index = hash(random_key) % buckets
            # Increment the key_counts associated with hash_index by 1
            key_counts[hash_index] += 1

        # Create a placeholder variable for longest chain and assign 0
        longest_chain = 0
        # For each key in key_counts...
        for key in key_counts:
            # If the current key count is greater than the longest chain...
            if key_counts[key] > longest_chain:
                # Assign the current key count to largest chain
                longest_chain = key_counts[key]

        # Note: 2f is just a style formatting thing (converts to floating point number)
        print(f"Longest Linked List Chain for {keys} keys in {buckets} buckets (Load Factor: {keys/buckets:2f}: {longest_chain})")

longest_linked_list_chain(16, 16, 10)
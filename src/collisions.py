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

def longest_linked_list_chain(keys, buckets, loops): 
    for i in range(loops):
        key_counts = {}

        for i in range(buckets):
            key_counts[i] = 0

        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

        largest_n = 0
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]

        print(f"Longest Linked List Chain for {keys} keys in {buckets} buckets (Load Factor: {keys/buckets:2f}: {largest_n})")

longest_linked_list_chain(16, 16, 10)
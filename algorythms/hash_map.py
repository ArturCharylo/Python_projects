class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found = False
        for index, record in enumerate(bucket):
            record_key = record

            # check if the bucket has same key as the key to be inserted
            if record_key == key:
                found = True
                break

        # If the bucket has same key as the key to be inserted, Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key

    def get_val(self, key):

        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched, Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key = record

            # check if the bucket has same key as the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)

    # To print the items of hash map

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = HashMap(50)

# insert some values
hash_table.set_val('example value', 'some value')
print(hash_table)
print()

hash_table.set_val('value', 'some other value')
print(hash_table)
print()

# search/access a record with key
print(hash_table.get_val('value'))
print()

# delete or remove a value
hash_table.delete_val('value')
print(hash_table)

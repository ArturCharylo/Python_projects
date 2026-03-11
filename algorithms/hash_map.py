class HashMap:
    def __init__(self, size: int):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found = False
        index_to_update = -1
        
        # Using _ for unused record_val
        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                found = True
                index_to_update = index
                break

        if found:
            bucket[index_to_update] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        # If we only need the value, we don't need enumerate(bucket) or index
        for record_key, record_val in bucket:
            if record_key == key:
                return record_val
        
        return "No record found"

    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_index = -1
        # Using _ for unused record_val
        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                found_index = index
                break
        
        if found_index != -1:
            bucket.pop(found_index)

    def __str__(self) -> str:
        return "".join(str(item) for item in self.hash_table)


# Example usage
if __name__ == "__main__":
    hash_table = HashMap(50)
    hash_table.set_val('example key', 'some value')
    hash_table.set_val('value', 'some other value')
    
    print(f"Full table: {hash_table}\n")
    print(f"Search 'value': {hash_table.get_val('value')}\n")
    
    hash_table.delete_val('value')
    print(f"After deletion: {hash_table}")
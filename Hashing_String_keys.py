"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

#U = 85
#D = 68

class HashTable(object):
    def __init__(self):
        self.table = [None]*100
        self.index = 0

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        self.table[self.index] = string
        self.index += 1

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        if string in self.table:
            hash_val = str(ord(string[0])) + str(ord(string[1]))
            return hash_val
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hash_val = str(ord(string[0])) + str(ord(string[1]))
        return hash_val
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))

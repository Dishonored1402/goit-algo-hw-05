class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def delete(self, key):
        index = self.hash_function(key)
        
        if self.table[index] is None:
            print("Ключ не знайдений!")
            return
        
        for i, (existing_key, _) in enumerate(self.table[index]):
            if existing_key == key:
                del self.table[index][i]
                print(f"Ключ {key} та значення видалено.")
                return
        print("Ключ не знайдений!")

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for existing_key, value in self.table[index]:
            if existing_key == key:
                return value
        return None

    def display(self):
        for i, slot in enumerate(self.table):
            if slot is not None:
                print(f"Індекс {i}: {slot}")


ht = HashTable()
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("grapes", 300)

ht.display()
ht.delete("banana")
ht.display()
ht.delete("orange")

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for item in range(self.array_size)]

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    found = False
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        found = True
    if not found:
      list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None

# -----------------------------------------------------
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
print(blossom.retrieve('snapdragon'))
print('---------------------')
# -----------------------------------------------------
for item in blossom.array:
  if item.head_node == None:
    print(None)
    continue
  for node in item:
    print(node, end='')
  print()

'''
hash_map = HashMap(10)
hash_map.assign('i', 'yo')
hash_map.assign('he', 'dont know')
hash_map.assign('she', 'ella')
hash_map.assign('it', 'esto')
hash_map.assign('he', 'quien?')
hash_map.assign('he', 'él')
hash_map.assign('we', 'nosotros')
hash_map.assign('they', 'ellos')
print(hash_map.retrieve('it'))
'''

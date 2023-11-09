class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes

  def add_child(self, child_node):
    # creates parent-child relationship
    print("Adding " + child_node.value)
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    # removes parent-child relationship
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

EU = TreeNode("Europe")
GER = TreeNode("Germany")
FRA = TreeNode("France")
ITA = TreeNode("Italy")
Dor = TreeNode("Dortmund")
Ber = TreeNode("Berlin")
Str = TreeNode("Strasburgo")
Mar = TreeNode("Marseille")
Mil = TreeNode("Milan")
Rom = TreeNode("Roma")

EU.add_child(GER)
EU.add_child(FRA)
EU.add_child(ITA)

GER.add_child(Dor)
GER.add_child(Ber)
FRA.add_child(Str)
FRA.add_child(Mar)
ITA.add_child(Mil)
ITA.add_child(Rom)

print("-------------------")
EU.traverse()

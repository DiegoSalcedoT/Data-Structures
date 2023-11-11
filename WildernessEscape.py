######
# TREENODE CLASS
######

class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    while len(story_node.choices) != 0:
      choice = int(input("Enter 1 or 2 to continue the story: "))
      if choice not in [1, 2]:
        print("Enter a valid value (1 or 2): ")
      else:
        chosen_index = choice - 1
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)
        story_node = chosen_child

######
# VARIABLES FOR TREE
######
Text1 = """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""

Text2 = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""

Text3 = """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""

Text4 = """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""

Text5 = """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
"""

Text6 = """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""

Text7 = """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""

######
# TESTING AREA
######
story_root = TreeNode(Text1)
choice_a = TreeNode(Text2)
choice_b = TreeNode(Text3)
choice_a_1 = TreeNode(Text4)
choice_a_2 = TreeNode(Text5)
choice_b_1 = TreeNode(Text6)
choice_b_2 = TreeNode(Text7)
story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

print(story_root.story_piece)
story_root.traverse()

'''

Height of tree & total num of nodes
N = 1+2^1+2^2+2^3+.....+2^(k-1)
k = log(n+1) <= log(n)+1

Complexity - O(log N)

'''

'''
Implement a binary tree using python, and show its usage with some examples
'''


class TreeNodeEx:
    def __init__(self, key_num=None):
        self.key_num = key_num
        self.left = None
        self.right = None

    ''''
    Tree structure:
    tree_tuple = ((1,3,None), 2, (None, 3, 4), 5, (6, 7, 8))
    ### 2 --> root node
    In each child nodes, center element is the node root
    So creating node with center element but then calling the create multi nodes function recursively
    to create rest of the nodes

    1st condition for recursion:
    data is of type tuple i.e has 3 elements for a complete node
    If node is None, then just assign None to node
    If node is a single element, then just create it
    '''

    def create_multi_nodes(self, data):
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNodeEx(data[1])
            node.left = self.create_multi_nodes(data[0])
            node.right = self.create_multi_nodes(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNodeEx(data)
        return node

    def create_tuple_from_tree(self, node):
        if isinstance(node, TreeNodeEx):
            if node.left is None and node.right is None:
                return node.key_num
            return (
                self.create_tuple_from_tree(node.left),
                node.key_num,
                self.create_tuple_from_tree(node.right)
            )

# node0 = TreeNodeEx(3)
# node1 = TreeNodeEx(4)
# node2 = TreeNodeEx(5)
# #print(node0.key_num, node1.key_num, node2.key_num)
#
# node0.left = node1
# node0.right = node2
#
# # Now can create a tree and assign the
# tree = node0
# print(tree.key_num, tree.left.key_num, tree.right.key_num)
#
#




####### Creating a tree from tuple #########
tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
multi_tree = TreeNodeEx.create_multi_nodes(TreeNodeEx(), tree_tuple)
print(multi_tree.key_num, multi_tree.left.key_num, multi_tree.right.key_num)
print(multi_tree.left.key_num, multi_tree.left.left.key_num)
print(multi_tree.right.key_num, multi_tree.right.left.key_num, multi_tree.right.right.key_num)

######### Converting a tree back to a tuple ##########
# tree_to_tuple = create_tuple_from_tree(multi_tree)
# print(tree_to_tuple)

def in_order_trav(node):
    if node is None:
        return []
    return (in_order_trav(node.left) + [node.key_num] + in_order_trav(node.right))


# in_order_trav_tup = in_order_trav(multi_tree)
# print(in_order_trav_tup)

def pre_order_trav(node):
    if node is None:
        return []
    return (
        # o/p for below:
        # (2, (3, (1, [], []), []), (5, (3, [], (4, [], [])), (7, (6, [], []), (8, [], []))))
        #node.key_num, pre_order_trav(node.left), pre_order_trav(node.right)
        [node.key_num] + pre_order_trav(node.left) + pre_order_trav(node.right)
    )

# pre_order_trav_tup = pre_order_trav(multi_tree)
# print(pre_order_trav_tup)

def post_order_trav(node):
    if node is None:
        return []
    return (
        post_order_trav(node.left) + post_order_trav(node.right) + [node.key_num]
    )

# post_order_trav_tup = post_order_trav(multi_tree)
# print(post_order_trav_tup)


'''
The height/depth of a BT is the length of the longest path from its root node to a leaf.
Considering root node as one step so adding 1 in return
Can be computed recursively
'''


def get_tree_ht(node):
    if node is None:
        return 0
    return 1 + max(get_tree_ht(node.left), get_tree_ht(node.right))


# tree_ht = get_tree_ht(multi_tree)
# print(tree_ht)

'''
Count the number of nodes on the left and right and then add them up excluding None
'''


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

#
# tree_sze = tree_size(multi_tree)
# print(tree_sze)
from collections import Counter

class Node():
    '''
        Description:
            Class for Node
        
        Params:
            char    : To store the character in string
            freq    : To store the frequency of character
            left    : To store the location of left child
            right   : To store the location of right child        
            
        Return:
            Node object with char, freq, left & right child
    '''
    
    def __init__(self, char = None, freq = None):
        self.char = char
        self.freq = freq    
        self.left = None
        self.right = None
        
def huffman_tree(frequency_List):
    '''
        Description:
            Function to build the huffman tree
        
        Params:
            frequency_List    : List of tuples containing frequencies of charactes.
            
        Return:
            Root node of huffman tree                 
    '''    
    
    # List of nodes created from all characters present in string.
    nodes = [Node(tupple[0], tupple[1]) for tupple in frequency_List]    
    
    # Loop to merge nodes & build tree till we have only one node left in list
    while len(nodes) > 1:
        
        # Sort current list with increasing order of frequency
        nodes = sorted(nodes, key=lambda x: x.freq)
        
        # Pop out first 2 least frequency nodes & make them as left child & right child node
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        # Create merged_node with frequecy as sum of frequency of left & right node;
        # assign left & right of merged node with left & right nodes selected in previous step
        merged_node = Node(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        
        # Append the newly created merged node into our nodes list
        nodes.append(merged_node)
        
        # repeat the process until we have only 1 node left, that will become our root node.
        
    # return the root node
    return nodes[0]   

def treeTraversal(node, currentCode, huffmanCode):
    '''     
        Description:
            Function to traverse tree & create huffman code
        
        Params:
            node        :   Current node we are traversing
            currentCode :   Code we have built for current leaf node
            huffmanCode :   Dictionary to store final huffman code
            
        Return:
            None                 
    '''
    
    # Check if node if leaf then return as traversal is completed.
    if node == None:
        return
    
    # If node is not leaf then store the currentCode as ket for currenct leaf Character
    if node.char:
            huffmanCode[node.char] = currentCode
            
    # Recurssive function to travel the tress for left child tree
    treeTraversal(node.left, currentCode + '0', huffmanCode)
    
    # Recurssive function to travel the tress for right child tree
    treeTraversal(node.right, currentCode + '1', huffmanCode)

if __name__ == '__main__':
    
    # Initiate dictionary to store the huffman code
    huffmanCode = {}
    
    # Initiate string for which we need to derive huffman code
    string = 'POORNIMAPATHAK'
    print('\n ', string)
    
    # Get dictionary with character as key frequency as value
    freq = dict(Counter(string)) 
    print("\n Given Frequency", freq)
        
    # Sort the dictionary based on frequency of characters
    freq = sorted(freq.items(), key=lambda x: x[1])        
    
    # Build the huffman tree
    rootNode = huffman_tree(freq)
    
    # Traverse the tree to get the huffman code
    treeTraversal(rootNode, '', huffmanCode)
    
    # Print the huffman code
    print('\n {}'.format(huffmanCode))

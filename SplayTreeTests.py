import unittest
from SplayTree import Splay

class SplayTreeTests( unittest.TestCase ):

    def test_splay_tree_simple( self ):
            
        # Initializes the splay tree
        tree = Splay()

        # Root should be None initially
        self.assertIsNone( tree.root, None ) 

        sample_values = [ 3, 6, 10, 34, 4, 7 ]

        # Insert all of the values in the csv file into our
        # splay tree
        for value in sample_values:
            tree.insert(value)

        # The root value should be the last item that you insert
        # into the tree
        self.assertEqual( tree.root.value,  7 )

    def test_splay_tree_num_children( self ):
        # Initializes the splay tree
        tree = Splay()

        sample_values = [ 3, 6, 10, 34, 4, 7, 20, 34 ]
        # Insert all of the values in the csv file into our
        # splay tree
        for value in sample_values:
            tree.insert(value)
        
        num_nodes = tree.print()

        self.assertEqual( num_nodes, 8 )


if __name__=='__main__':
    unittest.main
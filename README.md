## Splay Tree

# Description
This project is my rendition of a splay tree implementation. The splaying algorithm itself is taken from [here](https://en.wikipedia.org/wiki/Splay_tree). 

# Usage
Values can be inserted into the splay tree via a csv file. This csv value contains comma separated integer values (they do not need to be sorted).

To create the splay tree, run the following

```python3 main.py example_values.csv```

where example_values.csv contains the values described above, ex. "1, 2, 3, 4"

The splay tree will be constructed, then printed to the console. The format is "Value: <node_value>, Depth: <node_depth>"

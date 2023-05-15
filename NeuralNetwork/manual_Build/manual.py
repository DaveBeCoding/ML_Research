class Operation():                                                          
  2     def __init__(self, input_nodes = []):
  3         self.input_nodes = input_nodes
  4         self.ouput_nodes = []
  5 
  6         for node in input_nodes:
  7             node.output_nodes.append(self)

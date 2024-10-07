class graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list = {f'{i}': [] for i in range(0, vno)}
    def add_edge(self,u,v):
        if self.vertex_count < u < 0 or self.vertex_count < v < 0:
            return "Wrong Values of U and V passed"
        self.adj_list[f'{u}'].append(v) 
        self.adj_list[f'{v}'].append(u)
    
    def remove_edge(self,u,v):
        if self.vertex_count < u < 0 or self.vertex_count < v < 0:
            return "Wrong Values of U and V passed"    
        self.adj_list[f'{u}'].remove(v) 
        self.adj_list[f'{v}'].remove(u)      

    def has_edge(self,u,v):
        if self.vertex_count < u < 0 or self.vertex_count < v < 0:
            return "Wrong Values of U and V passed"  
        else:
            if v in self.adj_list[f'{u}']:
                print(f"{u} and {v} has an edge") 
            else:
                print("No Edge")        

    def print_adj_list(self):
        return self.adj_list
ob = graph(5)
ob.add_edge(2,1)
ob.add_edge(1,3)
print(ob.print_adj_list())
ob.remove_edge(1,3)
print(ob.print_adj_list())
ob.has_edge(1,2)
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        super().__init__(src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.__str__() + "->" + self.dest.__str__() + " (" + str(self.weight) + ")"

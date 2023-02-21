def dijkstra():

    pass


if __name__=="__main__":

    graph = {}
    graph["start"] = {}
    graph["a"] = {}
    graph["b"] = {}
    graph["fin"] = {}

    graph["a"]["fin"] = 1
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = float("inf")

    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None    

    print(graph)
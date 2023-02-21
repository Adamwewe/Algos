from collections import deque

def person_is_seller(name: str) -> bool:
    return name[-1]  == 'm'

def mongo_seller(search_queue, graph, searched):
    if search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("{} is a mongo seller!".format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
                return mongo_seller(search_queue, graph, searched)
    return False


if __name__ == "__main__":
    graph = {}
    graph["you"] = ["alice", "bobm", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggym"] = []
    graph["thom"] = []
    graph["jonny"] = []
    graph["anuj"] = []
    graph["claire"] = ["thom", "jonny"]

    search_queue = deque()
    search_queue += graph["you"]
    mongo_seller(search_queue=search_queue, 
        graph=graph, searched=[])
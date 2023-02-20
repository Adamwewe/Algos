from collections import deque

def person_is_seller(name: str) -> bool:
    return name[-1]  == 'm'

def mongo_seller():
    pass


if __name__ == "__main__":
    graph = {}
    search_queue = deque()

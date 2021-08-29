'''Breadth first search (BFS) tells you if there's a path from A to B.
If there's a path, BFS will find the shortest path.
Running time of BFS is O(v + E), V for the number of vertices and E for
the number of edges'''
from collections import deque

# dictionary to define the graph
graph = {}
graph["You"] = ["Nico", "Tod", "Sabella"]
graph["Nico"] = ["Montag", "Brian", "Ariel"]
graph["Brian"] = ["Jennie"]
graph["Tod"] = ["You", "Brian", "Adam"]


# someone is a mango seller if their name ends with 'm'
def is_mango_seller(person):
    return person[-1] == "m"

# keep a queue containing the people to check
# dequeue a person and check if that person ia a mango seller
# if the person is a mango seller you're done
# otherwise enqueue their neighbors and mark the person as searched
# keep looping, if the queue is empty, it means there are no mango sellers in your network
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue: 
        person = search_queue.popleft()
        if not person in searched:
            if is_mango_seller(person):
                return (True, person)
            else:
                if person in graph:
                    search_queue += graph[person]
                searched.append(person)
    return (False, None)

if __name__ == "__main__":
    mango_seller = search("You")
    print(f"Is there a mango seller in your network? {mango_seller[0]}, {mango_seller[1]}")

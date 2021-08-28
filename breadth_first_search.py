from collections import deque

graph = {}
graph["Celine"] = ["Nico", "Tod", "Sabella"]
graph["Nico"] = ["Montague", "Brian", "Ariel"]
graph["Brian"] = ["Jennie"]
graph["Tod"] = ["Celine", "Brian", "Adam"]


def is_mango_seller(person):
    return person[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue: 
        person = search_queue.popleft()
        if not person in searched:
            if is_mango_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                if person in graph:
                    search_queue += graph[person]
                searched.append(person)
    return False

if __name__ == "__main__":
    search("Celine")

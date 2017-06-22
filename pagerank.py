import random


class Pagerank(object):
    def __init__(self, links_file, pages_file):
        # self._vertex = 1483277
        # self._edge = 52973671
        self.links_file = links_file
        self.pages_file = pages_file
        self._jump = 15
        self._limit = 1000
        self._edge = sum(1 for line in open(links_file))
        self._vertex = sum(1 for line in open(pages_file))
        self.adjacency_list = {}
        self.visited = [0]*self._vertex

    def read(self):
        with open(self.links_file, "r") as file:
            for line in file:
                items = line[:-1].split()
                if items[0] in self.adjacency_list:
                    self.adjacency_list[items[0]].append(items[1])
                else:
                    self.adjacency_list[items[0]] = [items[1]]

    def surf(self):
        current = random.randint(0, (self._vertex-1))
        for i in range(self._limit):
            rand = random.randint(0, (self._vertex-1))
            if random.randint(0, 99) < self._jump:
                current = rand
            else:
                current = random.choice(self.adjacency_list.get(current, [rand]))
            self.visited[random.randint(0, (self._vertex-1))] += 1
        print(self.visited)


    def rank(self):
        pass


if __name__ == '__main__':
    pagerank = Pagerank("wikipedia_links/small_links.txt", "wikipedia_links/small_pages.txt")
    pagerank.read()
    pagerank.surf()

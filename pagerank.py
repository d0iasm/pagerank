class Pagerank(object):
    def __init__(self):
        self._vertex = 1483277
        self._edge = 52973671
        self.adjacency_list = {}

    def read(self):
        with open("wikipedia_links/links.txt", "r") as file:
            for line in file:
                lines = line[:-1].split('\t')
                if lines[0] in self.adjacency_list:
                    self.adjacency_list[lines[0]].append(lines[1])
                else:
                    self.adjacency_list[lines[0]] = [lines[1]]

if __name__ == '__main__':
    pagerank = Pagerank()

import matplotlib.pyplot as plt
import networkx as nx


class Bff(object):
    """
    https://code.google.com/codejam/contest/4304486/dashboard#s=p2
    """
    def __init__(self, filename):
        """ Initialize with the given filename.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass

    def draw(self, input):
        """ Draw the string that represents the bff network.

        The input string contains N integers F1, F2, ..., FN, where Fi is the student ID number of the BFF
        of the kid with student ID i.

        :param input: the string that represents the bff network.
        :return:
        """
        self._plot_graph(input)

    def _plot_graph(self, input):
        # Construct the directed graph
        bffs = [int(e.strip()) for e in input.split(' ')]
        nodes = [i+1 for i in xrange(len(bffs))]
        gr = nx.DiGraph()
        gr.add_nodes_from(nodes)
        gr.add_edges_from([e for e in zip(nodes, bffs)])

        nx.draw_networkx(gr)
        plt.savefig(self._filename)


def main():
    plot = Bff("bff.png")
    # plot.draw("2 1 6 3 8 4 6 5")
    plot.draw("6 1 6 5 4 1 5 10 3 7")
    pass


if __name__ == "__main__":
    main()
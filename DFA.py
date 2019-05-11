from ArtistConnections import Vertex, Edge
from SongLibrary import SongLibrary

class DFA:

    def __init__(self, s=None):
        # initializes vertices
        self.start = Vertex(0)
        self.v1 = Vertex(1)
        self.v2 = Vertex(2)
        self.v3 = Vertex(3)
        self.v4 = Vertex(4)
        self.v5 = Vertex(5)
        self.v6 = Vertex(6)
        self.v7 = Vertex(7)

    """
    Build the DFA graph from the figure in task 2
    """
    def build_DFA(self):
        # building graphs based on the given FSM
        self.start.addEdge(Edge('A', self.v1))
        self.v1.addEdge(Edge('A', self.v1))
        self.v1.addEdge(Edge('C', self.v2))
        self.v2.addEdge(Edge('A', self.v3))
        self.v3.addEdge(Edge('T', self.v1))
        self.v3.addEdge(Edge('C', self.v4))
        self.v4.addEdge(Edge('A', self.v5))
        self.v5.addEdge(Edge('T', self.v1))
        self.v5.addEdge(Edge('C', self.v4))
        self.v5.addEdge(Edge('G', self.v6))
        self.v6.addEdge(Edge('A', self.v7))
        self.v7.addEdge(Edge('A', self.v1))
        self.v7.addEdge(Edge('C', self.v2))
        self.v7.setAcceptingState() # sets the final vertex's state to be True
        return

    """
    Test whether the input sequence seq will be accepted by the state machine
    return True if accept
    """
    def testMatch(self, seq):
        # vertex is start
        v = self.start
        for c in seq:
            # takes each character in the string
            if v == None:
                return False
            v = v.followEdge(c)
            # follows the edge
        if v == None:
            return False
        if v.isAcceptingState:
            return True
        return False

    """
    Test whether the one suffix of the input sequence seq will be accepted by the state machine
    return the index position if accept
    return -1 if not accept
    """
    def testAccept(self, seq):
        # initializes the index as -1
        indx = -1
        for i in range(0, len(seq)):
            s = seq[i:len(seq)]
            # substring through the given sequence
            result = self.testMatch(s)
            if result:
                return i
        return indx

    """
    For every song in the song library array, test whether they will be accepted by the state machine
    Store the match index or -1 into the matchIndx array.
    Please make sure the order of songs in the songlibrary is the same as the input file
    """
    def testSongLibrary(self, song_lib):
        songArray = song_lib.songArray
        # stores the song Array
        matchIndx = []
        for i in songArray:
            DNA = i.DNA
            # appends each result of the DNA from testAccept method
            matchIndx.append(self.testAccept(DNA))
        return matchIndx


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':

    dfa = DFA()
    dfa.build_DFA()
    print(dfa.testAccept("AACACATCACAGA"))
    song_lib = SongLibrary()
    song_lib.loadLibrary()
    dfa.testSongLibrary(song_lib)

    print("finish")
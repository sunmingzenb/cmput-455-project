# Transposition table code from CMPUT 455 website
# Written by Martin Mueller

class TranspositionTable(object):
    def __init__(self):
        self.table = {}

    def __repr__(self):
        return self.table.__repr__()
        
    def store(self, code, score):
        self.table[code] = score
    
    def lookup(self, code):
        return self.table.get(code)
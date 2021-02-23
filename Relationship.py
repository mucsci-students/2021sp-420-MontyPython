class Relationship():
    def __init__(self, src, dst, typ, srcMult = 0, dstMult = 0):

        #src is the first class in the tuple key and dst is the scond class
        self.src = src
        self.dst = dst
        self.typ = typ

        #multplicity
        self.srcMult = srcMult
        self.dstMult = dstMult
             
    # Helper function for unit tests
    def getRelationshipTyp(self):
        return self.typ
    def getRelationshipSrc(self):
        return self.src
    def getRelationshipDst(self):
        return self.dst
    def getRelationshipDstMult(self):
        return self.dstMult
    def getRelationshipSrcMult(self):
        return self.srcMult

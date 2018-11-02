

class QuestionType(object):
    """
    Enum-workaround class: NL query types
    See See Damljanovic, D. (2011)
    """
    VOID, BOOLEAN, COUNT, BOW, = range(4)


class Query(object):
    def __init__(self, rawQuery):
        """
        Query (NL question) constructor
        """
        self.rawQuery = rawQuery
        self.questionType = QuestionType.VOID
        self.focus = None
        self.pocs = []
        self.tokens = []
        self.pt = None  # Syntax parse tree (PT) of type nltk.Tree
        self.answerType = None
        self.semanticConcepts = []
        self.annotations = []  # Annotations to be looked up in the ontology; they do *not* have to be in the KB
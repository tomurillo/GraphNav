""""
Graphic Navigator constants
"""

"""
Commonly used Namespaces
"""
VIS_NS = "http://www.semanticweb.org/ak116252/ontologies/2015/2/upper-visualization"
OWL_NS = "http://www.w3.org/2002/07/owl"
RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns"
RDFS_NS = "http://www.w3.org/2000/01/rdf-schema"
XML_NS = 'http://www.w3.org/XML/1998/namespace'
XSD_NS = 'http://www.w3.org/2001/XMLSchema'
PURL_NS_1 = 'http://purl.org/dc/elements/1.1'
PURL_NS_2 = 'http://purl.org/dc/terms'
COMMON_NS = [OWL_NS, RDFS_NS, RDF_NS, XML_NS, XSD_NS, PURL_NS_1, PURL_NS_2]

"""
Domains
"""
BAR_CHART = 'Bar Chart'

"""
Session variables
"""
SESS_QUERY = "user_query"
SESS_SUG_PAIR = "suggestion_pair"
SESS_CURR_NODES = "%s_current_nodes"
SESS_PREV_NODES = "%s_prev_nodes"
SESS_HOME_NODES = "%s_home_nodes"
SESS_USER_LABELS = "%s_user_labels"
SESS_SUMMARY = "%s_summary"


""" ------------------- """
""" NLI basic operators """
""" ------------------- """

"""Reserved words"""
NonTags = ['no', 'not', 'without', 'higher', 'than', 'more', 'at', 'and', 'or',
           'lower', 'least', 'a', 'the', 'number', 'of', 'exactly', 'average',
           'mean', 'mode', 'max', 'min', 'maximum', 'minimum', 'less', 'how', 'what',
           'count', 'many', 'sum', 'aggregate', 'this', 'that', 'in', 'out', 'highest',
           'most', 'lowest', 'least', 'min', 'max', 'minimum', 'maximum', 'range',
           'sort', 'reverse', 'inverse', 'compare', 'to', 'add', 'sub', 'mult',
           'div', 'subtract', 'divide', 'multiply', 'tally', 'split', 'deduct',
           'minus', 'plus']

"""Reserved Filters for navigation purposes"""
NavFilters = {'home_node' : 'Home_Node', 'last_node' : 'Last_Node',
              'home_bar' : 'Home_Node',  'current_node' : 'Current_Node',
              'current' : 'Current_Node',  'current_bar' : 'Current_Node',
              'last_bar' : 'Last_Node', 'previous_node' : 'Last_Node',
              'previous_bar' : 'Last_Node' }

""" Non-Contrasting Positive Coordinators """
NLNCPosCoordinators = set(['and'])

"""Logical negators"""
NLopNEG = set(['no', 'not', 'without'])

"""Sort reverse operators"""
NLsortOpNeg = set(["reverse", "inverse"])

"""Basic Arithmetic Operators"""
NLArithmeticBasicOp = {'add': 'add', 'subtract' : 'sub', 'divide': 'div',
                         'multiply': 'mul', 'sum' : 'add', 'tally' : 'add',
                         'deduct': 'sub', 'sub' : 'sub', 'split' : 'div',
                         'mult' : 'mul', 'div' : 'div'}

"""Basic Connectors of arithmetic operations"""
NLArithmeticOpConnector = ['to', 'from', 'and', 'minus', 'plus']
"""Arithmetic operation connectors that invert order of operands"""
NLArithmeticOpInvConnector = ['from']

"""Attribute value cardinal filters"""
NLAttrValCardFilterOp = {"higher than" : '>', "more than" : '>',
               "at least" : '>=', "lower than" : '<',
               "less than" : '<', "a number of" : '=', "exactly" : '='}

"""Derived Value Operators"""
NLDerivedValueOp = {"average" : "avg", "mean": "avg", "mode" : "mode",
                    "how many" : "count", "count" : "count", "value" : "val"}



"""Extreme Value Operators"""
LNAttrExtremeOp = {"highest":"max", "most":"max", "maximum":"max", "max":"max",
                   "lowest":"min","least":"min","minimum":"min","min":"min",
                   "range":"range"}
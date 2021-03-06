"""
Mapping constants
"""

from NLP.constants import *

TOKEN_IGNORE_LABELS = [DT_TREE_POS_TAG, PRP_TREE_POS_TAG, PRPDOLLAR_TREE_POS_TAG, IN_TREE_POS_TAG]

TOKEN_IGNORE_VERB_LABELS = [VB_TREE_POS_TAG, VBG_TREE_POS_TAG, VBZ_TREE_POS_TAG, VBP_TREE_POS_TAG, VBN_TREE_POS_TAG,
                            VBN_TREE_POS_TAG]

TOKEN_IGNORE_VERBS = ["do", "does", "did", "are", "were", "is", "has", "have", "had", "give", "show", "list"]


TOKEN_IGNORE_SP_ARTICLE = ["a", "an"]  # Articles that confuse Stanford Parser

TOKEN_IGNORE_PHRASE = [IN_TREE_POS_TAG]

TOKEN_IGNORE_WH_PHRASE = [WHADVP_TREE_POS_TAG, WHAVP_TREE_POS_TAG, WHADJP_TREE_POS_TAG, WHNP_TREE_POS_TAG, WHPP_TREE_POS_TAG]

TOKEN_IGNORE_WH_CHILD = [NN_TREE_POS_TAG, NNPS_TREE_POS_TAG, NNP_TREE_POS_TAG, NNS_TREE_POS_TAG, JJR_TREE_POS_TAG,
                         JJS_TREE_POS_TAG, JJ_TREE_POS_TAG]

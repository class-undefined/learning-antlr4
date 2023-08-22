# Generated from Data.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,2,23,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,1,
        1,1,1,1,2,1,2,1,2,5,2,18,8,2,10,2,12,2,21,9,2,1,2,0,0,3,0,2,4,0,
        0,21,0,7,1,0,0,0,2,11,1,0,0,0,4,19,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,
        0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,1,1,0,0,0,11,12,5,1,0,
        0,12,13,3,4,2,0,13,3,1,0,0,0,14,15,4,2,0,1,15,16,5,1,0,0,16,18,6,
        2,-1,0,17,14,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,
        5,1,0,0,0,21,19,1,0,0,0,2,9,19
    ]

class DataParser ( Parser ):

    grammarFileName = "Data.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "INT", "WS" ]

    RULE_data = 0
    RULE_group = 1
    RULE_sequence = 2

    ruleNames =  [ "data", "group", "sequence" ]

    EOF = Token.EOF
    INT=1
    WS=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DataParser.GroupContext)
            else:
                return self.getTypedRuleContext(DataParser.GroupContext,i)


        def getRuleIndex(self):
            return DataParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = DataParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.group()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._INT = None # Token

        def INT(self):
            return self.getToken(DataParser.INT, 0)

        def sequence(self):
            return self.getTypedRuleContext(DataParser.SequenceContext,0)


        def getRuleIndex(self):
            return DataParser.RULE_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup" ):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)




    def group(self):

        localctx = DataParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            localctx._INT = self.match(DataParser.INT)
            self.state = 12
            self.sequence((0 if localctx._INT is None else int(localctx._INT.text)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, n:int=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.n = None
            self.i = 1;
            self.n = n

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(DataParser.INT)
            else:
                return self.getToken(DataParser.INT, i)

        def getRuleIndex(self):
            return DataParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self, n:int):

        localctx = DataParser.SequenceContext(self, self._ctx, self.state, n)
        self.enterRule(localctx, 4, self.RULE_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 14
                    if not localctx.i<=localctx.n:
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "$i<=$n")
                    self.state = 15
                    self.match(DataParser.INT)
                    localctx.i+=1; 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.sequence_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def sequence_sempred(self, localctx:SequenceContext, predIndex:int):
            if predIndex == 0:
                return localctx.i<=localctx.n
         





from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):
   
    ''' topLevelDefinition'''
    @abstractmethod 
    def visitTopLevelDefinitionVariable(self, topLevelDefinitionVariable):
        pass

    @abstractmethod 
    def visitTopLevelDefinitionVariableRepetition(self, topLevelDefinitionVariableRepetition):
        pass

    @abstractmethod 
    def visitTopLevelDefinitionFunction(self, topLevelDefinitionFunction):
        pass

    @abstractmethod 
    def visitTopLevelDefinitionFunctionRepetition(self, topLevelDefinitionFunctionRepetition):
        pass


    ''' variableDeclaration'''
    @abstractmethod 
    def visitVariableDeclarationID(self, variableDeclarationID):
        pass

    @abstractmethod 
    def visitConcretevariableDeclaration(self, concretevariableDeclaration):
        pass


    ''' decIdentifier'''
    @abstractmethod 
    def visitDeclaredIdentifierType(self, declaredIdentifierType):
        pass


    ''' functionSignature '''
    @abstractmethod 
    def visitCallFormalParameterListId(self, callFormalParameterListId):
        pass
    
    @abstractmethod 
    def visitCallFormalParameterListvoidOrType(self, callFormalParameterListvoidOrType):
        pass
            

    ''' formalParameterList'''
    @abstractmethod 
    def visitCallNormalFormalParameters(self, callNormalFormalParameters):
        pass
    

    ''' normalFormalParameters '''
    @abstractmethod 
    def visitCallNormalFormalParameter(self, normalFormalParameter):
        pass
    
    @abstractmethod 
    def visitNormalFormalParametersRepetition(self, normalFormalParametersRepetition):
        pass
    

    ''' simlpleFormalParameter '''
    @abstractmethod 
    def visitCallVoidOrType(self, callVoidOrType):
        pass
    
    @abstractmethod 
    def visitCallParameterExpression(self, callParameterExpression):
        pass
        
        
    ''' FunctionBody '''
    @abstractmethod 
    def visitCallFunctionBody(self, callFunctionBody):
        pass
 

    ''' block '''
    @abstractmethod 
    def visitCallBlockStatements(self, callBlockStatements):
        pass


    ''' statements '''
    @abstractmethod 
    def visitConcretStatements(self, concretStatement):
        pass

    @abstractmethod 
    def visitConcretStatement(self, concretStatement):
        pass


    ''' statement'''
    @abstractmethod 
    def visitStatementNonLabelledStatement(self, statementNonLabelledStatement):
        pass


    ''' nonLabelledStatement'''
    @abstractmethod 
    def visitNonLabelledStatementblock(self, nonLabelledStatementblock):
        pass
    
    @abstractmethod 
    def visitLocalVariableDeclaration(self, localVariableDeclaration):
        pass
    
    @abstractmethod 
    def visitConcreteExpressionStatement(self, concreteExpressionStatement):
        pass

    @abstractmethod 
    def visitConcreteReturnStatement(self, concreteReturnStatement):
        pass
    
    @abstractmethod 
    def visitConcreteIfStatement(self, concreteIfStatement):
        pass
    
    @abstractmethod 
    def visitConcreteForStatement(self, concreteForStatement):
        pass

    @abstractmethod 
    def visitConcreteWhileStatement(self, concreteWhileStatement):
        pass

    @abstractmethod 
    def visitConcreteDoStatement(self, concreteDoStatement):
        pass

    @abstractmethod 
    def visitConcreteSwitchStatement(self, concreteSwitchStatement):
        pass

    @abstractmethod 
    def visitConcreteBreakStatement(self, concreteBreakStatement):
        pass


    ''' localVariableDeclaration'''
    @abstractmethod 
    def visitCallLocalInitializedVariableDeclaration(self, callLocalInitializedVariableDeclaration):
        pass
        

    ''' initializedVariableDeclaration '''
    @abstractmethod 
    def visitCallDeclaredIdentifier(self, callDeclaredIdentifier):
        pass

    @abstractmethod 
    def visitCallLiteralAtribuirExp(self, callLiteralAtribuirExp):
        pass

    @abstractmethod 
    def visitCallDeclaredInitializedIdentifier(self, callDeclaredInitializedIdentifier):
        pass
    
    @abstractmethod 
    def visitCalliniRepeticion(self, callIRepeticion):
        pass


    ''' expressionStatement '''
    @abstractmethod 
    def visitConcretexpression(self, concretexpression):
        pass


    '''expression '''
    @abstractmethod 
    def visitCallExpression(self, callExpression):
        pass


    ''' orExpression '''
    @abstractmethod 
    def visitCallandExpression(self, callandExpression):
        pass

    @abstractmethod 
    def visitExpressionORexpression(self, expressionORexpression):
        pass


    ''' andExpression '''
    @abstractmethod 
    def visitCalligualExpression(self, calligualExpression):
        pass
    
    @abstractmethod 
    def visitCallAndExpressionIgual(self, callAndExpressionIgual):
        pass

    
    ''' equalityExpression '''
    @abstractmethod 
    def visitCallRelacionalExpression(self, callRelacionalExpression):
        pass

    @abstractmethod 
    def visitCallEqualityExpression(self, callEqualityExpression):
        pass
        

    ''' relacionalExpression '''
    @abstractmethod 
    def visitCallUnary(self, callUnary):
        pass
        
    
    @abstractmethod 
    def visitCallConcretExpression(self, callConcretExpression):
        pass


    ''' addExpression '''
    @abstractmethod 
    def visitCallMultExpression(self, callMultExpression):
        pass
        
    @abstractmethod 
    def visitCallAddExpressionMult(self, callAddExpressionMult):
        pass
        

    ''' multExpression '''
    @abstractmethod 
    def visitCallUnaryExp(self, callUnaryExp):
        pass
    
    @abstractmethod 
    def visitCallUnaryExpMultExpression(self, callUnaryExpMultExpression):
        pass


    ''' unaryExpression '''
    @abstractmethod 
    def visitConcreteprimaryExpression(self, concreteprimaryExpression):
        pass
    
    @abstractmethod 
    def visitCallfunctioncall(self, callfunctioncall):
         pass

    @abstractmethod 
    def visitConcreteunaryExpression(self, concreteunaryExpression):
        pass


    ''' functionCall '''
    @abstractmethod 
    def visitConcretFunctionCall(self, concretFunctionCall):
        pass


    ''' primary '''
    @abstractmethod 
    def visitCallPrimaryLiteral(self, callPrimaryLiteral):
        pass
        
    @abstractmethod 
    def visitCallPrimaryExpression(self, callPrimaryExpression):
        pass


    ''' literal '''
    @abstractmethod 
    def visitCallLiteralListLiteralID(self, callLiteralListLiteral):
        pass

    def visitCallLiteralListLiteral(self, callLiteralListLiteral):
        pass

    @abstractmethod 
    def visitCallLiteralBooleanLiteral(self, callLiteralBooleanLiteral):
        pass

    @abstractmethod 
    def visitCallLiteralId(self, callLiteralId):
        pass
    
    @abstractmethod 
    def visitCallNum(self, callnum):
        pass
        
    @abstractmethod
    def visitCallLiteralString(self, callLiteralString):
        pass


    ''' listLiteral'''
    @abstractmethod 
    def visitExpressionListlistLiteral(self, expressionListlistLiteral):
        pass


    '''listLiteralID '''
    @abstractmethod 
    def visitCallListlistLiteralID(self, callListlistLiteralID):
        pass


    ''' booleanLiteral'''
    @abstractmethod 
    def visitbooleanLiteralTrue(self, booleanLiteralTrue):
        pass


    @abstractmethod 
    def visitbooleanLiteralFalse(self, booleanLiteralFalse):
        pass


    ''' expressionList'''
    @abstractmethod
    def visitConcreteExpression(self, concreteExpression):
        pass

    @abstractmethod 
    def visitCallExpressionList(self, callExpressionList):
        pass


    " ReturnStatementExpression "
    @abstractmethod 
    def visitReturnStatementExpression(self, returnStatementExpression):
        pass


    ''' ifStatement '''
    @abstractmethod 
    def visitIfexpressionStatement(self, ifexpressionStatement):
        pass

    @abstractmethod 
    def visitIfElseExpressionStatement(self, ifElseExpressionStatement):
        pass


    ''' forStatement '''
    @abstractmethod 
    def visitConcreteForLoopParts(self, concreteForLoopParts):
        pass   


    ''' forLoopParts '''
    @abstractmethod 
    def visitConcreteForInitializerStatement(self, concreteForInitializerStatement):
        pass

    @abstractmethod 
    def visitForInitializerStatementExpressionList(self, forInitializerStatementExpressionList):
        pass 

    @abstractmethod 
    def visitForInitializerStatementExpression(self, forInitializerStatementExpression):
        pass 

    @abstractmethod 
    def visitExpressionForInitializerStatementExpressionList(self, expressionForInitializerStatementExpressionList):
        pass       


    ''' forInitializerStatement '''
    @abstractmethod 
    def visitConcreteLocalVariableDeclaration(self, concreteLocalVariableDeclaration):
        pass    

    @abstractmethod 
    def visitCallConcreteExpression(self, callConcreteExpression):
        pass

   
    ''' whileStatement  '''
    @abstractmethod 
    def visitWhileStatementExpressionStatement(self, whileStatementExpressionStatement):
        pass


    ''' doStatement '''
    @abstractmethod 
    def visitDOStatementWhileExpression(self, DOStatementWhileExpression):
        pass


    ''' switchCaseRepetition '''
    @abstractmethod 
    def visitRepetitionSwitchCase(self, repetitionSwitchCase):
        pass
        
    @abstractmethod 
    def visitRepetitionSwitchCase2(self, repetitionSwitchCase2):
        pass


    ''' switchStatement '''
    @abstractmethod 
    def visitConcreteSwitch(self, concreteSwitch):
        pass
    
    @abstractmethod 
    def visitConcreteDefaultCase(self, concreteDefaultCase):
        pass


    ''' switchCase'''
    @abstractmethod 
    def visitExpressionSwitchCase(self, expressionSwitchCase):
        pass


    ''' defaultCase'''
    @abstractmethod 
    def visitDefaultStatements(self, defaultStatements):
        pass
    

    ''' break '''
    @abstractmethod 
    def visitCallBreak(self, callBreak):
        pass
    
    @abstractmethod
    def visitBreakID(self, breakID):
        pass



 
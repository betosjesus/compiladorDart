from abc import abstractmethod
from abc import ABCMeta
from DartVisitor import Visitor

''' topLevelDefinition e classes concretas '''
class topLevelDefinition(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class TopLevelDefinitionVariable(topLevelDefinition):
    def __init__(self, variableDeclaration):
        self.variableDeclaration = variableDeclaration
    def accept(self, visitor):
        return visitor.visitTopLevelDefinitionVariable(self)
        
class TopLevelDefinitionVariableRepetition(topLevelDefinition):
    def __init__(self, variableDeclaration, topLevel):
        self.variableDeclaration = variableDeclaration
        self.topLevel = topLevel
    def accept(self, visitor):
        return visitor.visitTopLevelDefinitionVariableRepetition(self)

class TopLevelDefinitionFunction(topLevelDefinition):
    def __init__(self, functionSignature, functionBody):
        self.functionSignature = functionSignature 
        self.functionBody = functionBody
    def accept(self, visitor):
        return visitor.visitTopLevelDefinitionFunction(self)

class TopLevelDefinitionFunctionRepetition(topLevelDefinition):
    def __init__(self, functionSignature, functionBody, topLevel):
        self.functionSignature = functionSignature 
        self.functionBody = functionBody
        self.topLevel = topLevel
    def accept(self, visitor):
        return visitor.visitTopLevelDefinitionFunctionRepetition(self)


''' variableDeclaration e classes concretas '''
class variableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class VariableDeclarationID(variableDeclaration):
    def __init__(self, declaredIdentifier):
        self.declaredIdentifier = declaredIdentifier
    def accept(self, visitor):
        return visitor.visitVariableDeclarationID(self)

class ConcretevariableDeclaration(variableDeclaration):
    def __init__(self, variableDeclaration, id):
        self.variableDeclaration = variableDeclaration
        self.id = id
    def accept(self, visitor):
        return visitor.visitConcretevariableDeclaration(self)

''' decIdentifier e classes concretas '''
class declaredIdentifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaredIdentifierType(declaredIdentifier):
    def __init__(self, voidOrType, id):
        self.voidOrType = voidOrType 
        self.id = id 
    def accept(self, visitor):
        return visitor.visitDeclaredIdentifierType(self)

class DeclaredIdentifierId(declaredIdentifier):
    def __init__(self, id):
        self.id = id 
    def accept(self, visitor):
        return visitor.visitDeclaredIdentifierId(self)

''' voidOrType e classes concretas '''
class voidOrType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteVoidOrType(voidOrType):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor):
        return visitor.visitConcreteVoidOrType(self)

# class VoidOrTypeV(voidOrType):
#     def __init__(self, void):
#         self.void = void
#     def accept(self, visitor):
#         return visitor.visitVoidOrTypeV(self)

''' functionSignature e classes concretas '''
class functionSignature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallFormalParameterListId(functionSignature):
    def __init__(self, id, formalParameterList):
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
        return visitor.visitCallFormalParameterListId(self)

class CallFormalParameterListvoidOrType(functionSignature):
    def __init__(self, voidOrType, id, formalParameterList):
        self.voidOrType = voidOrType
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
       return visitor.visitCallFormalParameterListvoidOrType(self)


''' formalParameterList e classes concretas '''
class formalParameterList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallNormalFormalParameters(formalParameterList):
    def __init__(self, normalFormalParameters):
        self.normalFormalParameters = normalFormalParameters
    def accept(self, visitor):
        return visitor.visitCallNormalFormalParameters(self)


''' normalFormalParameters e classes concretas '''
class normalFormalParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallNormalFormalParameter(normalFormalParameters):
    def __init__(self, simpleFormalParameter):
        self.simpleFormalParameter = simpleFormalParameter
    def accept(self, visitor):
        return visitor.visitCallNormalFormalParameter(self)

class NormalFormalParametersRepetition(normalFormalParameters):
    def __init__(self, simpleFormalParameter, normalFormalParameters):
        self.simpleFormalParameter = simpleFormalParameter
        self.normalFormalParameters = normalFormalParameters
    def accept(self, visitor):
        return visitor.visitNormalFormalParametersRepetition(self)
        
''' simlpleFormalParameter e classes concretas '''
class simlpleFormalParameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallVoidOrType(simlpleFormalParameter):
    def __init__(self, voidOrType, id):
        self.voidOrType = voidOrType
        self.id = id
    def accept(self, visitor):
        return visitor.visitCallVoidOrType(self)  

class CallParameterExpression(simlpleFormalParameter):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitCallParameterExpression(self)  
    

''' functionBody e classes concretas '''
class functionBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallFunctionBody(functionBody):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        return visitor.visitCallFunctionBody(self)


''' block e classes concretas '''
class block(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallBlockStatements(block):
    def __init__(self, statements):
        self.statements = statements
    def accept(self, visitor):
        return visitor.visitCallBlockStatements(self)


''' statements e classes concretas '''
class statements(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcretStatements(statements):
    def __init__(self, statement, statements):
        self.statement = statement
        self.statements = statements
    def accept(self, visitor):
        return visitor.visitConcretStatements(self)

class ConcretStatement(statements):
    def __init__(self, statement):
        self.statement = statement
    def accept(self, visitor):
        return visitor.visitConcretStatement(self)


''' statement e classes concretas '''
class statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class StatementNonLabelledStatement(statement):
    def __init__(self, nonLabelledStatement):
        self.nonLabelledStatement = nonLabelledStatement
    def accept(self, visitor):
        return visitor.visitStatementNonLabelledStatement(self)


''' nonLabelledStatement e classes concretas '''
class nonLabelledStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class  ConcreteExpressionStatement(nonLabelledStatement):
    def __init__(self, expressionStatement):
        self.expressionStatement = expressionStatement
    def accept(self, visitor):
        return visitor.visitConcreteExpressionStatement(self)

class NonLabelledStatementblock(nonLabelledStatement):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        return visitor.visitNonLabelledStatementblock(self)

class LocalVariableDeclaration(nonLabelledStatement):
    def __init__(self, localVariableDeclaration):
        self.localVariableDeclaration = localVariableDeclaration
    def accept(self, visitor):
        return visitor.visitLocalVariableDeclaration(self)

class  ConcreteReturnStatement(nonLabelledStatement):
    def __init__(self, returnStatement):
        self.returnStatement = returnStatement
    def accept(self, visitor):
        return visitor.visitConcreteReturnStatement(self)

class ConcreteIfStatement(nonLabelledStatement):
    def __init__(self, ifStatement):
        self.ifStatement = ifStatement
    def accept(self, visitor):
        return visitor.visitConcreteIfStatement(self)

class ConcreteForStatement(nonLabelledStatement):
    def __init__(self, forStatement):
        self.forStatement = forStatement
    def accept(self, visitor):
        return visitor.visitConcreteForStatement(self)

class ConcreteWhileStatement(nonLabelledStatement):
    def __init__(self, whileStatement):
        self.whileStatement = whileStatement
    def accept(self, visitor):
        return visitor.visitConcreteWhileStatement(self)

class  ConcreteDoStatement(nonLabelledStatement):
    def __init__(self, doStatement):
        self.doStatement = doStatement
    def accept(self, visitor):
        return visitor.visitConcreteDoStatement(self)
    
class ConcreteSwitchStatement(nonLabelledStatement):
    def __init__(self, switchStatement):
        self.switchStatement = switchStatement
    def accept(self, visitor):
        return visitor.visitConcreteSwitchStatement(self)

class ConcreteBreakStatement(nonLabelledStatement):
    def __init__(self, breakStatement):
        self.breakStatement = breakStatement
    def accept(self, visitor):
        return visitor.visitConcreteBreakStatement(self)


''' localVariableDeclaration e classes concretas '''
class localVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallLocalInitializedVariableDeclaration(localVariableDeclaration):
    def __init__(self, initializedVariableDeclaration):
        self.initializedVariableDeclaration = initializedVariableDeclaration
    def accept(self, visitor):
        return visitor.visitCallLocalInitializedVariableDeclaration(self)


''' initializedVariableDeclaration e classes concretas '''
class initializedVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallDeclaredIdentifier(initializedVariableDeclaration):
    def __init__(self, declaredIdentifier):
        self.declaredIdentifier = declaredIdentifier
    def accept(self, visitor):
        return visitor.visitCallDeclaredIdentifier(self)

class CallDeclaredInitializedIdentifier(initializedVariableDeclaration):
    def __init__(self, declaredIdentifier, expression):
        self.declaredIdentifier = declaredIdentifier
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitCallDeclaredInitializedIdentifier(self)

class CallDeclaredInitializedIdentifierListLiteral(initializedVariableDeclaration):
    def __init__(self, declaredIdentifier, listLiteral):
        self.declaredIdentifier = declaredIdentifier
        self.listLiteral = listLiteral
    def accept(self, visitor):
        return visitor.visitCallDeclaredInitializedIdentifierListLiteral(self)

class CallIdListIdAtribuirExpression(initializedVariableDeclaration):
    def __init__(self, listLiteralID, expression):
        self.listLiteralID = listLiteralID
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitCallIdListAtribuirIdList(self)


''' expressionStatement e classes concretas '''
class expressionStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class Concretexpression(expressionStatement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitConcretexpression(self)


''' expression e classes concretas '''
class expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallExpression(expression):
    def __init__(self, orExpression):
        self.orExpression = orExpression
    def accept(self, visitor):
        return visitor.visitCallExpression(self)


''' orExpression e classes concretas '''
class orExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallandExpression(orExpression):
    def __init__(self, andExpression):
        self.andExpression = andExpression
    def accept(self, visitor):
        return visitor.visitCallandExpression(self)
        
class ExpressionORexpression(orExpression):
    def __init__(self, orExpression, operation, andExpression):
        self.orExpression = orExpression
        self.operation = operation
        self.andExpression = andExpression
    def accept(self, visitor):
        return visitor.visitExpressionORexpression(self)


''' andExpression e classes concretas '''
class andExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CalligualExpression(andExpression):
    def __init__(self, equalityExpression):
        self.equalityExpression = equalityExpression
    def accept(self, visitor):
        return visitor.visitCalligualExpression(self)

class CallAndExpressionIgual(andExpression):
    def __init__(self, andExpression, operation, equalityExpression):
        self.andExpression = andExpression
        self.operation = operation
        self.equalityExpression = equalityExpression
    def accept(self, visitor):
        return visitor.visitCallAndExpressionIgual(self)


''' equalityExpression e classes concretas '''
class equalityExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallRelacionalExpression(equalityExpression):
    def __init__(self, relacionalExpression):
        self.relacionalExpression = relacionalExpression
    def accept(self, visitor):
        return visitor.visitCallRelacionalExpression(self)

class CallEqualityExpression(equalityExpression):
    def __init__(self, equalityExpression, operation, relacionalExpression):
        self.equalityExpression = equalityExpression
        self.operation = operation
        self.relacionalExpression = relacionalExpression
    def accept(self, visitor):
        return visitor.visitCallEqualityExpression(self)


''' relacionalExpression e classes concretas '''
class relacionalExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallUnary(relacionalExpression):
    def __init__(self, addExpression):
        self.addExpression = addExpression
    def accept(self, visitor):
        return visitor.visitCallUnary(self)
    
class CallConcretExpression(relacionalExpression):
    def __init__(self, relacionalExpression, operation, addExpression):
        self.relacionalExpression = relacionalExpression
        self.operation = operation
        self.addExpression = addExpression
    def accept(self, visitor):
        return visitor.visitCallConcretExpression(self)


''' addExpression e classes concretas '''
class addExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallMultExpression(addExpression):
    def __init__(self, multExpression):
        self.multExpression = multExpression
    def accept(self, visitor):
        return visitor.visitCallMultExpression(self)

class CallAddExpressionMult(addExpression):
    def __init__(self, addExpression, operation, multExpression):
        self.addExpression = addExpression
        self.operation = operation
        self.multExpression = multExpression
    def accept(self, visitor):
        return visitor.visitCallAddExpressionMult(self)

''' multExpression e classes concretas '''
class multExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallUnaryExp(multExpression):
    def __init__(self, unaryExpression):
        self.unaryExpression = unaryExpression
    def accept(self, visitor):
        return visitor.visitCallUnaryExp(self)

class CallUnaryExpMultExpression(multExpression):
    def __init__(self, multExpression, operation, unaryExpression):
        self.multExpression = multExpression
        self.operation = operation
        self.unaryExpression = unaryExpression
    def accept(self, visitor):
        return visitor.visitCallUnaryExpMultExpression(self)


''' unaryExpression e classes concretas '''
class unaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcreteprimaryExpression(unaryExpression):
    def __init__(self, primary):
        self.primary = primary
    def accept(self, visitor):
        return visitor.visitConcreteprimaryExpression(self)

class Callfunctioncall(unaryExpression):
    def __init__(self, functionCall):
        self.functionCall = functionCall
    def accept(self, visitor):
        return visitor.visitCallfunctioncall(self)

class ConcreteunaryExpression(unaryExpression):
    def __init__(self, unaryExpression, operation):
        self.unaryExpression = unaryExpression
        self.operation = operation
    def accept(self, visitor):
        return visitor.visitConcreteunaryExpression(self)


''' functionCall e classes concretas '''
class functionCall(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcretFunctionCall(functionCall):
    def __init__(self, functionSignature):
        self.functionSignature = functionSignature
    def accept(self, visitor):
        return visitor.visitConcretFunctionCall(self)


''' primary e classes concretas '''
class primary(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
        
class CallPrimaryLiteral(primary):
    def __init__(self, literal):
        self.literal = literal
    def accept(self, visitor):
        return visitor.visitCallPrimaryLiteral(self)

class CallPrimaryExpression(primary):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitCallPrimaryExpression(self)

''' literal e classes concretas '''
class literal(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallLiteralListLiteralID(literal):
    def __init__(self, listLiteral):
        self.listLiteralID = listLiteralID
    def accept(self, visitor):
        return visitor.visitCallLiteralListLiteralID(self)

class CallLiteralBooleanLiteral(literal):
    def __init__(self, booleanLiteral):
        self.booleanLiteral = booleanLiteral
    def accept(self, visitor):
        return visitor.visitCallLiteralBooleanLiteral(self)

class CallLiteralId(literal):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitCallLiteralId(self)

class CallNum(literal):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor):
        return visitor.visitCallNum(self)

''' listLiteral e classes concretas '''
class listLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressionListlistLiteral(listLiteral):
    def __init__(self, expressionList):
        self.expressionList = expressionList
    def accept(self, visitor):
        return visitor.visitExpressionListlistLiteral(self)


'''listLiteralID e classes concretas '''
class listLiteralID(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallListlistLiteralID(listLiteral):
    def __init__(self, id, listLiteral):
        self.id = id
        self.listLiteral = listLiteral
    def accept(self, visitor):
        return visitor.visitCallListlistLiteralID(self)


''' booleanLiteral e classes concretas '''
class booleanLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class booleanLiteralTrue(booleanLiteral):
    def __init__(self, true):
        self.true = true
    def accept(self, visitor):
        return visitor.visitbooleanLiteralTrue(self)

class booleanLiteralFalse(booleanLiteral):
    def __init__(self, false):
        self.false = false
    def accept(self, visitor):
        return visitor.visitbooleanLiteralFalse(self)


''' expressionList e classes concretas '''
class expressionList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteExpression(expressionList):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitConcreteExpression(self)

class CallExpressionList(expressionList):
    def __init__(self, expression, expressionList):
        self.expression = expression
        self.expressionList = expressionList
    def accept(self, visitor):
        return visitor.visitCallExpressionList(self)


''' returnStatement e classes concretas '''            
class returnStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ReturnStatementExpression(returnStatement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitReturnStatementExpression(self)


''' ifStatement e classes concretas '''
class ifStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class IfexpressionStatement(ifStatement):
    def __init__(self, IF, expression, statement):
        self.IF = IF
        self.expression = expression
        self.statement = statement
    def accept(self, visitor):
        return visitor.visitIfexpressionStatement(self)
    
class IfElseExpressionStatement(ifStatement):
    def __init__(self, IF, expression, statement, ELSE, statement01):
        self.IF = IF
        self.expression = expression
        self.statement = statement
        self.ELSE = ELSE
        self.statement01 = statement01
    def accept(self, visitor):
        return visitor.visitIfElseExpressionStatement(self)


''' forStatement e classes concretas '''
class forStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcreteForLoopParts(forStatement):
    def __init__(self, FOR, forLoopParts, statement):
        self.FOR = FOR
        self.forLoopParts = forLoopParts
        self.statement = statement
    def accept(self, visitor):
        return visitor.visitConcreteForLoopParts(self)


''' forLoopParts e classes concretas '''
class forLoopParts(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcreteForInitializerStatement(forLoopParts):
    def __init__(self, forInitializerStatement):
        self.forInitializerStatement = forInitializerStatement
    def accept(self, visitor):
        return visitor.visitConcreteForInitializerStatement(self)
    
class ForInitializerStatementExpressionList(forLoopParts):
    def __init__(self, forInitializerStatement, expressionList):
        self.forInitializerStatement = forInitializerStatement
        self.expressionList = expressionList
    def accept(self, visitor):
        return visitor.visitForInitializerStatementExpressionList(self)
    
class ForInitializerStatementExpression(forLoopParts):
    def __init__(self, forInitializerStatement, expression):
        self.forInitializerStatement = forInitializerStatement
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitForInitializerStatementExpression(self)
    
class ExpressionForInitializerStatementExpressionList(forLoopParts):
    def __init__(self, forInitializerStatement, expression, expressionList):
        self.forInitializerStatement = forInitializerStatement
        self.expression = expression
        self.expressionList = expressionList
    def accept(self, visitor):
        return visitor.visitExpressionForInitializerStatementExpressionList(self)


''' forInitializerStatement e classes concretas '''
class forInitializerStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcreteLocalVariableDeclaration(forInitializerStatement):
    def __init__(self, localVariableDeclaration):
        self.localVariableDeclaration = localVariableDeclaration
    def accept(self, visitor):
        return visitor.visitConcreteLocalVariableDeclaration(self)

class CallConcreteExpression(forInitializerStatement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitCallConcreteExpression(self)


''' whileStatement e classes concretas '''
class whileStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class WhileStatementExpressionStatement(whileStatement):
    def __init__(self, WHILE, expression, statement):
        self.WHILE = WHILE
        self.expression = expression
        self.statement = statement
    def accept(self, visitor):
        return visitor.visitWhileStatementExpressionStatement(self)
        
''' doStatement e classes concretas '''
class doStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class DOStatementWhileExpression(doStatement):
    def __init__(self, DO, statement,  WHILE,expression):
        self.DO = DO
        self.statement = statement
        self.WHILE = WHILE
        self.expression = expression
    def accept(self, visitor):
        return visitor.visitDOStatementWhileExpression(self)


''' switchStatement e classes concretas '''
class switchStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcreteSwitch(switchStatement):
    def __init__(self, switch, expression, switchCaseRepetition):
        self.switch = switch
        self.expression = expression
        self.switchCaseRepetition = switchCaseRepetition
    def accept(self, visitor):
        return visitor.visitConcreteSwitch(self)

class ConcreteDefaultCase(switchStatement):
    def __init__(self, switch, expression, switchCaseRepetition, defaultCase):
        self.switch = switch
        self.expression = expression
        self.switchCaseRepetition = switchCaseRepetition
        self.defaultCase = defaultCase
    def accept(self, visitor):
        return visitor.visitConcreteDefaultCase(self)


''' switchCaseRepetition e classes concretas '''
class switchCaseRepetition(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class RepetitionSwitchCase(switchCaseRepetition):
    def __init__(self, switchCase, switchCaseRepetition):
        self.switchCase = switchCase
        self.switchCaseRepetition = switchCaseRepetition
    def accept(self, visitor):
        return visitor.visitRepetitionSwitchCase(self)

class RepetitionSwitchCase2(switchCaseRepetition):
    def __init__(self, switchCase):
        self.switchCase = switchCase
    def accept(self, visitor):
        return visitor.visitRepetitionSwitchCase2(self)


''' switchCase e classes concretas '''
class switchCase(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ExpressionSwitchCase(switchCase):
    def __init__(self, CASE, expression, statements):
        self.CASE = CASE
        self.expression = expression
        self.statements = statements
    def accept(self, visitor):
        return visitor.visitExpressionSwitchCase(self)
        
class LabelSwitchCase(switchCase):
    def __init__(self, label, switchCase):
        self.label = label
        self.switchCase = switchCase
    def accept(self, visitor):
        return visitor.visitLabelSwitchCase(self)
   
''' defaultCase e classes concretas '''
class defaultCase(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DefaultStatements(defaultCase):
    def __init__(self, default, statements):
        self.default = default
        self.statements = statements
    def accept(self, visitor):
        return visitor.visitDefaultStatements(self)

class LabelDefaultCase(defaultCase):
    def __init__(self, label, defaultCase):
        self.label = label
        self.defaultCase = defaultCase
    def accept(self, visitor):
        return visitor.visitLabelDefaultCase(self)
        
        
''' label e classes concretas '''            
class label(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class IdPontos(label):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitIdPontos(self)

''' break e classes concretas '''
class BreakStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallBreak(switchCase):
    def __init__(self, BREAK):
        self.BREAK = BREAK
    def accept(self, visitor):
        return visitor.visitCallBreak(self)

class BreakID(switchCase):
    def __init__(self, BREAK, id):
        self.BREAK = BREAK
        self.id = id
    def accept(self, visitor):
        return visitor.visitBreakID(self)
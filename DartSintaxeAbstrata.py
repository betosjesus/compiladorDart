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
        visitor.visitTopLevelDefinitionVariable(self)
        
class TopLevelDefinitionVariableRepetition(topLevelDefinition):
    def __init__(self, variableDeclaration, topLevel):
        self.variableDeclaration = variableDeclaration
        self.topLevel = topLevel
    def accept(self, visitor):
        visitor.visitTopLevelDefinitionVariableRepetition(self)

class TopLevelDefinitionFunction(topLevelDefinition):
    def __init__(self, functionSignature, functionBody):
        self.functionSignature = functionSignature 
        self.functionBody = functionBody
    def accept(self, visitor):
        visitor.visitTopLevelDefinitionFunction(self)

class TopLevelDefinitionFunctionRepetition(topLevelDefinition):
    def __init__(self, functionSignature, functionBody, topLevel):
        self.functionSignature = functionSignature 
        self.functionBody = functionBody
        self.topLevel = topLevel
    def accept(self, visitor):
        visitor.visitTopLevelDefinitionFunctionRepetition(self)


''' variableDeclaration e classes concretas '''
class variableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class VariableDeclarationID(variableDeclaration):
    def __init__(self, declaredIdentifier):
        self.declaredIdentifier = declaredIdentifier
    def accept(self, visitor):
        visitor.visitVariableDeclarationID(self)

class ConcretevariableDeclaration(variableDeclaration):
    def __init__(self, variableDeclaration, id):
        self.variableDeclaration = variableDeclaration
        self.id = id
    def accept(self, visitor):
        visitor.visitConcretevariableDeclaration(self)

''' decIdentifier e classes concretas '''
class declaredIdentifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class DeclaredIdentifierId(declaredIdentifier):
    def __init__(self, voidOrType, id):
        self.voidOrType = voidOrType 
        self.id = id 
    def accept(self, visitor):
        visitor.visitDeclaredIdentifierId(self)

''' voidOrType e classes concretas '''
class voidOrType(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class VoidOrType(voidOrType):
    def __init__(self, type):
        self.type = type
    def accept(self, visitor):
        visitor.visitVoidOrType(self)

class VoidOrTypeV(voidOrType):
    def __init__(self, void):
        self.void = void
    def accept(self, visitor):
        visitor.visitVoidOrTypeV(self)

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
        visitor.visitCallFormalParameterListId(self)

class CallFormalParameterListvoidOrType(functionSignature):
    def __init__(self, voidOrType, id, formalParameterList):
        self.voidOrType = voidOrType
        self.id = id
        self.formalParameterList = formalParameterList
    def accept(self, visitor):
       visitor.visitCallFormalParameterListvoidOrType(self)


''' formalParameterList e classes concretas '''
class formalParameterList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallNormalFormalParameters(formalParameterList):
    def __init__(self, normalFormalParameters):
        self.normalFormalParameters = normalFormalParameters
    def accept(self, visitor):
        visitor.visitCallNormalFormalParameters(self)


''' normalFormalParameters e classes concretas '''
class normalFormalParameters(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallNormalFormalParameter(normalFormalParameters):
    def __init__(self, simpleFormalParameter):
        self.simpleFormalParameter = simpleFormalParameter
    def accept(self, visitor):
        visitor.visitCallNormalFormalParameter(self)

class NormalFormalParametersRepetition(normalFormalParameters):
    def __init__(self, simpleFormalParameter, normalFormalParameters):
        self.simpleFormalParameter = simpleFormalParameter
        self.normalFormalParameters = normalFormalParameters
    def accept(self, visitor):
        visitor.visitNormalFormalParametersRepetition(self)
        
''' simlpleFormalParameter e classes concretas '''
class simlpleFormalParameter(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallFinalConstVarOrTypeId(simlpleFormalParameter):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, visitor):
        visitor.visitCallFinalConstVarOrTypeId(self)  

class CallVoidOrType(simlpleFormalParameter):
    def __init__(self, voidOrType, ID):
        self.voidOrType = voidOrType
        self.ID = ID
    def accept(self, visitor):
        visitor.visitCallVoidOrType(self)  

class CallParameterExpression(simlpleFormalParameter):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        visitor.visitCallParameterExpression(self)  
    

''' functionBody e classes concretas '''
class functionBody(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallFunctionBody(functionBody):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        visitor.visitCallFunctionBody(self)


''' block e classes concretas '''
class block(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallBlockStatements(block):
    def __init__(self, statements):
        self.statements = statements
    def accept(self, visitor):
        visitor.visitCallBlockStatements(self)


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
        visitor.visitConcretStatements(self)

class ConcretStatement(statements):
    def __init__(self, statement):
        self.statement = statement
    def accept(self, visitor):
        visitor.visitConcretStatement(self)


''' statement e classes concretas '''
class statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class StatementNonLabelledStatement(statement):
    def __init__(self, nonLabelledStatement):
        self.nonLabelledStatement = nonLabelledStatement
    def accept(self, visitor):
        visitor.visitStatementNonLabelledStatement(self)


''' nonLabelledStatement e classes concretas '''
class nonLabelledStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class  ConcreteExpressionStatement(nonLabelledStatement):
    def __init__(self, expressionStatement):
        self.expressionStatement = expressionStatement
    def accept(self, visitor):
        visitor.visitConcreteExpressionStatement(self)

class NonLabelledStatementblock(nonLabelledStatement):
    def __init__(self, block):
        self.block = block
    def accept(self, visitor):
        visitor.visitNonLabelledStatementblock(self)

class LocalVariableDeclaration(nonLabelledStatement):
    def __init__(self, localVariableDeclaration):
        self.localVariableDeclaration = localVariableDeclaration
    def accept(self, visitor):
        visitor.visitLocalVariableDeclaration(self)

class  ConcreteReturnStatement(nonLabelledStatement):
    def __init__(self, returnStatement):
        self.returnStatement = returnStatement
    def accept(self, visitor):
        visitor.visitConcreteReturnStatement(self)

class ConcreteIfStatement(nonLabelledStatement):
    def __init__(self, ifStatement):
        self.ifStatement = ifStatement
    def accept(self, visitor):
        visitor.visitConcreteIfStatement(self)

class ConcreteForStatement(nonLabelledStatement):
    def __init__(self, forStatement):
        self.forStatement = forStatement
    def accept(self, visitor):
        visitor.visitConcreteForStatement(self)

class ConcreteWhileStatement(nonLabelledStatement):
    def __init__(self, whileStatement):
        self.whileStatement = whileStatement
    def accept(self, visitor):
        visitor.visitConcreteWhileStatement(self)

class  ConcreteDoStatement(nonLabelledStatement):
    def __init__(self, doStatement):
        self.doStatement = doStatement
    def accept(self, visitor):
        visitor.visitConcreteDoStatement(self)
    
class ConcreteSwitchStatement(nonLabelledStatement):
    def __init__(self, switchStatement):
        self.switchStatement = switchStatement
    def accept(self, visitor):
        visitor.visitConcreteSwitchStatement(self)

class ConcreteBreakStatement(nonLabelledStatement):
    def __init__(self, breakStatement):
        self.breakStatement = breakStatement
    def accept(self, visitor):
        visitor.visitConcreteBreakStatement(self)


''' localVariableDeclaration e classes concretas '''
class localVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallLocalInitializedVariableDeclaration(localVariableDeclaration):
    def __init__(self, initializedVariableDeclaration):
        self.initializedVariableDeclaration = initializedVariableDeclaration
    def accept(self, visitor):
        visitor.visitCallLocalInitializedVariableDeclaration(self)


''' initializedVariableDeclaration e classes concretas '''
class initializedVariableDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallDeclaredIdentifier(initializedVariableDeclaration):
    def __init__(self, declaredIdentifier):
        self.declaredIdentifier = declaredIdentifier
    def accept(self, visitor):
        visitor.visitCallDeclaredIdentifier(self)

class CallVarExpression(initializedVariableDeclaration):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        visitor.visitCallVarExpression(self)

class CallDeclaredInitializedIdentifier(initializedVariableDeclaration):
    def __init__(self, declaredIdentifier, expression):
        self.declaredIdentifier = declaredIdentifier
        self.expression = expression
    def accept(self, visitor):
        visitor.visitCallDeclaredInitializedIdentifier(self)

class CallDeclaredIdentifierComma(initializedVariableDeclaration):
    def __init__(self, declaredIdentifier, expression, initializedVariableDeclaration):
        self.declaredIdentifier = declaredIdentifier
        self.expression = expression
        self.initializedVariableDeclaration = initializedVariableDeclaration
    def accept(self, visitor):
        visitor.visitCallDeclaredIdentifierComma(self)

class CallDeclaredIdentifierIniti(initializedVariableDeclaration):
    def __init__(self, declaredIdentifier, initializedVariableDeclaration):
        self.declaredIdentifier = declaredIdentifier
        self.initializedVariableDeclaration = initializedVariableDeclaration
    def accept(self, visitor):
        visitor.visitCallDeclaredIdentifierIniti(self)

class DeclaredIdCommaInit(initializedVariableDeclaration):
    def __init__(self, id, initializedVariableDeclaration):
        self.id = id
        self.initializedVariableDeclaration = initializedVariableDeclaration
    def accept(self, visitor):
        visitor.visitDeclaredIdCommaInit(self)

class IdInit(initializedVariableDeclaration):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
    def accept(self, visitor):
        visitor.visitIdInit(self)

class IdAtribuirList(initializedVariableDeclaration):
    def __init__(self, id, id2, listLiteral):
        self.id = id
        self.id2 = id2
        self.listLiteral = listLiteral
    def accept(self, visitor):
        visitor.visitIdAtribuirList(self)

class IdListLiteral(initializedVariableDeclaration):
    def __init__(self, id, listLiteral, expression):
        self.id = id
        self.listLiteral = listLiteral
        self.expression = expression
    def accept(self, visitor):
        visitor.visitIdListLiteral(self)

class ConcreteIdInit(initializedVariableDeclaration):
    def __init__(self, id, expression, initializedVariableDeclaration):
        self.id = id
        self.expression = expression
        self.initializedVariableDeclaration = initializedVariableDeclaration
    def accept(self, visitor):
        visitor.visitConcreteIdInit(self)

class IdInitList(initializedVariableDeclaration):
    def __init__(self, declaredIdentifier, listLiteral, expression):
        self.declaredIdentifier = declaredIdentifier
        self.listLiteral = listLiteral
        self.expression = expression
    def accept(self, visitor):
        visitor.visitIdInitList(self)


''' expressionStatement e classes concretas '''
class expressionStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class Concretexpression(expressionStatement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        visitor.visitConcretexpression(self)


''' expression e classes concretas '''
class expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallExpression(expression):
    def __init__(self, constantExpression):
        self.constantExpression = constantExpression
    def accept(self, visitor):
        visitor.visitCallExpression(self)

''' constantExpression e classes concretas '''
class constantExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallConstantExpression(constantExpression):
    def __init__(self, orExpression):
        self.orExpression = orExpression
    def accept(self, visitor):
        visitor.visitCallConstantExpression(self)


''' orExpression e classes concretas '''
class orExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallandExpression(orExpression):
    def __init__(self, andExpression):
        self.andExpression = andExpression
    def accept(self, visitor):
        visitor.visitCallandExpression(self)
        
class ExpressionORexpression(orExpression):
    def __init__(self, orExpression, operation, andExpression):
        self.orExpression = orExpression
        self.operation = operation
        self.andExpression = andExpression
    def accept(self, visitor):
        visitor.visitExpressionORexpression(self)


''' andExpression e classes concretas '''
class andExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CalligualExpression(andExpression):
    def __init__(self, igualExpression):
        self.igualExpression = igualExpression
    def accept(self, visitor):
        visitor.visitCalligualExpression(self)

class CallAndExpressionIgual(andExpression):
    def __init__(self, andExpression, operation, igualExpression):
        self.andExpression = andExpression
        self.operation = operation
        self.igualExpression = igualExpression
    def accept(self, visitor):
        visitor.visitCallAndExpressionIgual(self)


''' igualExpression e classes concretas '''
class igualExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CalldiferenteExpression(igualExpression):
    def __init__(self, diferenteExpression):
        self.diferenteExpression = diferenteExpression
    def accept(self, visitor):
        visitor.visitCalldiferenteExpression(self)

class ExpressionIGUALExpression(igualExpression):
    def __init__(self, igualExpression, operation, diferenteExpression):
        self.igualExpression = igualExpression
        self.operation = operation
        self.diferenteExpression = diferenteExpression
    def accept(self, visitor):
        visitor.visitExpressionIGUALExpression(self)


''' diferenteExpression e classes concretas '''
class diferenteExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallRelacionalExpression(diferenteExpression):
    def __init__(self, relacionalExpression):
        self.relacionalExpression = relacionalExpression
    def accept(self, visitor):
        visitor.visitCallRelacionalExpression(self)
         
class CallRelacionalExpressionDif(diferenteExpression):
    def __init__(self, diferenteExpression, operation, relacionalExpression):
        self.diferenteExpression = diferenteExpression
        self.operation = operation
        self.relacionalExpression = relacionalExpression
    def accept(self, visitor):
        visitor.visitCallRelacionalExpressionDif(self)


''' relacionalExpression e classes concretas '''
class relacionalExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallUnary(relacionalExpression):
    def __init__(self, unaryExpression):
        self.unaryExpression = unaryExpression
    def accept(self, visitor):
        visitor.visitCallUnary(self)
    
class CallConcretExpression(relacionalExpression):
    def __init__(self, relacionalExpression, operation, unaryExpression):
        self.relacionalExpression = relacionalExpression
        self.operation = operation
        self.unaryExpression = unaryExpression
    def accept(self, visitor):
        visitor.visitCallConcretExpression(self)


''' unaryExpression e classes concretas '''
class unaryExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CalladdExpression(unaryExpression):
    def __init__(self, addExpression):
        self.addExpression = addExpression
    def accept(self, visitor):
        visitor.visitCalladdExpression(self)

class ConcreteunaryExpression(unaryExpression):
    def __init__(self, unaryExpression, operation):
        self.unaryExpression = unaryExpression
        self.operation = operation
    def accept(self, visitor):
        visitor.visitConcreteunaryExpression(self)


''' addExpression e classes concretas '''
class addExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallMultExpression(addExpression):
    def __init__(self, addExpression):
        self.addExpression = addExpression
    def accept(self, visitor):
        visitor.visitCallMultExpression(self)

class CallAddExpressionMult(addExpression):
    def __init__(self, addExpression, operation, multExpression):
        self.addExpression = addExpression
        self.operation = operation
        self.multExpression = multExpression
    def accept(self, visitor):
        visitor.visitCallAddExpressionMult(self)

''' multExpression e classes concretas '''
class multExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class Callprimary(multExpression):
    def __init__(self, primary):
        self.primary = primary
    def accept(self, visitor):
        visitor.visitCallprimary(self)

class CallprimaryMultExpression(multExpression):
    def __init__(self, multExpression, operation, primary):
        self.multExpression = multExpression
        self.operation = operation
        self.primary = primary
    def accept(self, visitor):
        visitor.visitCallprimaryMultExpression(self)

class CallfunctionCall(multExpression):
    def __init__(self, functionCall):
        self.functionCall = functionCall
    def accept(self, visitor):
        visitor.visitCallfunctionCall(self)

class CallprimaryFunctionCall(multExpression):
    def __init__(self, multExpression, operation,functionCall):
        self.multExpression = multExpression
        self.operation = operation
        self.functionCall = functionCall
    def accept(self, visitor):
        visitor.visitCallprimaryFunctionCall(self)

''' functionCall e classes concretas '''
class functionCall(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcretFunctionCall(functionCall):
    def __init__(self, functionSignature):
        self.functionSignature = functionSignature
    def accept(self, visitor):
        visitor.visitConcretFunctionCall(self)

''' primary e classes concretas '''
class primary(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
        
class CallPrimaryLiteral(primary):
    def __init__(self, literal):
        self.literal = literal
    def accept(self, visitor):
        visitor.visitCallPrimaryLiteral(self)

class CallPrimaryExpression(primary):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        visitor.visitCallPrimaryExpression(self)

''' literal e classes concretas '''
class literal(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallLiteralListLiteral(literal):
    def __init__(self, listLiteral):
        self.listLiteral = listLiteral
    def accept(self, visitor):
        visitor.visitCallLiteralListLiteral(self)

# class CallLiteralBooleanLiteral(literal):
#     def __init__(self, booleanLiteral):
#         self.booleanLiteral = booleanLiteral
#     def accept(self, visitor):
#         visitor.visitCallLiteralBooleanLiteral(self)

class CallLiteralId(literal):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, visitor):
        visitor.visitCallLiteralId(self)


''' listLiteral e classes concretas '''
class listLiteral(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressionListlistLiteral(listLiteral):
    def __init__(self, expressionList):
        self.expressionList = expressionList
    def accept(self, visitor):
        visitor.visitExpressionListlistLiteral(self)


''' expressionList e classes concretas '''
class expressionList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteExpression(expressionList):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        visitor.visitConcreteExpression(self)

class CallExpressionList(expressionList):
    def __init__(self, expression, expressionList):
        self.expression = expression
        self.expressionList = expressionList
    def accept(self, visitor):
        visitor.visitCallExpressionList(self)


''' returnStatement e classes concretas '''            
class returnStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ReturnStatementExpression(returnStatement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        visitor.visitReturnStatementExpression(self)


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
        visitor.visitIfexpressionStatement(self)
    
class IfElseExpressionStatement(ifStatement):
    def __init__(self, IF, expression, statement, ELSE, statement01):
        self.IF = IF
        self.expression = expression
        self.statement = statement
        self.ELSE = ELSE
        self.statement01 = statement01
    def accept(self, visitor):
        visitor.visitIfElseExpressionStatement(self)


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
        visitor.visitConcreteForLoopParts(self)


''' forLoopParts e classes concretas '''
class forLoopParts(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcreteForInitializerStatement(forLoopParts):
    def __init__(self, forInitializerStatement):
        self.forInitializerStatement = forInitializerStatement
    def accept(self, visitor):
        visitor.visitConcreteForInitializerStatement(self)
    
class ForInitializerStatementExpressionList(forLoopParts):
    def __init__(self, forInitializerStatement, expressionList):
        self.forInitializerStatement = forInitializerStatement
        self.expressionList = expressionList
    def accept(self, visitor):
        visitor.visitForInitializerStatementExpressionList(self)
    
class ForInitializerStatementExpression(forLoopParts):
    def __init__(self, forInitializerStatement, expression):
        self.forInitializerStatement = forInitializerStatement
        self.expression = expression
    def accept(self, visitor):
        visitor.visitForInitializerStatementExpression(self)
    
class ExpressionForInitializerStatementExpressionList(forLoopParts):
    def __init__(self, forInitializerStatement, expression, expressionList):
        self.forInitializerStatement = forInitializerStatement
        self.expression = expression
        self.expressionList = expressionList
    def accept(self, visitor):
        visitor.visitExpressionForInitializerStatementExpressionList(self)


''' forInitializerStatement e classes concretas '''
class forInitializerStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ConcreteLocalVariableDeclaration(forInitializerStatement):
    def __init__(self, localVariableDeclaration):
        self.localVariableDeclaration = localVariableDeclaration
    def accept(self, visitor):
        visitor.visitConcreteLocalVariableDeclaration(self)

class CallConcreteExpression(forInitializerStatement):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        visitor.visitCallConcreteExpression(self)


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
        visitor.visitWhileStatementExpressionStatement(self)
        
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
        visitor.visitDOStatementWhileExpression(self)


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
        visitor.visitConcreteSwitch(self)

class ConcreteDefaultCase(switchStatement):
    def __init__(self, switch, expression, switchCaseRepetition, defaultCase):
        self.switch = switch
        self.expression = expression
        self.switchCaseRepetition = switchCaseRepetition
        self.defaultCase = defaultCase
    def accept(self, visitor):
        visitor.visitConcreteDefaultCase(self)


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
        visitor.visitRepetitionSwitchCase(self)

class RepetitionSwitchCase2(switchCaseRepetition):
    def __init__(self, switchCase):
        self.switchCase = switchCase
    def accept(self, visitor):
        visitor.visitRepetitionSwitchCase2(self)


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
        visitor.visitExpressionSwitchCase(self)
        
class LabelSwitchCase(switchCase):
    def __init__(self, label, switchCase):
        self.label = label
        self.switchCase = switchCase
    def accept(self, visitor):
        visitor.visitLabelSwitchCase(self)
   
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
        visitor.visitDefaultStatements(self)

class LabelDefaultCase(defaultCase):
    def __init__(self, label, defaultCase):
        self.label = label
        self.defaultCase = defaultCase
    def accept(self, visitor):
        visitor.visitLabelDefaultCase(self)
        
        
''' label e classes concretas '''            
class label(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class IdPontos(label):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        visitor.visitIdPontos(self)

''' break e classes concretas '''
class BreakStatement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CallBreak(switchCase):
    def __init__(self, BREAK):
        self.BREAK = BREAK
    def accept(self, visitor):
        visitor.visitCallBreak(self)

class BreakID(switchCase):
    def __init__(self, BREAK, id):
        self.BREAK = BREAK
        self.id = id
    def accept(self, visitor):
        visitor.visitBreakID(self)
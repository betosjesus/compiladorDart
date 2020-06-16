from DartAbstractVisitor import AbstractVisitor
import DartSymbolTable as st
from DartVisitor import Visitor

import DartSintaxeAbstrata as sa


def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None


class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')


    ''' topLevelDefinition'''
    def visitTopLevelDefinitionVariable(self, topLevelDefinitionVariable):
        topLevelDefinitionVariable.variableDeclaration.accept(self)

    def visitTopLevelDefinitionVariableRepetition(self, topLevelDefinitionVariableRepetition):
        topLevelDefinitionVariableRepetition.variableDeclaration.accept(self)
        topLevelDefinitionVariableRepetition.topLevel.accept(self)

    def visitTopLevelDefinitionFunction(self, topLevelDefinitionFunction):
        topLevelDefinitionFunction.functionSignature.accept(self)
        topLevelDefinitionFunction.functionBody.accept(self)

    def visitTopLevelDefinitionFunctionRepetition(self, topLevelDefinitionFunctionRepetition):
        topLevelDefinitionFunctionRepetition.functionSignature.accept(self)
        topLevelDefinitionFunctionRepetition.functionBody.accept(self)
        topLevelDefinitionFunctionRepetition.topLevel.accept(self)


    ''' variableDeclaration '''
    def visitVariableDeclarationID(self, variableDeclarationID):
        variableDeclarationID.declaredIdentifier.accept(self)

    def visitConcretevariableDeclaration(self, concretevariableDeclaration):
        return concretevariableDeclaration.id, concretevariableDeclaration.variableDeclaration.accept(self)


    ''' decIdentifier '''
    def visitDeclaredIdentifierType(self, declaredIdentifierType):
        st.addVar(declaredIdentifierType.id, declaredIdentifierType.type)
        return declaredIdentifierType.type


    ''' functionSignature '''
    def visitCallFormalParameterListId(self, callFormalParameterListId):
        bindable = st.getBindable(callFormalParameterListId.id)
        if (callFormalParameterListId.formalParameterList != None):
            if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
                typeParams = callFormalParameterListId.formalParameterList.accept(self)
                if (list(bindable[st.PARAMS][1::2]) == typeParams):
                    return bindable[st.TYPE]
                callFormalParameterListId.accept(self.printer)
                print("\n\t[Erro] Chamada de funcao invalida. Tipos passados na chamada sao:", typeParams)
                print('\tenquanto que os tipos definidos no metodo sao:', bindable[st.PARAMS][1::2], '\n')
            else:
                callFormalParameterListId.accept(self.printer)
                print("\n\t[Erro] Chamada de funcao invalida. O id", callFormalParameterListId.id,
                      "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
            return None
        elif (callFormalParameterListId.formalParameterList == None):
            if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
                return bindable[st.TYPE]
            callFormalParameterListId.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao invalida. O id", callFormalParameterListId.id,
                  "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
            return None

    def visitCallFormalParameterListvoidOrType(self, callFormalParameterListvoidOrType):
        params = {}
        if (not isinstance(callFormalParameterListvoidOrType.formalParameterList, sa.expression)):
            if (callFormalParameterListvoidOrType.formalParameterList != None):
                params = callFormalParameterListvoidOrType.formalParameterList.accept(self)
                st.addFunction(callFormalParameterListvoidOrType.id, params,
                               callFormalParameterListvoidOrType.type)
            elif (callFormalParameterListvoidOrType.formalParameterList == None):
                st.addFunction(callFormalParameterListvoidOrType.id, params,
                               callFormalParameterListvoidOrType.type)
        #print (st.symbolTable)
        st.beginScope(callFormalParameterListvoidOrType.id)
        for k in range(0, len(params), 2):
            st.addVar(params[k], params[k + 1])


    ''' formalParameterList'''
    def visitCallNormalFormalParameters(self, callNormalFormalParameters):
        if (callNormalFormalParameters.normalFormalParameters != None):
            return callNormalFormalParameters.normalFormalParameters.accept(self)
        else:
            return None


    ''' normalFormalParameters '''
    def visitCallNormalFormalParameter(self, normalFormalParameter):
        return normalFormalParameter.simpleFormalParameter.accept(self)

    def visitNormalFormalParametersRepetition(self, normalFormalParametersRepetition):
        if (normalFormalParametersRepetition.normalFormalParameters.accept(self) != None):
            return normalFormalParametersRepetition.simpleFormalParameter.accept(
                self) + normalFormalParametersRepetition.normalFormalParameters.accept(self)
        else:
            return normalFormalParametersRepetition.simpleFormalParameter.accept(self)


    ''' simlpleFormalParameter'''
    def visitCallVoidOrType(self, callVoidOrType):
        return [callVoidOrType.id, callVoidOrType.type]

    def visitCallParameterExpression(self, callParameterExpression):
        return [callParameterExpression.expression.accept(self)]


    ''' functionBody '''
    def visitCallFunctionBody(self, callFunctionBody):
        return callFunctionBody.block.accept(self)


    ''' block '''
    def visitCallBlockStatements(self, callBlockStatements):
        if callBlockStatements.statements != None:
            callBlockStatements.statements.accept(self)


    ''' statements '''
    def visitConcretStatements(self, concretStatements):
        concretStatements.statement.accept(self)
        concretStatements.statements.accept(self)

    def visitConcretStatement(self, concretStatements):
        concretStatements.statement.accept(self)


    ''' statement'''
    def visitStatementNonLabelledStatement(self, statementNonLabelledStatement):
        statementNonLabelledStatement.nonLabelledStatement.accept(self)


    ''' nonLabelledStatement '''
    def visitConcreteExpressionStatement(self, concreteExpressionStatement):
        concreteExpressionStatement.expressionStatement.accept(self)

    def visitNonLabelledStatementblock(self, nonLabelledStatementblock):
        nonLabelledStatementblock.block.accept(self)

    def visitLocalVariableDeclaration(self, localVariableDeclaration):
        localVariableDeclaration.localVariableDeclaration.accept(self)

    def visitConcreteReturnStatement(self, concreteReturnStatement):
        concreteReturnStatement.returnStatement.accept(self)

    def visitConcreteIfStatement(self, concreteIfStatement):
         concreteIfStatement.ifStatement.accept(self)

    def visitConcreteForStatement(self, concreteForStatement):
        concreteForStatement.forStatement.accept(self)

    def visitConcreteWhileStatement(self, concreteWhileStatement):
        concreteWhileStatement.whileStatement.accept(self)

    def visitConcreteDoStatement(self, concreteDoStatement):
         concreteDoStatement.doStatement.accept(self)

    def visitConcreteSwitchStatement(self, concreteSwitchStatement):
         concreteSwitchStatement.switchStatement.accept(self)

    def visitConcreteBreakStatement(self, concreteBreakStatement):
         concreteBreakStatement.breakStatement.accept(self)


    ''' localVariableDeclaration '''
    def visitCallLocalInitializedVariableDeclaration(self, localVariableDeclaration):
        return localVariableDeclaration.initializedVariableDeclaration.accept(self)


    ''' initializedVariableDeclaration '''
    def visitCallDeclaredIdentifier(self, callDeclaredIdentifier):
        return callDeclaredIdentifier.declaredIdentifier.accept(self)


    def visitCallDeclaredInitializedIdentifier(self, callDeclaredInitializedIdentifier):
        typeId = callDeclaredInitializedIdentifier.declaredIdentifier.accept(self)
        typeExp = callDeclaredInitializedIdentifier.expression.accept(self)
        if (typeId == None):
            print (" O identificador ", end='')
            callDeclaredInitializedIdentifier.declaredIdentifier.accept(self.printer)
            print (" não foi declarado")
        elif (typeId == st.FLOAT and (not typeExp in st.Number)):
            callDeclaredInitializedIdentifier.accept(self.printer)
            print (" tipos incompativeis. A expressao da esquerda eh", typeId, end='')
            print("e a expressao da direita eh", typeExp)
        elif (typeId != typeExp):
            callDeclaredInitializedIdentifier.accept(self.printer)
            print (" tipos incompativeis. A expressao da esquerda eh", typeId, end='')
            print(" e a expressao da direita eh", typeExp)


    def visitCalliniRepeticion(self, callIRepeticion):
        callIRepeticion.initializedVariableDeclaration.accept(self)
        return callIRepeticion.id 

    def visitCallLiteralAtribuirExp(self, callLiteralAtribuirExp):
        callLiteralAtribuirExp.literal.accept(self)
        callLiteralAtribuirExp.expression.accept(self)


    ''' returnStatement'''
    def visitReturnStatementExpression(self, returnStatementExpression):
        typeExp = returnStatementExpression.expression.accept(self)
        scope = st.symbolTable[-1][st.SCOPE]
        bindable = st.getBindable(scope)
        if (typeExp != bindable[st.TYPE]):
            returnStatementExpression.accept(self.printer)
            print('\t[Erro] O retorno da funcao', scope, 'eh do tipo', bindable[st.TYPE], end='')
            print(' no entanto, o retorno passado foi do tipo', typeExp, '\n')
        st.endScope()


    ''' expressionStatement '''
    def visitConcretexpression(self, concretexpression):
        return concretexpression.expression.accept(self)


    '''expression '''
    def visitCallExpression(self, callExpression):
        return callExpression.orExpression.accept(self)
        

    ''' orExpression '''
    def visitCallandExpression(self, callandExpression):
        return callandExpression.andExpression.accept(self)

    def visitExpressionORexpression(self, expressionORexpression):
        type1 = expressionORexpression.orExpression.accept(self)
        type2 = expressionORexpression.andExpression.accept(self)
        if (type1 != st.BOOL or type2 != st.BOOL):
            print("\n\t[Erro] A expressao ", end='')
            expressionORexpression.orExpression.accept(self.printer)
            print("\n\t OU ", end='')
            expressionORexpression.andExpression.accept(self.printer)
            print(" eh", type1, end='')
            print(". Deveria ser boolean\n")
        return st.BOOL


    ''' andExpression '''
    def visitCalligualExpression(self, calligualExpression):
        return calligualExpression.equalityExpression.accept(self)

    def visitCallAndExpressionIgual(self, callAndExpressionIgual):
        type1 = callAndExpressionIgual.andExpression.accept(self)
        type2 = callAndExpressionIgual.equalityExpression.accept(self)
        if (type1 != st.BOOL or type2 != st.BOOL):
            print("\n\t[Erro] A expressao ", end='')
            callAndExpressionIgual.equalityExpression.accept(self.printer)
            print("\n\t OU ", end='')
            callAndExpressionIgual.andExpression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser boolean\n")
        return st.BOOL


    ''' equalityExpression '''
    def visitCallRelacionalExpression(self, callRelacionalExpression):
        return callRelacionalExpression.relacionalExpression.accept(self)

    def visitCallEqualityExpression(self, callEqualityExpression):
        return st.BOOL if coercion(callEqualityExpression.equalityExpression.accept(self), 
                        callEqualityExpression.relacionalExpression.accept(self)) != None else None


    ''' relacionalExpression '''
    def visitCallUnary(self, callUnary):
        return callUnary.addExpression.accept(self)

    def visitCallConcretExpression(self, callConcretExpression):
        return st.BOOL if coercion(callConcretExpression.relacionalExpression.accept(self),
                        callConcretExpression.addExpression.accept(self)) != None else None


    ''' addExpression '''
    def visitCallMultExpression(self, callMultExpression):
        return callMultExpression.multExpression.accept(self)

    def visitCallAddExpressionMult(self, callAddExpressionMult):
        type1 = callAddExpressionMult.addExpression.accept(self)
        type2 = callAddExpressionMult.multExpression.accept(self)
        c = coercion(type1, type2)
        if (c == None):
            callAddExpressionMult.accept(self.printer)
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            callAddExpressionMult.addExpression.accept(self.printer)
            print(' eh do tipo', type1, 'enquanto a expressao ', end='')
            callAddExpressionMult.multExpression.accept(self.printer)
            print(' eh do tipo', type2, '\n')
        return c


    ''' multExpression '''
    def visitCallUnaryExp(self, callUnaryExp):
        return callUnaryExp.unaryExpression.accept(self)

    def visitCallUnaryExpMultExpression(self, callUnaryExpMultExpression):
        type1 = callUnaryExpMultExpression.multExpression.accept(self)
        type2 = callUnaryExpMultExpression.unaryExpression.accept(self)
        c = coercion(type1, type2)
        if (c == None):
            callUnaryExpMultExpression.accept(self.printer)
            print('\n\t[Erro] Multiplicação invalida. A expressao ', end='')
            callUnaryExpMultExpression.multExpression.accept(self.printer)
            print(' eh do tipo', type1, 'enquanto a expressao ', end='')
            callUnaryExpMultExpression.unaryExpression.accept(self.printer)
            print(' eh do tipo', type2, '\n')
        return c


    ''' unaryExpression '''
    def visitConcreteprimaryExpression(self, concreteprimaryExpression):
        # print("[visitConcreteprimaryExpression]")
        return concreteprimaryExpression.primary.accept(self)

    def visitCallfunctioncall(self, callfunctioncall):
        return callfunctioncall.functionCall.accept(self)

    def visitConcreteunaryExpression(self, concreteunaryExpression):
        typeVar = concreteunaryExpression.unaryExpression.accept(self)
        if (typeVar != st.INT):
            print('\n\t[Erro] Tipo invalido. ', end='')
        else: 
            return typeVar


    ''' primary '''
    def visitCallPrimaryLiteral(self, callPrimaryLiteral):
        if isinstance(callPrimaryLiteral.literal, sa.literal):
            return callPrimaryLiteral.literal.accept(self)


    def visitCallPrimaryExpression(self, callPrimaryExpression):
        return callPrimaryExpression.expression.accept(self)        


    ''' literal '''
    def visitCallLiteralListLiteralID(self, callLiteralListLiteralID):
        return callLiteralListLiteralID.listLiteralID.accept(self)

    def visitCallLiteralListLiteral(self, callLiteralListLiteral):
        return callLiteralListLiteral.listLiteral.accept(self)

    def visitCallLiteralBooleanLiteral(self, callLiteralBooleanLiteral):
        callLiteralBooleanLiteral.booleanLiteral.accept(self)
        return st.BOOL

    def visitCallLiteralId(self, callLiteralId):
        idName = st.getBindable(callLiteralId.id)
        #print ("[visitCallLiteralId]", st.symbolTable)
        if (idName != None):
            return idName[st.TYPE]
        return None
    
    def visitCallNum(self, callnum):
        # print("[visitCallNum] ", callnum.num)
        if (callnum.num.isdigit()):
            return st.INT
        else:
            return st.FLOAT



    ''' listLiteral'''
    def visitExpressionListlistLiteral(self, expressionListlistLiteral):
        return expressionListlistLiteral.expressionList.accept(self)


    '''listLiteralID '''
    def visitCallListlistLiteralID(self, callListlistLiteralID):
        return callListlistLiteralID.id, callListlistLiteralID.listLiteral.accept(self)


    ''' booleanLiteral'''
    def visitbooleanLiteralTrue(self, booleanLiteralTrue):
        return st.BOOL

    def visitbooleanLiteralFalse(self, booleanLiteralFalse):
        return st.BOOL


    ''' expressionList'''
    def visitConcreteExpression(self, concreteExpression):
        return concreteExpression.expression.accept(self)

    def visitCallExpressionList(self, callExpressionList):
        callExpressionList.expression.accept(self)
        callExpressionList.expressionList.accept(self)


    ''' functionCall '''
    def visitConcretFunctionCall(self, concretFunctionCall):
        return concretFunctionCall.functionSignature.accept(self)


    ''' whileStatement '''
    def visitWhileStatementExpressionStatement(self, whileStatementExpressionStatement):
        type = whileStatementExpressionStatement.expression.accept(self)
        if (type != st.BOOL):
            whileStatementExpressionStatement.expression.accept(self.printer)
            print("\n\t[Erro] A expressao ", end='')
            whileStatementExpressionStatement.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser boolean\n")
        whileStatementExpressionStatement.statement.accept(self)
    

    ''' ifStatement '''
    def visitIfexpressionStatement(self, ifexpressionStatement):
        type = ifexpressionStatement.expression.accept(self)
        if (type != st.BOOL):
            ifexpressionStatement.expression.accept(self.printer)
            print("\n\t[Erro] A expressao ", end='')
            ifexpressionStatement.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser boolean\n")
        ifexpressionStatement.statement.accept(self)   
    
    def visitIfElseExpressionStatement(self, ifElseExpressionStatement):
        type = ifElseExpressionStatement.expression.accept(self)
        if (type != st.BOOL):
            ifElseExpressionStatement.expression.accept(self.printer)
            print("\n\t[Erro] A expressao ", end='')
            ifElseExpressionStatement.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser boolean\n")
        ifElseExpressionStatement.statement.accept(self)
        ifElseExpressionStatement.statement01.accept(self)   


    ''' doStatement '''
    def visitDOStatementWhileExpression(self, DOStatementWhileExpression):      
        type = DOStatementWhileExpression.expression.accept(self)
        DOStatementWhileExpression.statement.accept(self)
        if (type != st.BOOL):
            DOStatementWhileExpression.expression.accept(self.printer)
            print("\n\t[Erro] A expressao ", end='')
            DOStatementWhileExpression.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser boolean\n")     
    

    ''' switchStatement '''
    def visitConcreteSwitch(self, concreteSwitch):
        type = concreteSwitch.expression.accept(self)
        if (type != st.INT):
            concreteSwitch.expression.accept(self.printer)  
            print("\n\t[Erro] A expressao ", end='')
            concreteSwitch.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser INTEIRO\n")    
        concreteSwitch.switchCaseRepetition.accept(self)    
      
    def visitConcreteDefaultCase(self, concreteDefaultCase):
        type = concreteDefaultCase.expression.accept(self)
        if (type != st.INT):
            concreteDefaultCase.expression.accept(self.printer)
            print("\n\t[Erro] A expressao ", end='')
            concreteDefaultCase.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser INTEIRO\n")   
        concreteDefaultCase.switchCaseRepetition.accept(self)
        concreteDefaultCase.defaultCase.accept(self)        


    ''' switchCaseRepetition '''
    def visitRepetitionSwitchCase(self, repetitionSwitchCase):
        repetitionSwitchCase.switchCase.accept(self)
        repetitionSwitchCase.switchCaseRepetition.accept(self)
        
    def visitRepetitionSwitchCase2(self, repetitionSwitchCase2):
        repetitionSwitchCase2.switchCase.accept(self)


    ''' switchCase'''
    def visitExpressionSwitchCase(self, expressionSwitchCase):
        type = expressionSwitchCase.expression.accept(self)
        if (type != st.INT):
            expressionSwitchCase.expression.accept(self.printer)
            print("\n\t[Erro] A expressao ", end='')
            expressionSwitchCase.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser INTEIRO\n")   
        expressionSwitchCase.statements.accept(self)


    ''' defaultCase'''
    def visitDefaultStatements(self, defaultStatements):
        defaultStatements.statements.accept(self)
    
    def visitLabelDefaultCase(self, labelDefaultCase):
        labelDefaultCase.label.accept(self)
        labelDefaultCase.defaultCase.accept(self)
    

    ''' break '''
    def visitCallBreak(self, callBreak):
        return callBreak.BREAK
    
    def visitBreakID(self, breakID):
        return breakID.id


    ''' forStatement '''
    def visitConcreteForLoopParts(self, concreteForLoopParts):
        concreteForLoopParts.forLoopParts.accept(self)
        concreteForLoopParts.statement.accept(self)    

    ''' forLoopParts '''
    def visitConcreteForInitializerStatement(self, concreteForInitializerStatement):
        return concreteForInitializerStatement.forInitializerStatement.accept(self)
        
    def visitForInitializerStatementExpressionList(self, forInitializerStatementExpressionList):
        forInitializerStatementExpressionList.forInitializerStatement.accept(self)
        forInitializerStatementExpressionList.expressionList.accept(self)     

    def visitForInitializerStatementExpression(self, forInitializerStatementExpression):
        forInitializerStatementExpression.forInitializerStatement.accept(self)
        type = forInitializerStatementExpression.expression.accept(self)
        if (type != st.BOOL):
            forInitializerStatementExpression.expression.accept(self.printer)
            print("\n\t[Erro] A expressao ", end='')
            forInitializerStatementExpression.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser boolean\n")


    def visitExpressionForInitializerStatementExpressionList(self, expressionForInitializerStatementExpressionList):
        expressionForInitializerStatementExpressionList.forInitializerStatement.accept(self)
        type = expressionForInitializerStatementExpressionList.expression.accept(self)
        if (type != st.BOOL):
            expressionForInitializerStatementExpressionList.expression.accept(self.printer)
            print("\n\t[Erro] A expressao ", end='')
            expressionForInitializerStatementExpressionList.expression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser boolean\n")       
        expressionForInitializerStatementExpressionList.expressionList.accept(self)         


    ''' forInitializerStatement '''
    def visitConcreteLocalVariableDeclaration(self, concreteLocalVariableDeclaration):
        return concreteLocalVariableDeclaration.localVariableDeclaration.accept(self)     

    def visitCallConcreteExpression(self, callConcreteExpression):
        if (callConcreteExpression.expression != None):
            return callConcreteExpression.expression.accept(self)
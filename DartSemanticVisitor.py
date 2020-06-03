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
        st.addVar(declaredIdentifierType.id, declaredIdentifierType.voidOrType.type)

    def visitDeclaredIdentifierId(self, declaredIdentifierId):
        return declaredIdentifierId.expression.accept(self)

    ''' voidOrType '''

    def visitConcreteVoidOrType(self, concretevoidOrType):
        return concretevoidOrType.type(self)

    def visitVoidOrTypeV(self, voidOrTypeV):
        return [voidOrTypeV.void]

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
            #print("[visitCallFormalParameterListId]", typeParams)
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
        if (callFormalParameterListvoidOrType.formalParameterList != None):
            params = callFormalParameterListvoidOrType.formalParameterList.accept(self)
            st.addFunction(callFormalParameterListvoidOrType.id, params,
                           callFormalParameterListvoidOrType.voidOrType.type)
        elif (callFormalParameterListvoidOrType.formalParameterList == None):
            st.addFunction(callFormalParameterListvoidOrType.id, params,
                           callFormalParameterListvoidOrType.voidOrType.type)
        st.beginScope(callFormalParameterListvoidOrType.id)
        #print("[visitCallFormalParameterListvoidOrType]", params)
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
        return [callVoidOrType.id, callVoidOrType.voidOrType.type]

    def visitCallParameterExpression(self, callParameterExpression):
        return callParameterExpression.expression.accept(self)

    ''' functionBody '''

    def visitCallFunctionBody(self, callFunctionBody):
        callFunctionBody.block.accept(self)

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

    # def visitConcreteIfStatement(self, concreteIfStatement):
    #      nonLabelledStatementblock.ifStatement.accept(self)

    # def visitConcreteForStatement(self, concreteForStatement):
    #     nonLabelledStatementblock.forStatement.accept(self)

    def visitConcreteWhileStatement(self, concreteWhileStatement):
        concreteWhileStatement.whileStatement.accept(self)

    # def visitConcreteDoStatement(self, concreteDoStatement):
    #      nonLabelledStatementblock.doStatement.accept(self)

    # def visitConcreteSwitchStatement(self, concreteSwitchStatement):
    #      nonLabelledStatementblock.switchStatement.accept(self)

    # def visitConcreteBreakStatement(self, concreteBreakStatement):
    #      nonLabelledStatementblock.breakStatement.accept(self)

    ''' localVariableDeclaration '''

    def visitCallLocalInitializedVariableDeclaration(self, localVariableDeclaration):
        localVariableDeclaration.initializedVariableDeclaration.accept(self)

    ''' initializedVariableDeclaration '''

    def visitCallDeclaredIdentifier(self, callDeclaredIdentifier):
        callDeclaredIdentifier.declaredIdentifier.accept(self)

    def visitCallDeclaredInitializedIdentifier(self, callDeclaredInitializedIdentifier):
        # callDeclaredInitializedIdentifier.declaredIdentifier.accept(self)
        typeVar = callDeclaredInitializedIdentifier.expression.accept(self)
        if (isinstance(callDeclaredInitializedIdentifier.declaredIdentifier, sa.literal)):
            st.addVar(callDeclaredInitializedIdentifier.declaredIdentifier.id, typeVar)
            return typeVar
        return None

    def visitCallDeclaredInitializedIdentifierListLiteral(self, callDeclaredInitializedIdentifierListLiteral):
        callDeclaredInitializedIdentifierListLiteral.declaredIdentifier.accept(self)
        callDeclaredInitializedIdentifierListLiteral.listLiteral.accept(self)

    def visitCallIdListAtribuirIdList(self, callIdListIdAtribuirExpression):
        callIdListIdAtribuirExpression.listLiteralID.accept(self)
        callIdListIdAtribuirExpression.expression.accept(self)

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
        concretexpression.expression.accept(self)

    '''expression '''

    def visitCallExpression(self, callExpression):
        callExpression.orExpression.accept(self)

    ''' orExpression '''

    def visitCallandExpression(self, callandExpression):
        callandExpression.andExpression.accept(self)

    def visitExpressionORexpression(self, expressionORexpression):
        type1 = expressionORexpression.orExpression.accept(self)
        type2 = expressionORexpression.andExpression.accept(self)
        if (type1 != st.BOOL or type2 != st.BOOL):
            print("\n\t[Erro] A expressao ", end='')
            expressionORexpression.orExpression.accept(self.printer)
            print("\n\t OU ", end='')
            expressionORexpression.andExpression.accept(self.printer)
            print(" eh", type, end='')
            print(". Deveria ser boolean\n")

    ''' andExpression '''

    def visitCalligualExpression(self, calligualExpression):
        calligualExpression.equalityExpression.accept(self)

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

    ''' equalityExpression '''

    def visitCallRelacionalExpression(self, callRelacionalExpression):
        callRelacionalExpression.relacionalExpression.accept(self)

    def visitCallEqualityExpression(self, callEqualityExpression):
        callEqualityExpression.equalityExpression.accept(self)
        callEqualityExpression.relacionalExpression.accept(self)

    ''' relacionalExpression '''

    def visitCallUnary(self, callUnary):
        return callUnary.addExpression.accept(self)

    def visitCallConcretExpression(self, callConcretExpression):
        callConcretExpression.relacionalExpression.accept(self)
        callConcretExpression.addExpression.accept(self)

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
        #print('[visitCallAddExpressionMult]', type1)
        #print('[visitCallAddExpressionMult]', type2)
        return c

    ''' multExpression '''

    def visitCallUnaryExp(self, callUnaryExp):
        callUnaryExp.unaryExpression.accept(self)

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
        concreteprimaryExpression.primary.accept(self)

    def visitCallfunctioncall(self, callfunctioncall):
        callfunctioncall.functionCall.accept(self)

    def visitConcreteunaryExpression(self, concreteunaryExpression):
        type = concreteunaryExpression.unaryExpression.accept(self)
        if (type != st.INT):
            print('\n\t[Erro] Tipo invalido. ', end='')
            concreteunaryExpression.unaryExpression.accept(self.printer)

    ''' primary '''

    def visitCallPrimaryLiteral(self, callPrimaryLiteral):
        if isinstance(callPrimaryLiteral.literal, sa.literal):
            callPrimaryLiteral.literal.accept(self)

    ''' literal '''

    def visitCallLiteralListLiteral(self, callLiteralListLiteral):
        callLiteralListLiteral.listLiteral.accept(self)

    def visitCallLiteralBooleanLiteral(self, callLiteralBooleanLiteral):
        callLiteralBooleanLiteral.booleanLiteral.accept(self)
        return st.BOOL

    def visitCallLiteralId(self, callLiteralId):
        idName = st.getBindable(callLiteralId.id)
        if (idName != None):
            return idName[st.TYPE]
        return None

    ''' listLiteral'''

    def visitExpressionListlistLiteral(self, expressionListlistLiteral):
        expressionListlistLiteral.expressionList.accept(self)

    '''listLiteralID '''

    def visitCallListlistLiteralID(self, callListlistLiteralID):
        return [callListlistLiteralID.id] + callListlistLiteralID.listLiteral.accept(self)

    ''' booleanLiteral'''

    def visitbooleanLiteralTrue(self, booleanLiteralTrue):
        return [booleanLiteralTrue.true]

    def visitbooleanLiteralFalse(self, booleanLiteralFalse):
        return [booleanLiteralFalse.false]

    ''' expressionList'''

    def visitConcreteExpression(self, concreteExpression):
        concreteExpression.expression.accept(self)

    def visitCallExpressionList(self, callExpressionList):
        callExpressionList.expression.accept(self)
        callExpressionList.expressionList.accept(self)

    ''' functionCall '''

    def visitConcretFunctionCall(self, concretFunctionCall):
        concretFunctionCall.functionSignature.accept(self)

    def visitCallPrimaryExpression(self, callPrimaryExpression):
        callPrimaryExpression.expression.accept(self)

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
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
        concretevariableDeclaration.declaredIdentifier.accept(self)
        return [concretevariableDeclaration.id]
       

    ''' decIdentifier '''
    def visitDeclaredIdentifierType(self, declaredIdentifierType):
        declaredIdentifierType.voidOrType.accept(self)
        return [declaredIdentifierType.id]
    
    def visitDeclaredIdentifierId(self, declaredIdentifierId):
        return [declaredIdentifierId.id, declaredIdentifierId.type]

    ''' voidOrType '''
    def visitConcreteVoidOrType(self, concretevoidOrType):
        concretevoidOrType.type.accept(self)
        return [concretevoidOrType.type]

    def visitVoidOrTypeV(self, voidOrTypeV):
        voidOrTypeV.void.accept(self)         
        return [voidOrTypeV.type]
    
    ''' functionSignature '''
    def visitCallFormalParameterListId(self, callFormalParameterListId):
        callFormalParameterListId.formalParameterList.accept(self)
        return [callFormalParameterListId.id]
    
    def visitCallFormalParameterListvoidOrType(self, callFormalParameterListvoidOrType):
        callFormalParameterListvoidOrType.voidOrType.accept(self)
        params = {}
        if (callFormalParameterListvoidOrType.formalParameterList != None):
            params = callFormalParameterListvoidOrType.formalParameterList.accept(self)
            st.addFunction(callFormalParameterListvoidOrType.id, params, callFormalParameterListvoidOrType.type)
        else:
            st.addFunction(callFormalParameterListvoidOrType.id, params, callFormalParameterListvoidOrType.type)
        st.beginScope(callFormalParameterListvoidOrType.id)
        for k in range(0, len(params), 2):
            st.addVar(params[k], params[k+1])
    
    ''' formalParameterList'''
    def visitCallNormalFormalParameters(self, callNormalFormalParameters):
        if (callNormalFormalParameters.normalFormalParameters != None):
            callNormalFormalParameters.normalFormalParameters.accept(self)
    
    ''' normalFormalParameters '''
    def visitCallNormalFormalParameter(self, normalFormalParameter):
        normalFormalParameter.simpleFormalParameter.accept(self)
    
    def visitNormalFormalParametersRepetition(self, normalFormalParametersRepetition):
        normalFormalParametersRepetition.simpleFormalParameter.accept(self)
        normalFormalParametersRepetition.normalFormalParameters.accept(self)
    

    ''' simlpleFormalParameter'''
    def visitCallFinalConstVarOrTypeId(self, callFinalConstVarOrTypeId):
        return [callFinalConstVarOrTypeId.id]

    def visitCallVoidOrType(self, callVoidOrType):     
        callVoidOrType.voidOrType.accept(self)
    
    def visitCallParameterExpression(self, callParameterExpression):        
        callParameterExpression.expression.accept(self)
    

    ''' functionBody '''
    def visitCallFunctionBody(self, callFunctionBody):        
        callFunctionBody.block.accept(self)
    

    ''' block '''
    def visitCallBlockStatements(self, callBlockStatements):        
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

    # def visitLocalVariableDeclaration(self, localVariableDeclaration):        
    #     localVariableDeclaration.localVariableDeclaration.accept(self)

    def visitConcreteReturnStatement(self, concreteReturnStatement):        
         concreteReturnStatement.returnStatement.accept(self)

    # def visitConcreteIfStatement(self, concreteIfStatement):        
    #      nonLabelledStatementblock.ifStatement.accept(self)

    # def visitConcreteForStatement(self, concreteForStatement):        
    #     nonLabelledStatementblock.forStatement.accept(self)
 
    # def visitConcreteWhileStatement(self, concreteWhileStatement):        
    #      nonLabelledStatementblock.whileStatement.accept(self)

    # def visitConcreteDoStatement(self, concreteDoStatement):        
    #      nonLabelledStatementblock.doStatement.accept(self)

    # def visitConcreteSwitchStatement(self, concreteSwitchStatement):        
    #      nonLabelledStatementblock.switchStatement.accept(self)

    # def visitConcreteBreakStatement(self, concreteBreakStatement):        
    #      nonLabelledStatementblock.breakStatement.accept(self)
        
        
    # ''' localVariableDeclaration '''
    # def visitCallLocalInitializedVariableDeclaration(self, localVariableDeclaration):        
    #     localVariableDeclaration.initializedVariableDeclaration.accept(self)
    
    
    # ''' initializedVariableDeclaration '''
    # def visitCallDeclaredIdentifier(self, callDeclaredIdentifier):        
    #     callDeclaredIdentifier.declaredIdentifier.accept(self)

    # def visitCallDeclaredInitializedIdentifier(self, callDeclaredInitializedIdentifier):        
    #     callDeclaredIdentifier.declaredIdentifier.accept(self)
    #     callDeclaredIdentifier.expression.accept(self)

    # def visitCallDeclaredInitializedIdentifierList(self, callDeclaredInitializedIdentifierList):
    #     callDeclaredInitializedIdentifierList.declaredIdentifier.accept(self)
    #     callDeclaredInitializedIdentifierList.listLiteral.accept(self)

    # def visitCallDeclaredInitializedIdentifierListLiteral(self, callDeclaredInitializedIdentifierListLiteral):
    #     callDeclaredInitializedIdentifierListLiteral.declaredIdentifier.accept(self)

     # def visitIdInitList(self, idInitList):
    #     idInitList.listLiteral.accept(self)
    #     idInitList.expression.accept(self)


    # def visitCallIdListAtribuirIdList(self, callIdListAtribuirIdList):
    #     callIdListAtribuirIdList.listLiteral.accept(self)
    #     callIdListAtribuirIdList.listLiteral2.accept(self)


    # ''' expressionStatement '''
    # def visitConcretexpression(self, concretexpression):
    #     if concretexpression.expression != ';':
    #         concretexpression.expression.accept(self)
    #         print(' ;', end='\n')
    #     else:
    #         print(' ;', end='\n')


    # ''' returnStatement'''
    # def visitReturnStatementExpression(self, returnStatementExpression):
    #     returnStatementExpression.expression.accept(self)

    ''' expressionStatement '''
    def visitConcretexpression(self, concretexpression):
        concretexpression.expression.accept(self)


    '''expression '''
    def visitCallExpression(self, callExpression):
        callExpression.orExpression.accept(self)


    ''' orExpression '''
    def visitCallandExpression(self, callandExpression):
        callandExpression.andExpression.accept(self)




    # def visitExpressionORexpression(self, expressionORexpression):
    #     # print("visitExpressionORexpression")
    #     expressionORexpression.orExpression.accept(self)
    #     print(' || ', end='')
    #     expressionORexpression.andExpression.accept(self)


    # ''' andExpression '''
    # def visitCalligualExpression(self, calligualExpression):
    #     # print("visitCalligualExpression")
    #     calligualExpression.equalityExpression.accept(self)
    
    # def visitCallAndExpressionIgual(self, callAndExpressionIgual):
    #     # print("visitCallAndExpressionIgual")
    #     callAndExpressionIgual.andExpression.accept(self)
    #     print(' && ', end='')
    #     callAndExpressionIgual.equalityExpression.accept(self)

    
    # ''' equalityExpression '''
    # def visitCallRelacionalExpression(self, callRelacionalExpression):
    #     # print("visitCallRelacionalExpression")
    #     callRelacionalExpression.relacionalExpression.accept(self)

    # def visitCallEqualityExpression(self, callEqualityExpression):
    #     # print("visitCallEqualityExpression")
    #     callEqualityExpression.equalityExpression.accept(self)
    #     if callEqualityExpression.operation   ==  '==':
    #         print(' == ', end='')
    #     else:
    #         print(' != ', end='')
    #     callEqualityExpression.relacionalExpression.accept(self)
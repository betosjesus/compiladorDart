import DartSintaxeAbstrata as sa

class Visitor:

    ''' topLevelDefinition'''
    def visitTopLevelDefinitionVariable(self, topLevelDefinitionVariable):
        # print ("visitTopLevelDefinitionVariable")
         topLevelDefinitionVariable.variableDeclaration.accept(self)
         print(';', end='\n')

    def visitTopLevelDefinitionVariableRepetition(self, topLevelDefinitionVariableRepetition):
        # print ("visitTopLevelDefinitionVariableRepetition")
         topLevelDefinitionVariableRepetition.variableDeclaration.accept(self)
         print(';', end='\n')
         topLevelDefinitionVariableRepetition.topLevel.accept(self)

    def visitTopLevelDefinitionFunction(self, topLevelDefinitionFunction):
        # print("visitTopLevelDefinitionFunction")
        topLevelDefinitionFunction.functionSignature.accept(self)
        topLevelDefinitionFunction.functionBody.accept(self)

    def visitTopLevelDefinitionFunctionRepetition(self, topLevelDefinitionFunctionRepetition):
        # print ("visitTopLevelDefinitionFunctionRepetition")
         topLevelDefinitionFunctionRepetition.functionSignature.accept(self)
         topLevelDefinitionFunctionRepetition.functionBody.accept(self)
         topLevelDefinitionFunctionRepetition.topLevel.accept(self)


    ''' variableDeclaration'''
    def visitVariableDeclarationID(self, variableDeclarationID):
        # print ("visitVariableDeclarationID")
         variableDeclarationID.declaredIdentifier.accept(self)


    def visitConcretevariableDeclaration(self, concretevariableDeclaration):
        # print("visitConcretevariableDeclaration")
        concretevariableDeclaration.variableDeclaration.accept(self)
        print(', ', end='')
        print(concretevariableDeclaration.id, end='')

    ''' decIdentifier'''
    def visitDeclaredIdentifierType(self, declaredIdentifierType):
        # print("visitDeclaredIdentifierType")
        declaredIdentifierType.voidOrType.accept(self)
        print(declaredIdentifierType.id, end='')
    
    def visitDeclaredIdentifierId(self, declaredIdentifierId):
        # print("visitDeclaredIdentifierId")
        print(declaredIdentifierId.id, end='')

    ''' VoidOrType'''
    def visitVoidOrType(self, voidOrType):
        # print("visitVoidOrType")
        print(voidOrType.type, end=' ')
        #voidOrType.type.accept(self)

    def visitVoidOrTypeV(self, voidOrTypeV):
        # print("visitVoidOrTypeV")
        print(voidOrTypeV.void, end=' ')
#-----------------------------------------------------------------

    ''' functionSignature '''
    def visitCallFormalParameterListId(self, callFormalParameterListId):
        # print("visitCallFormalParameterListId")
        print(callFormalParameterListId.id, end='')
        callFormalParameterListId.formalParameterList.accept(self)
    
    def visitCallFormalParameterListvoidOrType(self, callFormalParameterListvoidOrType):
        # print("visitCallFormalParameterListvoidOrType")
        callFormalParameterListvoidOrType.voidOrType.accept(self)
        print(callFormalParameterListvoidOrType.id, end='')
        callFormalParameterListvoidOrType.formalParameterList.accept(self)
            

        ''' formalParameterList'''
    def visitCallNormalFormalParameters(self, callNormalFormalParameters):
        # print("visitCallNormalFormalParameters")
        print('(', end='')
        if (callNormalFormalParameters.normalFormalParameters != None):
            callNormalFormalParameters.normalFormalParameters.accept(self)
        print(')', end='')
    

    ''' normalFormalParameters '''
    def visitCallNormalFormalParameter(self, normalFormalParameter):
        #print("visitCallNormalFormalParameter")
        normalFormalParameter.simpleFormalParameter.accept(self)
    
    def visitNormalFormalParametersRepetition(self, normalFormalParametersRepetition):
        # print("visitNormalFormalParametersRepetition")
        normalFormalParametersRepetition.simpleFormalParameter.accept(self)
        print(', ', end='')
        normalFormalParametersRepetition.normalFormalParameters.accept(self)
    

    ''' simlpleFormalParameter '''
    def visitCallFinalConstVarOrTypeId(self, callFinalConstVarOrTypeId):
        # print("visitCallFinalConstVarOrTypeId")
        print(callFinalConstVarOrTypeId.id, end='')

    def visitCallVoidOrType(self, callVoidOrType):
        # print("visitCallVoidOrType")        
        callVoidOrType.voidOrType.accept(self)
        print(callVoidOrType.id, end='')
    
    def visitCallParameterExpression(self, callParameterExpression):
        # print("visitCallParameterExpression")        
        callParameterExpression.expression.accept(self)
        
        
    ''' FunctionBody '''
    def visitCallFunctionBody(self, callFunctionBody):
        # print("visitCallFunctionBody")
        callFunctionBody.block.accept(self)
 

    ''' block '''
    def visitCallBlockStatements(self, callBlockStatements):
        # print("visitCallBlockStatements")
        print('{ ', end='\n')
        callBlockStatements.statements.accept(self)
        print('}', end='\n')


    ''' statements '''
    def visitConcretStatements(self, concretStatement):
        # print("visitConcretStatements")
        concretStatement.statement.accept(self)
        concretStatement.statements.accept(self)

    def visitConcretStatement(self, concretStatement):
        # print("visitConcretStatement")
        concretStatement.statement.accept(self)


    ''' statement'''
    def visitStatementNonLabelledStatement(self, statementNonLabelledStatement):
        #print("visitStatementNonLabelledStatement")
        statementNonLabelledStatement.nonLabelledStatement.accept(self)


    ''' nonLabelledStatement'''
    def visitNonLabelledStatementblock(self, nonLabelledStatementblock):
        # print("visitNonLabelledStatementblock")
        nonLabelledStatementblock.block.accept(self)
        print('')
    
    def visitLocalVariableDeclaration(self, localVariableDeclaration):
        # print("visitLocalVariableDeclaration")
        localVariableDeclaration.localVariableDeclaration.accept(self)
    
    def visitConcreteExpressionStatement(self, concreteExpressionStatement):
        # print("visitConcreteExpressionStatement")
        if concreteExpressionStatement.expressionStatement == ';': 
            print(concreteExpressionStatement.expressionStatement, end='\n')
        else:
            concreteExpressionStatement.expressionStatement.accept(self)

    def visitConcreteReturnStatement(self, concreteReturnStatement):
        #print("visitConcreteReturnStatement"))
        concreteReturnStatement.returnStatement.accept(self)
    
    def visitConcreteIfStatement(self, concreteIfStatement):
        # print("visitConcreteIfStatement")
        concreteIfStatement.ifStatement.accept(self)
    
    def visitConcreteForStatement(self, concreteForStatement):
        # print("visitConcreteForStatement")
        concreteForStatement.forStatement.accept(self)

    def visitConcreteWhileStatement(self, concreteWhileStatement):
        # print("visitConcreteWhileStatement")
        concreteWhileStatement.whileStatement.accept(self)
        print('')

    def visitConcreteDoStatement(self, concreteDoStatement):
        # print("visitConcreteDoStatement")
        concreteDoStatement.doStatement.accept(self)
        print('')

    def visitConcreteSwitchStatement(self, concreteSwitchStatement):
        # print("visitConcreteSwitchStatement")
        concreteSwitchStatement.switchStatement.accept(self)
        print('')

    def visitConcreteBreakStatement(self, concreteBreakStatement):
        # print("visitConcreteBreakStatement")
        concreteBreakStatement.breakStatement.accept(self)
        print('')


    ''' localVariableDeclaration'''
    def visitCallLocalInitializedVariableDeclaration(self, callLocalInitializedVariableDeclaration):
        # print("visitCallLocalInitializedVariableDeclaration")
        callLocalInitializedVariableDeclaration.initializedVariableDeclaration.accept(self)
        print(' ; ', end='\n')
        

    ''' ================ initializedVariableDeclaration ================= '''
    def visitCallDeclaredIdentifier(self, callDeclaredIdentifier):
        # print("visitCallDeclaredIdentifier")
        callDeclaredIdentifier.declaredIdentifier.accept(self)

    def visitCallDeclaredInitializedIdentifierList(self, callDeclaredInitializedIdentifierList):
        # print("visitCallDeclaredInitializedIdentifierList")
        callDeclaredInitializedIdentifierList.declaredIdentifier.accept(self)
        print(' = ', end='')
        callDeclaredInitializedIdentifierList.listLiteral.accept(self)

    def visitCallDeclaredInitializedIdentifierListLiteral(self, callDeclaredInitializedIdentifierListLiteral):
        # print("visitCallDeclaredInitializedIdentifierListLiteral")
        callDeclaredInitializedIdentifierListLiteral.declaredIdentifier.accept(self)
        print(' = ', end='')
        callDeclaredInitializedIdentifierListLiteral.listLiteral.accept(self)

    def visitCallDeclaredInitializedIdentifier(self, callDeclaredInitializedIdentifier):
        # print("visitCallDeclaredInitializedIdentifier")
        callDeclaredInitializedIdentifier.declaredIdentifier.accept(self)
        print(' = ', end='')
        callDeclaredInitializedIdentifier.expression.accept(self)

    def visitIdInitList(self, idInitList):
        # print("visitIdInitList")
        idInitList.listLiteral.accept(self)
        print(' = ', end='')
        idInitList.expression.accept(self)


    def visitCallIdListAtribuirIdList(self, callIdListAtribuirIdList):
        # print("visitCallIdListAtribuirIdList")
        callIdListAtribuirIdList.listLiteral.accept(self)
        print(' = ', end='')
        callIdListAtribuirIdList.listLiteral2.accept(self)


    ''' expressionStatement '''
    def visitConcretexpression(self, concretexpression):
        # print("visitConcretexpression")
        if concretexpression.expression != ';':
            concretexpression.expression.accept(self)
            print(' ;', end='\n')
        else:
            print(' ;', end='\n')


    '''expression '''
    def visitCallExpression(self, callExpression):
        # print("visitCallExpression")
        callExpression.orExpression.accept(self)


    ''' orExpression '''
    def visitCallandExpression(self, callandExpression):
        # print("visitCallandExpression")
        callandExpression.andExpression.accept(self)

    def visitExpressionORexpression(self, expressionORexpression):
        # print("visitExpressionORexpression")
        expressionORexpression.orExpression.accept(self)
        print(' || ', end='')
        expressionORexpression.andExpression.accept(self)


    ''' andExpression '''
    def visitCalligualExpression(self, calligualExpression):
        # print("visitCalligualExpression")
        calligualExpression.equalityExpression.accept(self)
    
    def visitCallAndExpressionIgual(self, callAndExpressionIgual):
        # print("visitCallAndExpressionIgual")
        callAndExpressionIgual.andExpression.accept(self)
        print(' && ', end='')
        callAndExpressionIgual.equalityExpression.accept(self)

    
    ''' equalityExpression '''
    def visitCallRelacionalExpression(self, callRelacionalExpression):
        # print("visitCallRelacionalExpression")
        callRelacionalExpression.relacionalExpression.accept(self)

    def visitCallEqualityExpression(self, callEqualityExpression):
        # print("visitCallEqualityExpression")
        callEqualityExpression.equalityExpression.accept(self)
        if callEqualityExpression.operation   ==  '==':
            print(' == ', end='')
        else:
            print(' != ', end='')
        callEqualityExpression.relacionalExpression.accept(self)
        

    ''' relacionalExpression '''
    def visitCallUnary(self, callUnary):
        # print("visitCallUnary")
        callUnary.addExpression.accept(self)
        
    
    def visitCallConcretExpression(self, callConcretExpression):
        # print("visitCallConcretExpression")
        callConcretExpression.relacionalExpression.accept(self)
        if callConcretExpression.operation   ==  '<':
            print(' < ', end='')
        elif callConcretExpression.operation ==  '>':
            print(' > ', end='')
        elif callConcretExpression.operation == '>=':
            print(' >= ', end='')
        else:
            print(' >= ', end='')
        callConcretExpression.addExpression.accept(self)


    ''' addExpression '''
    def visitCallMultExpression(self, callMultExpression):
        # print("visitCallMultExpression")
        callMultExpression.multExpression.accept(self)
        
    def visitCallAddExpressionMult(self, callAddExpressionMult):
        # print("visitCallAddExpressionMult")
        callAddExpressionMult.addExpression.accept(self)
        if callAddExpressionMult.operation == '+':
            print(' + ', end='')
        else:
            print(' - ', end='')
        callAddExpressionMult.multExpression.accept(self)
        

    ''' multExpression '''
    def visitCallUnaryExp(self, callUnaryExp):
        # print("visitCallUnaryExp")
        callUnaryExp.unaryExpression.accept(self)
    
    def visitCallUnaryExpMultExpression(self, callUnaryExpMultExpression):
        # print("visitCallUnaryExpMultExpression")
        callUnaryExpMultExpression.multExpression.accept(self)
        if callUnaryExpMultExpression.operation   == '*':
            print(' * ', end='')
        elif callUnaryExpMultExpression.operation == '/':
            print(' / ', end='')
        else:
            print(' % ', end='')
        callUnaryExpMultExpression.unaryExpression.accept(self)


    ''' unaryExpression '''
    def visitCallprimaryExpression(self, callprimaryExpression):
        # print("visitCallprimaryExpression")
        callprimaryExpression.primary.accept(self)
    
    def visitCallfunctioncall(self, callfunctioncall):
        # print("visitCallfunctioncall")
        callfunctioncall.functionCall.accept(self)

    def visitConcreteunaryExpression(self, concreteunaryExpression):
        # print("visitConcreteunaryExpression")
        concreteunaryExpression.unaryExpression.accept(self)
        if concreteunaryExpression.operation == '++':
            print(' ++ ', end='')
        else:
            print(' -- ', end='')


    ''' functionCall '''
    def visitConcretFunctionCall(self, concretFunctionCall):
        # print("visitConcretFunctionCall")
        concretFunctionCall.functionSignature.accept(self)
        


    ''' primary '''
    def visitCallPrimaryLiteral(self, callPrimaryLiteral):
        # print("visitCallPrimaryLiteral")
        print(callPrimaryLiteral.literal, end='')
        

    def visitCallPrimaryExpression(self, callPrimaryExpression):
        # print("visitCallNormalFormalParameters")
        print(' ( ', end='')
        callPrimaryExpression.expression.accept(self)
        print(' ) ', end='')
        

    ''' literal '''
    def visitCallLiteralListLiteral(self, callLiteralListLiteral):
        # print("visitCallLiteralListLiteral")
        callLiteralListLiteral.listLiteral.accept(self)

    def visitCallLiteralBooleanLiteral(self, callLiteralBooleanLiteral):
        # print("visitCallLiteralBooleanLiteral")
        callLiteralBooleanLiteral.booleanLiteral.accept(self)

    def visitCallLiteralId(self, callLiteralId):
        # print("visitCallLiteralId")
        print(callLiteralId.id, end='')
        

    ''' listLiteral'''

    def visitCallIdListlistLiteral(self, callIdListlistLiteral):
        # print("visitCallIdListlistLiteral")
        print(callIdListlistLiteral.id, end='')
        print((' [ '), end='')
        print((' ] '), end='')

    def visitCallIdExpListlistLiteral(self, callIdExpListlistLiteral):
        # print("visitCallIdExpListlistLiteral")
        print(callIdExpListlistLiteral.id, end='')
        print((' [ '), end='')
        callIdExpListlistLiteral.expressionList.accept(self)
        print((' ] '), end='')

    def visitExpressionListlistLiteral(self, expressionListlistLiteral):
        # print("visitExpressionListlistLiteral")
        print((' [ '), end='')
        expressionListlistLiteral.expressionList.accept(self)
        print((' ] '), end='')


    ''' booleanLiteral'''
    def visitbooleanLiteralTrue(self, booleanLiteralTrue):
        # print("visitbooleanLiteralTrue")
        print(booleanLiteralTrue.true, end='')

    def visitbooleanLiteralFalse(self, booleanLiteralFalse):
        # print("visitbooleanLiteralFalse")
        print(booleanLiteralFalse.false, end='')


    ''' expressionList'''
    def visitConcreteExpression(self, concreteExpression):
        # print("visitConcreteExpression")
        concreteExpression.expression.accept(self)

    def visitCallExpressionList(self, callExpressionList):
        # print("visitCallExpressionList")
        callExpressionList.expression.accept(self)
        print(', ', end='')
        callExpressionList.expressionList.accept(self)


    " ReturnStatementExpression "
    def visitReturnStatementExpression(self, returnStatementExpression):
        #print("visitReturnStatementExpression")
        if returnStatementExpression.expression != ';':
            print('return ', end='')
            returnStatementExpression.expression.accept(self)
            print('; ', end='')
        else:
            print('return ', end='')
            print('; ', end='')


    ''' ifStatement '''
    def visitIfexpressionStatement(self, ifexpressionStatement):
        # print("visitIfexpressionStatement")
        print(ifexpressionStatement.IF, end='')
        print(' ( ', end='')
        ifexpressionStatement.expression.accept(self)
        print(' ) ', end='')
        ifexpressionStatement.statement.accept(self)   

    def visitIfElseExpressionStatement(self, ifElseExpressionStatement):
        # print("visitIfElseExpressionStatement")
        print(ifElseExpressionStatement.IF, end='')
        print(' ( ', end='')
        ifElseExpressionStatement.expression.accept(self)
        print(' ) ', end='')
        ifElseExpressionStatement.statement.accept(self)
        print(ifElseExpressionStatement.ELSE, end='')
        ifElseExpressionStatement.statement01.accept(self)     


    ''' forStatement '''
    def visitConcreteForLoopParts(self, concreteForLoopParts):
        # print("visitConcreteForLoopParts")
        print(concreteForLoopParts.FOR, end='')
        print(' ( ', end='')
        concreteForLoopParts.forLoopParts.accept(self)
        print(' ) ', end='')
        concreteForLoopParts.statement.accept(self)    


    ''' forLoopParts '''
    def visitConcreteForInitializerStatement(self, concreteForInitializerStatement):
        # print("visitConcreteForInitializerStatement")
        concreteForInitializerStatement.forInitializerStatement.accept(self)
        print('; ', end='\n')    

    def visitForInitializerStatementExpressionList(self, forInitializerStatementExpressionList):
        # print("visitForInitializerStatementExpressionList")
        forInitializerStatementExpressionList.forInitializerStatement.accept(self)
        print('; ', end='\n')
        forInitializerStatementExpressionList.expressionList.accept(self)     

    def visitForInitializerStatementExpression(self, forInitializerStatementExpression):
        # print("visitForInitializerStatementExpression")
        forInitializerStatementExpression.forInitializerStatement.accept(self)
        forInitializerStatementExpression.expression.accept(self)
        print('; ', end='\n')      

    def visitExpressionForInitializerStatementExpressionList(self, expressionForInitializerStatementExpressionList):
        # print("visitExpressionForInitializerStatementExpressionList")
        expressionForInitializerStatementExpressionList.forInitializerStatement.accept(self)
        expressionForInitializerStatementExpressionList.expression.accept(self)
        print('; ', end='\n')
        expressionForInitializerStatementExpressionList.expressionList.accept(self)         


    ''' forInitializerStatement '''
    def visitConcreteLocalVariableDeclaration(self, concreteLocalVariableDeclaration):
        # print("visitConcreteLocalVariableDeclaration")
        concreteLocalVariableDeclaration.localVariableDeclaration.accept(self)     

    def visitCallConcreteExpression(self, callConcreteExpression):
        # print("visitCallConcreteExpression")
        if (callConcreteExpression.expression != None):
            callConcreteExpression.expression.accept(self)
        print('; ', end='\n')      

   
    ''' whileStatement  '''
    def visitWhileStatementExpressionStatement(self, whileStatementExpressionStatement):
        # print("visitWhileStatementExpressionStatement")        
        print(whileStatementExpressionStatement.WHILE, end='')
        print(' ( ', end='')
        whileStatementExpressionStatement.expression.accept(self)
        print(' ) ', end='')
        whileStatementExpressionStatement.statement.accept(self)


    ''' doStatement '''
    def visitDOStatementWhileExpression(self, DOStatementWhileExpression):
        # print("visitDOStatementWhileExpression")        
        print(DOStatementWhileExpression.DO, end='')
        DOStatementWhileExpression.statement.accept(self)
        print(DOStatementWhileExpression.WHILE, end='')
        print(' ( ', end='')
        DOStatementWhileExpression.expression.accept(self)
        print(' ) ', end='')
        print(' ; ', end='\n')
        print('')     


    ''' switchCaseRepetition '''
    def visitRepetitionSwitchCase(self, repetitionSwitchCase):
        # print("visitRepetitionSwitchCase")
        repetitionSwitchCase.switchCase.accept(self)
        repetitionSwitchCase.switchCaseRepetition.accept(self)
        
    def visitRepetitionSwitchCase2(self, repetitionSwitchCase2):
        # print("visitRepetitionSwitchCase2")
        repetitionSwitchCase2.switchCase.accept(self)


    ''' switchStatement '''
    def visitConcreteSwitch(self, concreteSwitch):
        # print("visitConcreteSwitch")        
        print(concreteSwitch.switch, end='')
        print(' ( ', end='')      
        concreteSwitch.expression.accept(self)
        print(' ) ', end='')
        print(' { ', end='')
        concreteSwitch.switchCaseRepetition.accept(self)        
        print(' } ', end='')
    
    def visitConcreteDefaultCase(self, concreteDefaultCase):
        # print("visitConcreteDefaultCase")        
        print(concreteDefaultCase.switch, end='')
        print(' ( ', end='')      
        concreteDefaultCase.expression.accept(self)
        print(' ) ', end='')
        print(' { ', end='')
        concreteDefaultCase.switchCaseRepetition.accept(self)
        concreteDefaultCase.defaultCase.accept(self)        
        print(' } ', end='')

    ''' switchCase'''
    def visitExpressionSwitchCase(self, expressionSwitchCase):
        # print("visitExpressionSwitchCase")
        print(expressionSwitchCase.CASE, end=' ')
        expressionSwitchCase.expression.accept(self)
        print(' : ', end='')
        expressionSwitchCase.statements.accept(self)

    def visitLabelSwitchCase(self, labelSwitchCase):
        # print("visitLabelSwitchCase")
        labelSwitchCase.label.accept(self)
        labelSwitchCase.switchCase.accept(self)

    ''' defaultCase'''
    def visitDefaultStatements(self, defaultStatements):
        # print("visitDefaultStatements")
        print(defaultStatements.default, end='')
        print(' : ', end='')
        defaultStatements.statements.accept(self)
    
    def visitLabelDefaultCase(self, labelDefaultCase):
        # print("visitLabelDefaultCase")
        labelDefaultCase.label.accept(self)
        labelDefaultCase.defaultCase.accept(self)


    ''' label ''' 
    def visitIdPontos(self, idPontos):
        # print("visitIdPontos")
        print(idPontos.id, end='')
        print(' : ', end='')
    

    ''' break '''
    def visitCallBreak(self, callBreak):
        print("visitCallBreak")
        print(callBreak.BREAK, end='')
        print('; ', end='\n')
    
    def visitBreakID(self, breakID):
        # print("visitBreakID")
        print(breakID.BREAK, end='')
        print(breakID.id, end='')
        print(' ; ', end='\n')

# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftCONCATASSIGN CHARS COMA CONCAT DIVIDE ID IMPRIMIRRESULTADO LPAREN MINUS NUMBER PLUS QUOTE RPAREN TIMESinicio : expresion\n              | inicio expresionexpresion : expresion PLUS expresion\n                 | expresion MINUS expresion\n                 | expresion TIMES expresion\n                 | expresion DIVIDE expresionexpresion : ID ASSIGN expresionexpresion : IMPRIMIRRESULTADO LPAREN expresion RPARENexpresion : CONCAT LPAREN lista_expresiones RPARENlista_expresiones : expresion\n                         | lista_expresiones COMA expresionexpresion : IDexpresion : QUOTE CHARS QUOTEexpresion : NUMBERexpresion : LPAREN expresion RPARENexpresion : CHARS'
    
_lr_action_items = {'ID':([0,1,2,3,5,8,9,10,11,12,13,14,15,16,18,20,21,22,23,24,26,29,30,31,32,],[3,3,-1,-12,3,-16,-14,-2,3,3,3,3,3,3,3,-3,-4,-5,-6,-7,-15,-13,-8,-9,3,]),'IMPRIMIRRESULTADO':([0,1,2,3,5,8,9,10,11,12,13,14,15,16,18,20,21,22,23,24,26,29,30,31,32,],[4,4,-1,-12,4,-16,-14,-2,4,4,4,4,4,4,4,-3,-4,-5,-6,-7,-15,-13,-8,-9,4,]),'CONCAT':([0,1,2,3,5,8,9,10,11,12,13,14,15,16,18,20,21,22,23,24,26,29,30,31,32,],[6,6,-1,-12,6,-16,-14,-2,6,6,6,6,6,6,6,-3,-4,-5,-6,-7,-15,-13,-8,-9,6,]),'QUOTE':([0,1,2,3,5,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,26,29,30,31,32,],[7,7,-1,-12,7,-16,-14,-2,7,7,7,7,7,7,7,29,-3,-4,-5,-6,-7,-15,-13,-8,-9,7,]),'NUMBER':([0,1,2,3,5,8,9,10,11,12,13,14,15,16,18,20,21,22,23,24,26,29,30,31,32,],[9,9,-1,-12,9,-16,-14,-2,9,9,9,9,9,9,9,-3,-4,-5,-6,-7,-15,-13,-8,-9,9,]),'LPAREN':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,18,20,21,22,23,24,26,29,30,31,32,],[5,5,-1,-12,16,5,18,-16,-14,-2,5,5,5,5,5,5,5,-3,-4,-5,-6,-7,-15,-13,-8,-9,5,]),'CHARS':([0,1,2,3,5,7,8,9,10,11,12,13,14,15,16,18,20,21,22,23,24,26,29,30,31,32,],[8,8,-1,-12,8,19,-16,-14,-2,8,8,8,8,8,8,8,-3,-4,-5,-6,-7,-15,-13,-8,-9,8,]),'$end':([1,2,3,8,9,10,20,21,22,23,24,26,29,30,31,],[0,-1,-12,-16,-14,-2,-3,-4,-5,-6,-7,-15,-13,-8,-9,]),'PLUS':([2,3,8,9,10,17,20,21,22,23,24,25,26,28,29,30,31,33,],[11,-12,-16,-14,11,11,-3,-4,-5,-6,11,11,-15,11,-13,-8,-9,11,]),'MINUS':([2,3,8,9,10,17,20,21,22,23,24,25,26,28,29,30,31,33,],[12,-12,-16,-14,12,12,-3,-4,-5,-6,12,12,-15,12,-13,-8,-9,12,]),'TIMES':([2,3,8,9,10,17,20,21,22,23,24,25,26,28,29,30,31,33,],[13,-12,-16,-14,13,13,13,13,-5,-6,13,13,-15,13,-13,-8,-9,13,]),'DIVIDE':([2,3,8,9,10,17,20,21,22,23,24,25,26,28,29,30,31,33,],[14,-12,-16,-14,14,14,14,14,-5,-6,14,14,-15,14,-13,-8,-9,14,]),'ASSIGN':([3,],[15,]),'RPAREN':([3,8,9,17,20,21,22,23,24,25,26,27,28,29,30,31,33,],[-12,-16,-14,26,-3,-4,-5,-6,-7,30,-15,31,-10,-13,-8,-9,-11,]),'COMA':([3,8,9,20,21,22,23,24,26,27,28,29,30,31,33,],[-12,-16,-14,-3,-4,-5,-6,-7,-15,32,-10,-13,-8,-9,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'expresion':([0,1,5,11,12,13,14,15,16,18,32,],[2,10,17,20,21,22,23,24,25,28,33,]),'lista_expresiones':([18,],[27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> expresion','inicio',1,'p_inicio','parser.py',15),
  ('inicio -> inicio expresion','inicio',2,'p_inicio','parser.py',16),
  ('expresion -> expresion PLUS expresion','expresion',3,'p_expresion_binaria','parser.py',24),
  ('expresion -> expresion MINUS expresion','expresion',3,'p_expresion_binaria','parser.py',25),
  ('expresion -> expresion TIMES expresion','expresion',3,'p_expresion_binaria','parser.py',26),
  ('expresion -> expresion DIVIDE expresion','expresion',3,'p_expresion_binaria','parser.py',27),
  ('expresion -> ID ASSIGN expresion','expresion',3,'p_asignacion','parser.py',38),
  ('expresion -> IMPRIMIRRESULTADO LPAREN expresion RPAREN','expresion',4,'p_expresion_imprimir','parser.py',46),
  ('expresion -> CONCAT LPAREN lista_expresiones RPAREN','expresion',4,'p_expresion_concat','parser.py',51),
  ('lista_expresiones -> expresion','lista_expresiones',1,'p_lista_expresiones','parser.py',57),
  ('lista_expresiones -> lista_expresiones COMA expresion','lista_expresiones',3,'p_lista_expresiones','parser.py',58),
  ('expresion -> ID','expresion',1,'p_expresion_variable','parser.py',66),
  ('expresion -> QUOTE CHARS QUOTE','expresion',3,'p_expresion_cadena','parser.py',73),
  ('expresion -> NUMBER','expresion',1,'p_expresion_numero','parser.py',77),
  ('expresion -> LPAREN expresion RPAREN','expresion',3,'p_expresion_parentesis','parser.py',81),
  ('expresion -> CHARS','expresion',1,'p_repeat','parser.py',85),
]

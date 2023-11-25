
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATRIBUT CLASS COMA ELSE EQUAL ID IDENTACAO IF LPAREN NEWLINE RPAREN SPACE TAG TEXTO TEXTPLAIN VARhtml :   linhas\n    linhas : linhas NEWLINE linha_normal\n                | linha_normal\n                | linhas NEWLINE linha_codigo\n                | linha_codigo\n                | linhas NEWLINE linha_var\n                | linha_var\n                | linhas NEWLINE linha_textplain\n    linha_var :  IDENTACAO VAR TEXTO EQUAL TEXTO\n                    | VAR TEXTO EQUAL TEXTO\n    linha_codigo :   IDENTACAO IF TEXTO\n                        | IF TEXTO\n                        | IDENTACAO ELSE\n                        | ELSE\n    linha_normal :  IDENTACAO corpo COMA\n                | IDENTACAO corpo\n                | corpo\n    linha_textplain : IDENTACAO TEXTPLAIN corpo :  tag\n                | tag SPACE\n                | tag SPACE TEXTO\n                | tag EQUAL SPACE TEXTO\n    tag :  tag TAG atributos_linha\n                | tag CLASS atributos_linha\n                | tag ID atributos_linha\n                |\n    atributos_linha :  LPAREN atributos RPAREN\n                        |\n    atributos :   ATRIBUT \n                    | ATRIBUT atributos\n    '
    
_lr_action_items = {'IDENTACAO':([0,12,],[6,28,]),'IF':([0,6,12,28,],[8,14,8,14,]),'ELSE':([0,6,12,28,],[9,15,9,15,]),'VAR':([0,6,12,28,],[10,16,10,16,]),'SPACE':([0,6,11,12,20,21,22,23,28,35,37,38,46,],[-26,-26,19,-26,34,-28,-28,-28,-26,-23,-24,-25,-27,]),'EQUAL':([0,6,11,12,18,21,22,23,28,31,35,37,38,46,],[-26,-26,20,-26,32,-28,-28,-28,-26,40,-23,-24,-25,-27,]),'TAG':([0,6,11,12,21,22,23,28,35,37,38,46,],[-26,-26,21,-26,-28,-28,-28,-26,-23,-24,-25,-27,]),'CLASS':([0,6,11,12,21,22,23,28,35,37,38,46,],[-26,-26,22,-26,-28,-28,-28,-26,-23,-24,-25,-27,]),'ID':([0,6,11,12,21,22,23,28,35,37,38,46,],[-26,-26,23,-26,-28,-28,-28,-26,-23,-24,-25,-27,]),'NEWLINE':([0,2,3,4,5,6,7,9,11,12,13,15,17,19,21,22,23,24,25,26,27,28,29,30,33,35,37,38,39,41,42,45,46,],[-26,12,-3,-5,-7,-26,-17,-14,-19,-26,-16,-13,-12,-20,-28,-28,-28,-2,-4,-6,-8,-26,-15,-11,-21,-23,-24,-25,-18,-10,-22,-9,-27,]),'$end':([0,1,2,3,4,5,6,7,9,11,12,13,15,17,19,21,22,23,24,25,26,27,28,29,30,33,35,37,38,39,41,42,45,46,],[-26,0,-1,-3,-5,-7,-26,-17,-14,-19,-26,-16,-13,-12,-20,-28,-28,-28,-2,-4,-6,-8,-26,-15,-11,-21,-23,-24,-25,-18,-10,-22,-9,-27,]),'COMA':([6,11,13,19,21,22,23,28,33,35,37,38,42,46,],[-26,-19,29,-20,-28,-28,-28,-26,-21,-23,-24,-25,-22,-27,]),'TEXTO':([8,10,14,16,19,32,34,40,],[17,18,30,31,33,41,42,45,]),'LPAREN':([21,22,23,],[36,36,36,]),'TEXTPLAIN':([28,],[39,]),'ATRIBUT':([36,44,],[44,44,]),'RPAREN':([43,44,47,],[46,-29,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'html':([0,],[1,]),'linhas':([0,],[2,]),'linha_normal':([0,12,],[3,24,]),'linha_codigo':([0,12,],[4,25,]),'linha_var':([0,12,],[5,26,]),'corpo':([0,6,12,28,],[7,13,7,13,]),'tag':([0,6,12,28,],[11,11,11,11,]),'linha_textplain':([12,],[27,]),'atributos_linha':([21,22,23,],[35,37,38,]),'atributos':([36,44,],[43,47,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> html","S'",1,None,None,None),
  ('html -> linhas','html',1,'p_html','yac_pug.py',8),
  ('linhas -> linhas NEWLINE linha_normal','linhas',3,'p_linhas','yac_pug.py',13),
  ('linhas -> linha_normal','linhas',1,'p_linhas','yac_pug.py',14),
  ('linhas -> linhas NEWLINE linha_codigo','linhas',3,'p_linhas','yac_pug.py',15),
  ('linhas -> linha_codigo','linhas',1,'p_linhas','yac_pug.py',16),
  ('linhas -> linhas NEWLINE linha_var','linhas',3,'p_linhas','yac_pug.py',17),
  ('linhas -> linha_var','linhas',1,'p_linhas','yac_pug.py',18),
  ('linhas -> linhas NEWLINE linha_textplain','linhas',3,'p_linhas','yac_pug.py',19),
  ('linha_var -> IDENTACAO VAR TEXTO EQUAL TEXTO','linha_var',5,'p_linha_var','yac_pug.py',74),
  ('linha_var -> VAR TEXTO EQUAL TEXTO','linha_var',4,'p_linha_var','yac_pug.py',75),
  ('linha_codigo -> IDENTACAO IF TEXTO','linha_codigo',3,'p_linha_codigo','yac_pug.py',95),
  ('linha_codigo -> IF TEXTO','linha_codigo',2,'p_linha_codigo','yac_pug.py',96),
  ('linha_codigo -> IDENTACAO ELSE','linha_codigo',2,'p_linha_codigo','yac_pug.py',97),
  ('linha_codigo -> ELSE','linha_codigo',1,'p_linha_codigo','yac_pug.py',98),
  ('linha_normal -> IDENTACAO corpo COMA','linha_normal',3,'p_linha_normal','yac_pug.py',112),
  ('linha_normal -> IDENTACAO corpo','linha_normal',2,'p_linha_normal','yac_pug.py',113),
  ('linha_normal -> corpo','linha_normal',1,'p_linha_normal','yac_pug.py',114),
  ('linha_textplain -> IDENTACAO TEXTPLAIN','linha_textplain',2,'p_linha_textplain','yac_pug.py',129),
  ('corpo -> tag','corpo',1,'p_corpo','yac_pug.py',133),
  ('corpo -> tag SPACE','corpo',2,'p_corpo','yac_pug.py',134),
  ('corpo -> tag SPACE TEXTO','corpo',3,'p_corpo','yac_pug.py',135),
  ('corpo -> tag EQUAL SPACE TEXTO','corpo',4,'p_corpo','yac_pug.py',136),
  ('tag -> tag TAG atributos_linha','tag',3,'p_tag','yac_pug.py',146),
  ('tag -> tag CLASS atributos_linha','tag',3,'p_tag','yac_pug.py',147),
  ('tag -> tag ID atributos_linha','tag',3,'p_tag','yac_pug.py',148),
  ('tag -> <empty>','tag',0,'p_tag','yac_pug.py',149),
  ('atributos_linha -> LPAREN atributos RPAREN','atributos_linha',3,'p_atributos_linha','yac_pug.py',162),
  ('atributos_linha -> <empty>','atributos_linha',0,'p_atributos_linha','yac_pug.py',163),
  ('atributos -> ATRIBUT','atributos',1,'p_atributos','yac_pug.py',171),
  ('atributos -> ATRIBUT atributos','atributos',2,'p_atributos','yac_pug.py',172),
]
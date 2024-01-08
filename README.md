# PUG -> HTML converter
As part of the Language Processing course, we were presented with various problem/challenge statements, from which we had to select one to solve. Therefore, we thought that the most interesting one would be the Pug to HTML(2.5) converter. Despite being two relatively similar languages, they have some differences that were challenging to implement. For this, we used the Python programming language and the Ply library, which provides us with ply.lex and ply.yacc tools. Using these, we created a lexer and a parser.

Pug is a simplified markup language that allows writing HTML in a more concise and indented manner, while HTML is the standard language for structuring and displaying content on the web. Implementing a converter between these languages involves dealing with the nuances of each and transforming Pug code into valid HTML.

The use of the Ply library in Python to create the lexer (lexical analyzer) and parser (syntax analyzer) facilitates the analysis and transformation of Pug code into its equivalent representation in HTML. The lexer tokenizes the source code into smaller chunks, while the parser interprets the syntactic structure of these tokens to generate the desired output in HTML.

This project likely involved identifying and manipulating specific elements of Pug, such as significant indentation, abbreviations, and other unique characteristics, to produce semantically correct and structured HTML code.

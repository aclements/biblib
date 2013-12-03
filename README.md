Biblib provides a simple, standalone Python3 package for parsing
BibTeX bibliographic databases, as well as algorithms for manipulating
BibTeX entries in BibTeX-y ways.

There are a lot of BibTeX parsers out there.  Most of them are
complete nonsense based on some imaginary grammar made up by the
module's author that is almost, but not quite, entirely unlike
BibTeX's actual grammar.  *BibTeX has a grammar*.  It's even pretty
simple, though it's probably not what you think it is.  The hardest
part of BibTeX's grammar is that it's only written down in one place:
the BibTeX source code.

Biblib's parser is derived directly from the WEB source code for
BibTeX and hence (barring bugs in translation) should be fully
compatible with BibTeX's own parser.


Features
--------

* BibTeX-compatible `.bib` file parser

* BibTeX-compatible name parser for fields like `author`

* Crossref resolution

* BibTeX-compatible title casing

* Translator for common TeX markup (like accents) to Unicode (which
  can, in turn, be used in HTML and other formats).


Installation
------------

Since biblib has no external dependencies or C modules, you can use
biblib in your project by simply unpacking it under your source tree
and adding

    sys.path.append('biblib')

before importing it.

Biblib can also be installed system-wide with

    python3 setup.py install


Examples
--------

There are a few simple examples of biblib's use in `examples/`.  To
run these dircetly from the source tree, use, for example

    PYTHONPATH=$PWD ./examples/bibparse


Recognized grammar
------------------

For reference, the `.bib` parser implements a grammar equivalent to
the following PEG.  All literals are matched case-*insensitively*.

    bib_db = comment (command_or_entry comment)*

    comment = [^@]*

    ws = [ \t\n]*

    ident = ![0-9] (![ \t"#%'(),={}] [\x20-\x7f])+

    command_or_entry = '@' ws (comment / preamble / string / entry)

    comment = 'comment'

    preamble = 'preamble' ws ( '{' ws preamble_body ws '}'
                             / '(' ws preamble_body ws ')' )

    preamble_body = value

    string = 'string' ws ( '{' ws string_body ws '}'
                         / '(' ws string_body ws ')' )

    string_body = ident ws '=' ws value

    entry = ident ws ( '{' ws key ws entry_body? ws '}'
                     / '(' ws key_paren ws entry_body? ws ')' )

    key = [^, \t}\n]*

    key_paren = [^, \t\n]*

    entry_body = (',' ws ident ws '=' ws value ws)* ','?

    value = piece (ws '#' ws piece)*

    piece
        = [0-9]+
        / '{' balanced* '}'
        / '"' (!'"' balanced)* '"'
        / ident

    balanced
        = '{' balanced* '}'
        / [^{}]

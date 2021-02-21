#!/usr/bin/env python

"""
Pandoc filter to convert code blocks to reveal.js compatible <code>...</code>
"""
import sys

from pandocfilters import toJSONFilter, RawBlock

def htmlblock(code):
    """Html block"""
    return RawBlock('html', code)

def codehighlight(key, value, format, meta):
    if key == 'CodeBlock' and format == 'revealjs':
        [[ident, classes, keyvals], code] = value
        code_attrs = ''
        for keyval in keyvals:
            code_attrs += keyval[0] + '="' + keyval[1] + '" '
        return [htmlblock('<pre><code data-trim ' + code_attrs + '>\n' + str(code) + '\n</code></pre>')]

if __name__ == "__main__":
    toJSONFilter(codehighlight)

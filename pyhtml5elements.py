#!/usr/bin/python
# -*- coding: latin1 -*- aka: ISO-8859
"""
Minimalist implementation of html5 supported element tags
"""

# Dictionary of supported elements
#   The element names are the keys;
#   The values are tuples, each containing:
#       the element's open tag;
#       the element's close tag;
#       a descritive comment from W3C
SUPPORTED_ELEMENTS = {
    'comment': ('<!--',
                '-->',
                'Defines a comment'),
    'doctype': ('<!DOCTYPE html>',
                '',
                'Defines the document type'),
    'hyperlink': ('<a>',
                  '</a>',
                  'Defines a hyperlink'),
    'abbreviation': ('<abbr>',
                     '</abbr>',
                     'Defines an abbreviation or an acronym'),
    'address': ('<address>',
                '</address>',
                'Defines contact info for the author/owner of a document'),
    'area': ('<area>',
             '',
             'Defines an area inside an image-map'),
    'article': ('<article>',
                '</article>',
                'Defines an article'),
    'aside': ('<aside>',
              '</aside>',
              'Defines content aside from the page content'),
    'audio': ('<audio>',
              '',
              'Defines sound content'),
    'bold': ('<b>',
             '</b>',
             'Defines bold text'),
    'base': ('<base>',
             '',
             'Specifies the base URL/target for relative URLs in a document'),
    'direction': ('<bdi>',
                  '</bdi>',
                  'Isolates a part of text that might be formatted in a \
                  different direction from other text outside it'),
    'override': ('<bdo>',
                 '</bdo>',
                 'Overrides the current text direction'),
    'blockquote': ('<blockquote>',
                   '</blockquote>',
                   'Defines a section that is quoted from another source'),
    'body': ('<body>',
             '</body>',
             'Defines the document\'s body'),
    'break': ('<br>',
              '',
              'Defines a single line break'),
    'button': ('<button>',
               '</button>',
               'Defines a clickable button'),
    'canvas': ('<canvas>',
               '</canvas>',
               'Used to draw graphics, on the fly (usually JavaScript)'),
    'caption': ('<caption>',
                '</caption>',
                'Defines a table caption'),
    'cite': ('<cite>',
             '</cite>',
             'Defines the title of a work'),
    'code': ('<code>',
             '</code>',
             'Defines a piece of computer code'),
    'column': ('<col>',
               '',
               'Specifies column props for each column within a <colgroup>'),
    'columngroup': ('<colgroup>',
                    '</colgroup>',
                    'Specifies a group of columns in a table for formatting'),
    'datalist': ('<datalist>',
                 '</datalist>',
                 'Specifies a list of pre-defined options for input controls'),
    'desclistvalue': ('<dd>',
                      '</dd>',
                      'Defines a description/value of a term in a desc. list'),
    'deleted': ('<del>',
                '</del>',
                'Defines text that has been deleted from a document'),
    'details': ('<details>',
                '</details>',
                'Defines additional details that the user can view or hide'),
    'define': ('<dfn>',
               '</dfn>',
               'Represents the defining instance of a term'),
    'dialog': ('<dialog>',
               '</dialog>',
               'Defines a dialog box or window'),
    'div': ('<div>',
            '</div>',
            'Defines a section in a document'),
    'desclist': ('<dl>',
                 '</dl>',
                 'Defines a description list'),
    'desclistterm': ('<dt>',
                     '</dt>',
                     'Defines a term/name in a description list'),
    'emphasis': ('<em>',
                 '</em>',
                 'Defines emphasized text '),
    'embed': ('<embed>',
              '',
              'Defines a container for an external (non-HTML) application'),
    'fieldset': ('<fieldset>',
                 '</fieldset>',
                 'Groups related elements in a form'),
    'figurecaption': ('<figcaption>',
                      '</figcaption>',
                      'Defines a caption for a <figure> element'),
    'figure': ('<figure>',
               '</figure>',
               'Specifies self-contained content'),
    'footer': ('<footer>',
               '</footer>',
               'Defines a footer for a document or section'),
    'form': ('<form>',
             '</form>',
             'Defines an HTML form for user input'),
    'heading1': ('<h1>',
                 '</h1>',
                 'Defines HTML heading 1'),
    'heading2': ('<h2>',
                 '</h2>',
                 'Defines HTML heading 2'),
    'heading3': ('<h3>',
                 '</h3>',
                 'Defines HTML heading 3'),
    'heading5': ('<h5>',
                 '</h5>',
                 'Defines HTML heading 5'),
    'heading4': ('<h4>',
                 '</h4>',
                 'Defines HTML heading 4'),
    'heading6': ('<h6>',
                 '</h6>',
                 'Defines HTML heading 6'),
    'head': ('<head>',
             '</head>', 'Defines information about the document'),
    'header': ('<header>',
               '</header>',
               'Defines a header for a document or section'),
    'horizontalruler': ('<hr>',
                        '',
                        'Defines a thematic change in the content'),
    'html': ('<html>',
             '</html>',
             'Defines the root of an HTML document'),
    'italic': ('<i>',
               '</i>',
               'Defines a part of text in an alternate voice or mood'),
    'iframe': ('<iframe>',
               '</iframe>',
               'Defines an inline frame'),
    'image': ('<img>',
              '',
              'Defines an image'),
    'input': ('<input>',
              '',
              'Defines an input control'),
    'inserted': ('<ins>',
                 '</ins>',
                 'Defines a text that has been inserted into a document'),
    'keyinput': ('<kbd>',
                 '</kbd>',
                 'Defines keyboard input'),
    'keygen': ('<keygen>',
               '',
               'Defines a key-pair generator field (for forms)'),
    'label': ('<label>',
              '</label>',
              'Defines a label for an <input> element'),
    'legend': ('<legend>',
               '</legend>',
               'Defines a caption for a <fieldset> element'),
    'listitem': ('<li>',
                 '</li>',
                 'Defines a list item'),
    'link': ('<link>',
             '',
             'Defines the relationship between a document and ext. resources'),
    'main': ('<main>',
             '</main>',
             'Specifies the main content of a document'),
    'map': ('<map>',
            '</map>',
            'Defines a client-side image-map'),
    'mark': ('<mark>',
             '</mark>',
             'Defines marked/highlighted text'),
    'menu': ('<menu>',
             '</menu>',
             'Defines a list/menu of commands'),
    'menuitem': ('<menuitem>',
                 '</menuitem>',
                 'Defines a command/menu item invokable from a popup menu'),
    'meta': ('<meta>',
             '',
             'Defines metadata about an HTML document'),
    'meter': ('<meter>',
              '</meter>',
              'Defines a scalar measurement within a known range (a gauge)'),
    'navlink': ('<nav>',
                '</nav>',
                'Defines navigation links'),
    'noscript': ('<noscript>',
                 '</noscript>',
                 'Defines alternate content for unsupp client-side scripts'),
    'object': ('<object>',
               '</object>',
               'Defines an embedded object'),
    'orderedlist': ('<ol>',
                    '</ol>',
                    'Defines an ordered list'),
    'optionsgroup': ('<optgroup>',
                     '</optgroup>',
                     'Defines a group of related options in a drop-down list'),
    'option': ('<option>',
               '</option>',
               'Defines an option in a drop-down list'),
    'output': ('<output>',
               '</output>',
               'Defines the result of a calculation'),
    'paragraph': ('<p>',
                  '</p>',
                  'Defines a paragraph'),
    'parameter': ('<param>',
                  '',
                  'Defines a parameter for an object'),
    'preformatted': ('<pre>',
                     '</pre>',
                     'Defines preformatted text'),
    'progress': ('<progress>',
                 '</progress>',
                 'Represents the progress of a task'),
    'quote': ('<q>',
              '</q>',
              'Defines a short quotation'),
    'rubynotsupported': ('<rp>',
                         '</rp>',
                         'Defines what to show for unsupp ruby annotations'),
    'rubysupported': ('<rt>',
                      '</rt>',
                      'Defines an explanation/pronunciation of characters'),
    'ruby': ('<ruby>',
             '</ruby>',
             'Defines a ruby annotation (for East Asian typography)'),
    'strikethrough': ('<s>',
                      '</s>',
                      'Defines text that is no longer correct'),
    'sample': ('<samp>',
               '</samp>',
               'Defines sample output from a computer program'),
    'script': ('<script>',
               '</script>',
               'Defines a client-side script'),
    'section': ('<section>',
                '</section>',
                'Defines a section in a document'),
    'select': ('<select>',
               '</select>',
               'Defines a drop-down list'),
    'small': ('<small>',
              '</small>',
              'Defines smaller text'),
    'source': ('<source>',
               '',
               'Defines media resources for media elms (<video> and <audio>)'),
    'span': ('<span>',
             '</span>',
             'Defines a section in a document'),
    'strong': ('<strong>',
               '</strong>',
               'Defines important text'),
    'style': ('<style>',
              '</style>',
              'Defines style information for a document'),
    'subscript': ('<sub>',
                  '</sub>',
                  'Defines subscripted text'),
    'summary': ('<summary>',
                '</summary>',
                'Defines a visible heading for a <details> element'),
    'superscript': ('<sup>',
                    '</sup>',
                    'Defines superscripted text'),
    'table': ('<table>',
              '</table>',
              'Defines a table'),
    'tablebody': ('<tbody>',
                  '</tbody>',
                  'Groups the body content in a table'),
    'tabledatacell': ('<td>',
                      '</td>',
                      'Defines a cell in a table'),
    'textarea': ('<textarea>',
                 '</textarea>',
                 'Defines a multiline input control (text area)'),
    'tablefooter': ('<tfoot>',
                    '</tfoot>',
                    'Groups the footer content in a table'),
    'tableheadcell': ('<th>',
                      '</th>',
                      'Defines a header cell in a table'),
    'tableheader': ('<thead>',
                    '</thead>',
                    'Groups the header content in a table'),
    'time': ('<time>',
             '</time>',
             'Defines a date/time'),
    'title': ('<title>',
              '</title>',
              'Defines a title for the document'),
    'tablerow': ('<tr>',
                 '</tr>',
                 'Defines a row in a table'),
    'track': ('<track>',
              '',
              'Defines text tracks for media elements (<video> and <audio>)'),
    'underline': ('<u>',
                  '</u>',
                  'Defines text that should have diff style from normal text'),
    'unorderedlist': ('<ul>',
                      '</ul>',
                      'Defines an unordered list'),
    'var': ('<var>',
            '</var>',
            'Defines a variable'),
    'video': ('<video>',
              '</video>',
              'Defines a video or movie'),
    'wordbreak': ('<wbr>',
                  '</wbr>',
                  'Defines a possible line-break')
}


class Element(object):

    """
    Common class for all html elements.

    An Element object has the following attributes:

    Attributes
    ---------------

    name :        str
                  defines the kind of an html element, such as heading,
                  a table or a page's body block. It is is set by __init__
                  method from the (required, str) constructor argument

    indent_size : int
                  element-wide indentation size for generated html code

    single_line : bool
                  element-wide single line flag (implies no indent output)

    __attribs :    dictionary
                  a dictionary containing Element's attributes and respective
                  values - the keys are the attribute names

    __content :   list
                  an html element's content - a list of strings and
                  other (nested) html pyhtml5elements.Element's

    """

    def __init__(self, name, indent_size=4, single_line=False):
        """Init name, indent_size and single_line from args."""
        # test for required argument 'name' type and value
        if not isinstance(name, str):
            raise TypeError
        elif name not in SUPPORTED_ELEMENTS.keys():
            raise ValueError
        else:
            self.name = name
        # Initialize empty attributes list
        self.__attribs = {}
        # Initialize empty inner content
        self.__content = []
        # Default element-wide generated html indent size
        self.indent_size = indent_size
        # Default single line renderization flag
        self.single_line = single_line

    def __repr__(self):
        """Return (partial) textual, representation of Element object."""
        return '{}({!r}, {!r}, {!r})'.format(
            self.__class__.__name__,
            self.name,
            self.indent_size,
            self.single_line)

    def __str__(self):
        """Renderize Element object as text."""
        # Check for non-text nested content (will force multiple lines output)
        text_nested_content = True
        for this_content in self.__content:
            if not isinstance(this_content, str):
                text_nested_content = False
        # Prepare indentation and newline strings to be used while redering
        if self.single_line is False or text_nested_content is False:
            new_line = "\n"
            indent = (" " * self.indent_size)
        else:
            new_line = ""
            indent = ""
        # Initialize empty report with open tag
        report = SUPPORTED_ELEMENTS[self.name][0]
        # Iterate attributes dictionary and add attributes to report
        if self.__attribs != {}:
            attrib_str = ""
            for this_attrib_key in self.__attribs:
                this_attrib_token_list = [
                    " ",
                    str(this_attrib_key),
                    "=\"",
                    str(self.__attribs[this_attrib_key]),
                    "\""
                ]
                attrib_str += "".join(this_attrib_token_list)
            attrib_str += ">"
            report = report.replace('>', attrib_str)
        # Add new line, as needed
        report += new_line
        # Add nested content (if any)
        for nested_content in self.__content:
            for line in str(nested_content).splitlines():
                report += indent + line + new_line
        # Add close tag
        if SUPPORTED_ELEMENTS[self.name][1] != "":
            report += SUPPORTED_ELEMENTS[self.name][1] + new_line
        # Return resulting string
        return report

    def add_inner_content(self, content):
        """Add inner content to Element object."""
        if not isinstance(content, str) and not isinstance(content, Element):
            print "Inner content of Element must be string or nested Element."
            raise TypeError
        else:
            self.__content.append(content)

    def add_attribute(self, attribute_name, attribute_value):
        """Add a attribute/value pair to Element object."""
        # test for 'attribute_name' type
        if not isinstance(attribute_name, str):
            print "type of attribute_name must be str."
            raise TypeError
        elif not isinstance(attribute_value, str):
            print "type of attribute_value must be str."
            raise TypeError
        elif self.name == "comment" or self.name == "doctype":
            print self.name + " html5 tags don't support attributes."
            raise ValueError
        else:
            self.__attribs.update({attribute_name: attribute_value})

    def help(self):
        """Return the W3C comment for Element object."""
        return SUPPORTED_ELEMENTS[self.name][2]

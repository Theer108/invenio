# -*- coding: utf-8 -*-
## This file is part of Invenio.
## Copyright (C) 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

### CONFIGURATION OPTIONS FOR BIBRECORD LIBRARY

"""BibRecord configuration file.

This file sets a list of errors that can be generated by BibRecord, the
default behaviours for the parsers used and the parsers available."""

import pkg_resources
# location of the MARC21 DTD file:
CFG_MARC21_DTD = pkg_resources.resource_filename('invenio.legacy.bibrecord.data', 'MARC21slim.dtd')

# internal dictionary of warning messages:
CFG_BIBRECORD_WARNING_MSGS = {
    0: "",
    1: "WARNING: tag missing for field(s)\nValue stored with tag '000'",
    2: "WARNING: bad range for tags (tag must be in range 001-999)\nValue stored with tag '000'",
    3: "WARNING: Missing atribute 'code' for subfield\nValue stored with code ''",
    4: "WARNING: Missing attribute 'ind1'\nValue stored with ind1 = ''",
    5: "WARNING: Missing attribute 'ind2'\nValue stored with ind2 = ''",
    6: "Import Error",
    7: "WARNING: value expected of type string.",
    8: "WARNING: empty datafield",
    98: "WARNING: problems importing invenio",
    99: "Document not well formed",
    }

# verbose level to be used when creating records from XML: (0=least, ..., 9=most)
CFG_BIBRECORD_DEFAULT_VERBOSE_LEVEL = 0

# correction level to be used when creating records from XML: (0=no, 1=yes)
CFG_BIBRECORD_DEFAULT_CORRECT = 0

# XML parsers available:
CFG_BIBRECORD_PARSERS_AVAILABLE = ['pyrxp', 'lxml', '4suite', 'minidom']

# Exceptions
class InvenioBibRecordParserError(Exception):
    """A generic parsing exception for all available parsers."""
    pass

class InvenioBibRecordFieldError(Exception):
    """An generic error for BibRecord."""
    pass
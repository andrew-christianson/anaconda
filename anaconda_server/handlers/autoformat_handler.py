# -*- coding: utf8 -*-

# Copyright (C) 2014 - Oscar Campos <oscar.campos@member.fsf.org>
# This program is Free Software see LICENSE file for details

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../anaconda_lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from commands import AutoPep8
from anaconda_handler import AnacondaHandler


class AutoFormatHandler(AnacondaHandler):
    """Handle request to execute auto format commands form the JsonServer
    """

    def pep8(self, code, settings=None):
        """Run PEP8 auto format command
        """

        AutoPep8(self.callback, self.uid, self.vid, code, settings)

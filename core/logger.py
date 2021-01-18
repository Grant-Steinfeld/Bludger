#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-#
#       Parasite        #
#-:-:-:-:-:-:-:-:-:-:-:-#

# Author: 0xInfection
# This module requires Parasite
# https://github.com/0xInfection/Parasite

import logging, config
from core.colors import O, R, color

class CustomFormatter(logging.Formatter):
    '''
    Customising my style of logging the results
    '''
    ftl_fmt  = R+" FATAL: %(msg)s"
    info_fmt = O+" %(msg)s"
    err_fmt  = color.RED+"[-] ERROR: "+color.END+"%(msg)s"
    crt_fmt  = color.RED+"[-] CRITICAL: "+color.END+"%(msg)s"
    dbg_fmt  = color.CYAN+"[~] DEBUG: "+color.END+"%(module)s: %(msg)s"

    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(msg)s", datefmt=None, style='%')

    def format(self, record):

        format_orig = self._style._fmt

        if record.levelno == logging.DEBUG:
            self._style._fmt = CustomFormatter.dbg_fmt

        elif record.levelno == logging.INFO:
            self._style._fmt = CustomFormatter.info_fmt

        elif record.levelno == logging.ERROR:
            self._style._fmt = CustomFormatter.err_fmt

        elif record.levelno == logging.CRITICAL:
            self._style._fmt = CustomFormatter.crt_fmt

        elif record.levelno == logging.FATAL:
            self._style._fmt = CustomFormatter.ftl_fmt

        result = logging.Formatter.format(self, record)
        self._style._fmt = format_orig

        return result

def calcLogLevel(args):
    '''
    Calculate logging level based on verbose options
    '''
    baseloglevel = config.DEBUG_LEVEL
    if args.verbose is not None:
        if args.verbose >= 3:
            baseloglevel = 10
        else:
            baseloglevel = 30 - (args.verbose * 10)
    if args.quiet:
        baseloglevel = 50
    return baseloglevel

def pheaders(tup: dict):
    '''
    This module prints out the headers as received
    '''
    #print(GR, 'Receiving headers...\n')
    print(color.GREY,'\n  '+color.UNDERLINE+'RESPONSE HEADERS'+color.END+color.GREY+':'+'\n')
    for key, val in tup.items():
        print('  ',color.CYAN+key+': '+color.ORANGE+val)

def pbody(body: str):
    '''
    Prints out the response body of the request
    '''
    print(color.GREY,'\n  '+color.UNDERLINE+'RESPONSE BODY'+color.END+color.GREY+':'+'\n'+color.END)
    if not body.strip():
        print('Empty body response.\n')
    else:
        print(body, '\n')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Download latest LanguageTool distribution."""
import os

if __name__ == '__main__':
    if not os.name == 'posix':
        raise Exception('This fork is only for Linux')
    if not os.path.exists('/usr/bin/curl'):
        raise Exception('Curl is not installed')
    if not os.path.exists('/usr/bin/unzip'):
        raise Exception('Unzip is not installed')
    os.system("curl https://www.languagetool.org/download/LanguageTool-3.2.zip -o LanguageTool-3.2.zip")
    os.system("unzip LanguageTool-3.2.zip")
    os.system("cp -r LanguageTool-3.2 language_tool")

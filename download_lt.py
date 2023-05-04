#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Download latest LanguageTool distribution."""
import os

def download_lt():
    if not os.name == 'posix':
        raise Exception('This fork is only for Linux')
    if not os.path.exists('/usr/bin/wget'):
        raise Exception('Wget is not installed')
    if not os.path.exists('/usr/bin/unzip'):
        raise Exception('Unzip is not installed')
    if not os.path.exists('LanguageTool-3.2.zip'):
        os.system("wget https://www.languagetool.org/download/LanguageTool-3.2.zip")
    os.system("rm -rf LanguageTool-3.2")
    os.system("unzip LanguageTool-3.2.zip")
    os.system("cp -r LanguageTool-3.2 language_tool")

if __name__ == "__main__":
    download_lt()

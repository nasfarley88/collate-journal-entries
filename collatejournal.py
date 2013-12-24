#!/usr/bin/python

# For naming the journal temporary file
from time import strftime

from subprocess import call
import os
from shutil import copyfile

# filename string, always good to have!
filename = ".journal" + strftime("%FT%H%M%S") 

# Open file ready for writing
f = open(filename+".tex","w+")

beginningOfFile = r"""\documentclass{memoir}

\begin{document}"""

endOfFile = r"""
\end{document}"""

middleOfFile = r"""I don't think the import worked \ldots"""

# TODO import the text files here

f.write(beginningOfFile + middleOfFile + endOfFile)
f.close()

copyfile(filename+".tex","journal.tex")

print "Attempting to run pdflatex on journal.tex"

call(['pdflatex','journal.tex'])

#!/usr/bin/python

# For naming the journal temporary file
from time import strftime
import os

# filename string, always good to have!
filename = "journal" + strftime("%FT%H%M%S") + ".tex"

# Open file ready for writing
f = open(filename,"w+")

beginningOfFile = r"""\documentclass{memoir}

\begin{document}"""

endOfFile = r"""
\end{document}"""

middleOfFile = r"""I don't think the import worked \ldots"""

# TODO import the text files here

f.write(beginningOfFile + middleOfFile + endOfFile)

print "Attempting to run pdflatex"
os.system("pdflatex " + filename)

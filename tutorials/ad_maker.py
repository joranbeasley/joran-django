import os
src_doc = "twisted_chat.asciidoc"
print os.system("asciidoc.py --out-file=test.part.html --no-header-footer %s"%src_doc)
print "OK MADE IT!"
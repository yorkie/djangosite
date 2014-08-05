
# encoding=utf-8

import os

def convert(text, config='t2s'):
  f = os.popen('t2s --config s2t '+text)
  return f.read()

print '>>', convert('我爱你')
print '>>'
'''

Transpiler skeleton. Probably won't be touching this for a good while

'''

import sys

# Local deps
from . import colors
from .sym import Symbol, Symbols
from .atomizer import Atomizer
from .gazellestr import gazellestr
from .gazelleerr import gazelleerr
from .parseval import eval, parse, gazellestr, global_env

def transpile(expr, env):
  pass

def run(files):

  for file in files:

    expression = Atomizer(open(file))

    try:

      code = transpile(parse(expression), global_env)
     
      print(code)

    except Exception as e:
      gazelleerr(e)
      
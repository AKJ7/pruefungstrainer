import pprint
import argparse
try:
    from core.xmlHandler import xmlHandler
except NameError:
    from .core.xmlHandler import xmlHandler


arg_parser = argparse.ArgumentParser('Pruefungstrainer')
arg_parser.add_argument('-a', '--add', help='New question', required=False)
parser = arg_parser.parse_args()


from wiktionaryparser import WiktionaryParser as wp
import pprint

pp = pprint.PrettyPrinter(indent=4)
parser = wp()
result = parser.fetch('fromage')
pp.pprint(result)
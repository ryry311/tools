import sys

def generate_class_code(argv):
   attribs = argv[2:]
   print('class {}:'.format(argv[1]))
   print('\tdef __init__(self, {}):'.format(", ".join(attribs)))
   for arg in attribs:
      print('\t\tself.{} = {}'.format(arg, arg))
   print('\tdef __eq__(self, other):')
   eq_list = []
   for arg in attribs:
      eq_list.append('self.{} == other.{}'.format(arg, arg))
   print('\t\treturn type(self) == type(other) and {}'.format(" and ".join(eq_list)))
   print('\tdef __repr__(self):')
   bracket_list = []
   for i in range(len(attribs)):
      attribs[i] = "self."+attribs[i]
      bracket_list.append('{}')
   print("\t\treturn '{}({})'.format({})".format(argv[1], ", ".join(bracket_list), ", ".join(attribs)))

if __name__ == '__main__':
   generate_class_code(sys.argv)

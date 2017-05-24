#python3 convert.py 100 ft to m
# -d distance, -t time, -m mass

from sys import argv

def main():

   conversion_type = argv[1]
   constant = float(argv[2])
   start_unit = argv[3]
   end_unit = argv[5]

   conversion_dictionary = {'-d': {'mm':0.001, 'cm':0.01, 'm':1, 'km':1000, 'in':0.0254, 'ft':0.3048, 'yd':0.9144, 'mi':1609.344},
                            '-t': {'ms':0.001, 's':1, 'min':60, 'hrs':3600, 'days':86400, 'weeks':604800, 'months':2592000, 'years':31536000, 'decades':315360000, 'centuries':3153600000, 'millennia':31536000000},
                            '-m': {'mg':0.000001, 'g':0.001, 'kg':1, 'oz':0.028349523125, 'lbs':0.45359237}}

   constant_in_si = constant * conversion_dictionary[conversion_type][start_unit]
   final_constant = constant_in_si / conversion_dictionary[conversion_type][end_unit]

   print("{:.2f} {}".format(final_constant, end_unit))

if __name__ == '__main__':
   main()

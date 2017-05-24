def main():
   num_categories = int(input("\nHow many grade non-final categories does the class have? "))
   weights = []
   grades = []

   for category_index in range(0, num_categories):
      weights.append(float(input("Enter category {} weight: ".format(category_index+1))))
      grades.append(weights[category_index] * float(input("Enter category {} grade: ".format(category_index+1))))

   target = float(input("What grade do you want in the class? "))

   grade_needed = (target - .01* sum(grades)) / (100 - sum(weights))
   print("\nYou need a {:.2f}% to get a {:.2f}% in the class.\n".format(grade_needed*100, target))

if __name__ == '__main__':
   main()

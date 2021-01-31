import matplotlib.pyplot as plt
import numpy as np
import person

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))

my_list = [len(n) for n in list_of_names]
for x in range(len(list_of_names)):
  print(my_list)

people = {}
for x in range(len(list_of_names)):
  people[list_of_names[x]] = person.person(
    name = list_of_names[x],
    age = list_of_ages[x],
    height = list_of_heights_cm[x]
  )

array_ages = np.array(list_of_ages)
array_heights = np.array(list_of_heights_cm)

mean_ages = np.mean(array_ages)
print(f"Average age: {mean_ages}")

mean_height = np.mean(array_heights)
print(f"Average height: {mean_height}")

plt.scatter(array_ages, array_heights)
plt.title('Average Age vs Height')
plt.xlabel('Age')
plt.ylabel('Height')
plt.savefig('hw1.png')
plt.show()



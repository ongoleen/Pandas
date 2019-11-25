import pandas as pd
cars = pd.read_csv('cars.csv')
x = cars.loc[[0,1,2,3,4], ::2]
y = cars[cars['Model']=='Mazda RX4']
z = cars.loc[cars['Model']=='Camaro Z28', 'cyl']
a1 = cars.loc[(cars['Model']=='Mazda RX4 Wag'), ('Model', 'cyl', 'gear')]
a2 = cars.loc[(cars['Model']=='Honda Civic'), ('Model', 'cyl', 'gear')]
a3 = cars.loc[(cars['Model']=='Ford Pantera L'), ('Model', 'cyl', 'gear')]
print(x, '\n')
print(y, '\n')
print('No. of cylinders of Camaro Z28:\n', z, '\n')
print('Cylinders and gears:')
print(pd.concat([a1,a2,a3]))
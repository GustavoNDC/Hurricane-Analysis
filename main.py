# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_list (list):
  updated_damages = []
  for value in list:
    x = ''
    if value not in 'Damages not recorded':
      for i in value:
        if i in conversion:
          x = value.replace(i, '')
          updated_damages.append(float(x)*conversion[i])
    else:
      updated_damages.append(value)
  return updated_damages
      


# test function by updating damages
updated_damages = update_list (damages)
#print(updated_damages, '\n')

# 2 
# Create a Table

def hurricanes_func (names, months, years,max_sustained_winds, areas_affected, damages, deaths):
  hurricanes = {}
  for i in range(34):
    hurricanes[i] = {"Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": damages[i],
      "Deaths":deaths[i]}

  return hurricanes

# Create and view the hurricanes dictionary

hurricanes = hurricanes_func (names, months, years,max_sustained_winds, areas_affected, updated_damages, deaths)

##print(hurricanes)

# 3
# Organizing by Year

def hurricanes_updatedd(hurricanes):
  hurricanes_update = {}
  for i in hurricanes:
    hurricanes_update[years[i]]=hurricanes[i]
  return (hurricanes_update)



# create a new dictionary of hurricanes with year and key
hurricanes_update = {}
hurricanes_update = hurricanes_updatedd(hurricanes)
#print(hurricanes_update)
for i in hurricanes_update:
  print(i)
  print(hurricanes_update[i], '\n')

# 4
# Counting Damaged Areas

def area_counter(hurricanes_update):
  cont = {}
  values = []
  for i in hurricanes_update:
    areas = (list(hurricanes_update[i].values())[4])
    for area in areas:
      if cont.get(area):
        cont[area] += 1
      else:
        cont[area] = 1
  return cont

# create dictionary of areas to store the number of hurricanes involved in
cont = {}
cont = area_counter(hurricanes_update)
for key,value in cont.items():
  print(key, value)


# 5 
# Calculating Maximum Hurricane Count

def find_area(cont):
  control = 0
  for key, value in cont.items():
    if control <value:
      control = value
    return (key,value)

# find most frequently affected area and the number of hurricanes involved in
area_most_affected = {}
area_most_affected = find_area(cont)
print('Area most affected:', area_most_affected, '\n')

# 6
# Calculating the Deadliest Hurricane
def deadlyest_hurricane(deaths):
  control = 0
  for i in deaths:
    if i > control:
      control = i
  index = deaths.index(control)
  return print('Hurricane: {} \n Deaths: {}'.format(names[index], control))

# find highest mortality hurricane and the number of deaths

deadlyest_hurricane(deaths)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def hurricanes_by_scale (deaths, mortality_scales, mortality_scale):
  hurricane_by_scale = {0:[], 1:[], 2:[], 3:[], 4:[]}
  for death in deaths:
    for key,value in mortality_scales.items():
      if death != 'Damages not recorded' and death < value:
        index = deaths.index(death)
        hurricane_by_scale[key-1].append(names[index])
        break
      elif death != 'Damages not recorded' and death >= mortality_scales[4]:
        index = deaths.index(death)
        hurricane_by_scale[4].append(names[index])
        break
  return hurricane_by_scale
      


# categorize hurricanes in new dictionary with mortality severity as key
hurricane_by_scale = {}
hurricane_by_scale = hurricanes_by_scale(deaths, mortality_scale, mortality_scale)

for key,value in hurricane_by_scale.items():
  print (key, value)

# 8 Calculating Hurricane Maximum Damage
def cost_hurricane(damages, names):
  control = 0.0
  for i in damages:
    if i != "Damages not recorded": 
      if float(i) > control:
        control = float(i)
  return names[damages.index(control)], control

# find highest damage inducing hurricane and its total cost
namess, damagess = cost_hurricane(updated_damages,names)
print('furicão de deu mais dano:',namess,'custando:', damagess,'dinheiros')
# 9
# Rating Hurricanes by Damage

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
updated_damages2 = []
for i in updated_damages:
  if i != 'Damages not recorded':
    updated_damages2.append(int(i))
  else:
    updated_damages2.append(i)

print(hurricanes_by_scale (updated_damages2, damage_scale, mortality_scale))
# categorize hurricanes in new dictionary with damage severity as key

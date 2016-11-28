import pandas as pd
import numpy as np
import pandas.util.testing as tm


CRIME = pd.read_csv("CRIME.csv")
INCOME = pd.read_csv("INCOME.csv")
SUICIDE = pd.read_csv("SUICIDE.csv")
DEATH = pd.read_csv("DEATH.csv")
POPULATION = pd.read_csv("POPULATION.csv")
BLACK_NONHISPANIC = pd.read_csv("BLACK_NONHISPANIC.csv")
HISPANIC = pd.read_csv("HISPANIC.csv")
OTHER_NONHISPANIC = pd.read_csv("OTHER_NONHISPANIC.csv")
WHITE_NONHISPANIC = pd.read_csv("WHITE_NONHISPANIC.csv")
POPULATION_MALE = pd.read_csv("POPULATION_MALE.csv")
POPULATION_FEMALE = pd.read_csv("POPULATION_FEMALE.csv")



# 1. PREPARING DATABASES (cleaning)
### A. INCOME
#### keeping three columns of income
INCOME1 = INCOME[['Tax Year','Place of Residence', 'Average NY AGI of All Returns']]
INCOME1.columns = ['Year', 'County', 'Average NY AGI']
INCOME2 = INCOME1.replace('New York City - Kings', 'Kings')
INCOME3 = INCOME2.replace('New York City - Bronx', 'Bronx')
INCOME4 = INCOME3.replace('New York City - Manhattan', 'Manhattan')
INCOME5 = INCOME4.replace('New York City - Queens', 'Queens')
INCOME6 = INCOME5.replace('New York City - Richmond', 'Richmond')
INCOME7 = INCOME6.replace('Total, New York City', 'New York City')


### B. SUICIDE
#### suicide by county
SUICIDE_COUNTY = SUICIDE[SUICIDE['Category']=="County_Group"]
SUICIDE_COUNTY_1 = SUICIDE_COUNTY[['Year', 'Value', 'Suicide Deaths', 'Population', 'Rate Per 100,000']]
SUICIDE_COUNTY_1.columns = ['Year', 'County', 'Suicide Deaths','Population', 'Suicide Rate Per 100,000']
#### suicide by sex
SUICIDE_SEX=SUICIDE[SUICIDE['Category']=='Gender_Group']
#### suicide by age_group
SUICIDE_AGE=SUICIDE[SUICIDE['Category']=='Age_Group']
#### suicide by race
SUICIDE_RACE = SUICIDE[SUICIDE['Category']=='Race_Ethnicity_Group']


### C. DEATH
#### KEEPING TOTAL NUMBER OF DEATHS TO COMPARE WITH SUICIDE
DEATH_TOTAL = DEATH[DEATH['Selected Cause of Death']=='Total']
DEATH_TOTAL_1 = DEATH_TOTAL[['Year', 'County Name', 'Deaths', 'Crude Rate', 'Adjusted Rate']]
DEATH_TOTAL_1.columns = ['Year', 'County', 'Deaths', 'Crude Rate', 'Adjusted Rate']


### D. POPULATION
#### INTERESTED IN RACE
POPULATION1 = POPULATION[POPULATION['Age Group Description']=='Total']
POPULATION2 = POPULATION1[POPULATION1['Gender Description']=='Total']
POPULATION3 = POPULATION2[POPULATION2['Race/Ethnicity Description']=='Total']
POPULATION4 = POPULATION3[['Year', 'County', 'Population Total']]

BLACK_NONHISPANIC1 = BLACK_NONHISPANIC[['Year', 'County', 'Population Black Non Hispanic']]
HISPANIC1 = HISPANIC[['Year', 'County', 'Population Hispanic']]
OTHER_NONHISPANIC1 = OTHER_NONHISPANIC[['Year', 'County', 'Population Other Non Hispanic']]
WHITE_NONHISPANIC1 = WHITE_NONHISPANIC[['Year', 'County', 'Population White Non Hispanic']]

### INTERESTED IN GENDER
POPULATION_MALE1 = POPULATION_MALE[['Year', 'County', 'Population Male']]
POPULATION_FEMALE1 = POPULATION_FEMALE[['Year', 'County', 'Population Female']]


### E. CRIME
CRIME1 = CRIME[['County', 'Agency', 'Year', 'Index Total', 'Violent Total']]
CRIME2 = CRIME1[CRIME1['Agency']=='County Total']
CRIME3 = CRIME2[['County', 'Year', 'Index Total', 'Violent Total']]
CRIME3.columns = ['County', 'Year', 'Crime Total', 'Violent Crime Total']

# 2. MERGING

### RACES POPULATION
POPULATION_RACE = pd.merge(POPULATION4, BLACK_NONHISPANIC1, on=['Year', 'County'])
POP_RACE1 = pd.merge(POPULATION_RACE, HISPANIC1, on=['Year', 'County'])
POP_RACE2 = pd.merge(POP_RACE1, OTHER_NONHISPANIC1, on=['Year', 'County'])
POP_RACE3 = pd.merge(POP_RACE2, WHITE_NONHISPANIC1, on=['Year', 'County'])

### GENDER POPULATION
GENDER_POPULATION = pd.merge(POPULATION_MALE1, POPULATION_FEMALE1, on=['Year', 'County'])
POP = pd.merge(POP_RACE3, GENDER_POPULATION, on=['Year', 'County'])

### A. INCOME WITH CRIME
INC_CRIME = pd.merge(INCOME7, CRIME3, on=['Year', 'County'])

### B. INC_CRIME WITH DEATH
INC_CRIME_DEATH = pd.merge(INC_CRIME, DEATH_TOTAL_1, on=['Year', 'County'])

### C. INC_CRIME_DEATH WITH SUICIDE BY COUNTY
INC_CRIME_DEATH_SUICIDE = pd.merge(INC_CRIME_DEATH, SUICIDE_COUNTY_1, on =['Year', 'County'])

### D. INC_CRIME_DEATH_SUICIDE WITH POPULATION
MASTER1 = pd.merge(INC_CRIME_DEATH_SUICIDE, POP, on=['Year', 'County'])
MASTER1.to_csv('MASTER1.csv', sep='\,')

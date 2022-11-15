import json
from datetime import date


def ask_user():
    while True:
            try: 
                user_input = input('Select the number of the meal you wish to add to the list or \'end\'')
                if user_input == 'end':
                    return user_input
                else:
                    assert 0<int(user_input)<len(lista_comida)
                    return user_input
            except (ValueError, AssertionError): 
                print(user_input + ' is not a valid option')              
        
    

#Defines season to recomend meals with seasonal vegetables
today = date.today()  
month = today.strftime('%B')
season = ''
summer = ['December','January','February']
autum = ['March','April','May']
winter = ['June', 'July', 'August']

if month in summer:
    season = 'Summer'
elif month in autum:
    season = 'Autum'
elif month in winter:
    season = 'Winter'
else:
    season = 'Spring'

print(month, 'is', season)

with open('seasonal.json') as j: #seasonal.json file has dictionary ={Season:[vegetables&fruits]}. 
    jobj = json.load(j)
    
estacion = jobj[season]

print(estacion)

recomended=[]
lista_comida=[]

with open('meals.json') as f: #meals.json file has a dictionary={'name':'meal','ingredients':[{'name':'ingredient','amount':'xxx'}];}
    all_meals = json.load(f)

#Enumerate meal with index so number can be choose
i=0
lenght=len(estacion)

for index, meal in enumerate(all_meals):
    index_meal = all_meals.index(meal)
    for  i in range(lenght):                #Compares name of meal and seasonal vegetable list. If vegetable included in list--> name is written in upper
        vegie=estacion[i]
        if meal['name'].find(vegie)!=-1:
            meal['name']= meal['name'].upper()
            i+=1
        else:
            i+=1
    lista_comida.append(meal['name'])
    print(index,'-', meal['name'])
    


list_select_meals = []

list_name_meals = []
meal_count=0

#ask user to select meals and stores them in list
select_meal = ask_user()

#Exception Handling for user input. ValueError if not type a number/IndexError if number out of range

while select_meal!='end':
    indx_select_meal=int(float(select_meal))
    list_select_meals.append(all_meals[indx_select_meal])
    print('>',all_meals[indx_select_meal]['name'],'\n')
    list_name_meals.append(all_meals[indx_select_meal]['name'])
    meal_count+=1
    print(meal_count)
    select_meal=ask_user()
  

to_buy = {}

#Counts selected meal's ingredients
for meal in list_select_meals:
    indx= all_meals.index(meal)
    select_meal = all_meals[indx]

    ingredients = select_meal['ingredients']

    for ingredient in ingredients:

        name_ingredient = ingredient['name']
        amount_ingredient = ingredient['amount']

        if name_ingredient in to_buy:
            to_buy[name_ingredient] += amount_ingredient
        else:
            to_buy[name_ingredient] = amount_ingredient


print('\n MEALS:')
for name in list_name_meals:
        print('>',name)
        
print('\n GROCERY LIST:')
for ingredient in to_buy:
    print(ingredient, to_buy[ingredient])
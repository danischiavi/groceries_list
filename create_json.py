import json

data= {
  'Winter': ['aceitunas', ' acelga', ' achicoria', ' apio', ' batata', ' berro', ' brocoli', ' cardo', ' coliflor', ' cebolla de verdeo', ' chaucha', ' escarola', ' espinaca', ' hinojo', ' nabo', ' nabiza', ' puerro', ' rabano', ' radicheta', ' remolacha', ' repollo', ' repollitos de Bruselas', ' zanahoria', ' zapallo', ' calabaza', ' banana', ' ciruela', ' durazno', ' limón', ' mandarina', ' melón', ' membrillo', ' naranja', ' palta', ' pelón', ' pera', ' pomelo'],
  'Spring':['remolacha', ' zapallito', ' radicha', ' perejil', ' puerro', ' habas', ' lechuga', ' nabiza', ' nabo', ' acelga', ' apio', ' alcaucil', ' espárrago', ' frutilla', ' frambuesa', ' cereza', ' arándano', ' manzana', ' naranja', ' palta', ' ananá', ' banana', ' frutilla', ' limón'],
  'Summer':['zapallo', ' calabaza', ' rabanito', ' tomate', ' espárrago', ' morron', ' cebolla', ' chauchas', ' pepino', ' acelga', ' berenjena', ' choclo', ' frambuesa', ' mora', ' manzana', ' sandia', ' uva', ' limon', ' pelon', ' pera', ' arandanos', ' frutilla', ' higo', ' melon', ' naranja', ' anana', ' ciruela', ' cereza', ' damasco', ' durazno'],
  'Autum':['aceitunas', ' acelga', ' achicoria', ' apio', ' batata', ' berro', ' brocoli', ' cardo', ' coliflor', ' cebolla de verdeo', ' chaucha', ' escarola', ' espinaca', ' hinojo', ' nabo', ' nabiza', ' puerro', ' rabano', ' radicheta', ' remolacha', ' repollo', ' repollitos de Bruselas', ' zanahoria', ' zapallo', ' calabaza', ' banana', ' ciruela', ' durazno', ' limón', ' mandarina', ' melón', ' membrillo', ' naranja', ' palta', ' pelón', ' pera', ' pomelo']
}

#for season in data:
#    index_=data[season].index('cabbage')
#   data[season][index_]='repollo'    

 

with open("seasonal.json", "w") as write_file:
    json.dump(data, write_file)

    

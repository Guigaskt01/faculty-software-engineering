import pprint

gamesDict = {
    'Resident evil 4':{
        'yearlaunch':2023,
        'classification':9.8,
        'genre':['ação','aventura']
    },
    'Mario Odyssey':{
        'yearlaunch':2017,
        'classification':10.0,
        'genre':['aventura','3d']
    },
    'Donkey Kong Country':{
        'yearlaunch':1995,
        'classification':9.5,
        'genre':['aventura','plataforma']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

#1- Buscar informação dentro de um dicionário aninhado
print(gamesDict['Resident evil 4']['genre'])

#2- Adicionar novo item
gamesDict['Mario Odyssey']['players']=1
print(gamesDict['Mario Odyssey'])

#3- Excluir um dicionário
del gamesDict['Resident evil 4']
pp.pprint(gamesDict)
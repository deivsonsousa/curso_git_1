"""
#Forma 1
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

#Forma 2
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ita', 'Não encontrado')

print(paises['br'])
print(paises['eua'])
print(paises['py'])
print(paises.get('br'))
print(f'Encontrei o pais {pais}')




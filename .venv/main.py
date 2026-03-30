from lista_livors import biblioteca

filto_livros = [ p for p in biblioteca if ['titulo'] = 'Harry Potter e a Pedra Filosofal']
print(filto_livros)

filto_livros = [ p for p in biblioteca if ['autor'] = 'Harper Lee']
print(filto_livros)

filto_livros = [ p for p in biblioteca if ['ano'] = '1881']
print(filto_livros)

filto_livros = [ p for p in biblioteca if ['categoria'] = 'Ficção Absurda']
print(filto_livros)
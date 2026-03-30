from main import filto_livros

filto_livros_1 = {"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "ano": 1997, "categoria": "Fantasia"}
filto_livros_2 = {"titulo": "O Sol é para Todos", "autor": "Harper Lee", "ano": 1960, "categoria": "Clássico"}
filto_livros_3 = {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "ano": 1881, "categoria": "Realismo"}
filto_livros_4 = {"titulo": "A Metamorfose", "autor": "Franz Kafka", "ano": 1915, "categoria": "Ficção Absurda"}

Lista_Livros_1 = filto_livros(filto_livros_1)
print(Lista_Livros_1)

Lista_Livros_2 = filto_livros(filto_livros_2)
print(Lista_Livros_2)

Lista_Livros_3 = filto_livros(filto_livros_3)
print(Lista_Livros_3)

Lista_Livros_4 = filto_livros(filto_livros_4)
print(Lista_Livros_4)
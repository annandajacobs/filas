'''
9. Qual a avaliação de desempenho do método rodar() ? É possível assegurar a implementação desse método rodar seja O(1)? mais
eficiente do que a chamada separada para f.enqueue(f.dequeue) .


Avaliação de Desempenho do rodar(): 
O(1) — o método é eficiente e realiza apenas operações de custo constante.

Comparação: A implementação do método rodar() é equivalente em termos de desempenho a chamar f.enqueue(f.dequeue), pois ambas as operações têm complexidade O(1). Portanto, o método rodar() não é necessariamente mais eficiente em termos de complexidade, mas pode ser considerado mais legível e semânticamente mais claro.
'''
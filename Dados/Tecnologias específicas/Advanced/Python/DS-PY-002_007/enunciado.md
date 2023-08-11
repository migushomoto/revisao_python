Uma empresa está criando um sistema para transportar `Objeto`s em `Caixas`. 
A ideia é criar uma `Caixa` com a quantidade máxima de `Objeto`s definida no 
momento da criação do objeto (com o parametro `qtd_max_objetos`) e, 
posteriormente, adicionar cada `Objeto` através
do método `adicionar_objeto`.

Caso tente adicionar um novo `Objeto` na `Caixa` e esta já estiver cheia, 
deve retornar `False`, caso contrário retornar `True`.

Uma vez que a `Caixa` é criada, deve ser possivel receber uma listagem simples, 
em texto, com o nome de todos os itens armazenados, em ordem alfabética, 
um por linha, usando o método `listar_itens`.

A classe `Objeto` tem os campos `nome` e `tipo`, e a classe `Caixa` tem o 
campo `qtd_max_objetos`.
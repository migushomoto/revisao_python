A empresa de venda de roupas em que você trabalha precisa de um jeito simples de alterar o 
preço de todas as roupas, de acordo com um valor de desconto fixo. 

A ideia é ter um objeto `Loja` com o campo `itens_a_venda` que retorna uma lista de **todos** os itens
à venda na loja. Os itens podem ser do tipo `Camiseta`, `Camisa`, `Calca`, sendo que todos os
itens tem o campo `tamanho`, mas `Camiseta` tem `cor`, enquanto `Camisa` tem `tamanho_manga` e 
`estilo`, e `Calca` tem `cor` e `modelo`. Para adicionar um item à loja, usamos o método 
`adicionar_item`. 

Todos os tipos de itens tem o metodo `obter_preco`, que retorna o preço da peça; para definir o 
preço, vamos usar o método `definir_preco`.

No objeto `Loja` temos o método `aplicar_desconto` que recebe um valor e aplica essa porcentagem de 
desconto a todos os produtos da loja.
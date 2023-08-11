Para ajudar a lojinha do seu tio, voce vai criar uma classe que 
simula um caixa de registro de produtos.

A classe principal, `CaixaRegistradora`, deve ter um método `iniciar_venda`
que cria uma nova `Venda`. Com essa venda, usando o método 
`registrar_produto`, você vai registrar um produto com o `nome`, 
o `valor_unitario` e a quantidade desse produto (`qtd_produtos`). 

Ao final da venda, você roda o método `listar_produtos`, que gera 
uma tupla de tuplas com quatro campos:

- nome do produto 
- valor unitario
- quantidade comprada
- valor total do produto

E rodando o método `obter_valor_total`, a resposta é o valor total 
da venda. E depois, rodando o método `finalizar_venda`, o valor
recebido é adicionado à `CaixaRegistradora` pelo método 
`adicionar_pagamento`. 

Finalmente, após todas as vendas, podemos usar o método 
`obter_saldo_atual` na `CaixaRegistradora` para obter o saldo total
até o momento.
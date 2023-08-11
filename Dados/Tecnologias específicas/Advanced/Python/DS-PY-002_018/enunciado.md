Estamos criando um sistema de registro de produtos, e para cada `Produto` temos os seguintes 
campos e regras de preenchimento:

- Nome do produto (`nome_produto`): Entre 5 e 30 caracteres
- Data do Lançamento (`dt_lancamento`): Deve ser um `datetime` do python
- Descricao (`descricao`): Entre 5 e 200 caracteres
- Atualmente em venda (`em_venda`): Campo `bool` baseado no valor de `dt_lancamento`; caso o campo `dt_lancamento` 
seja posterior a hoje, `em_venda` retorna `False`, ao contrário retorna `True`

O 3 primeiros campos devem ser informados e validados no momento da criação do objeto, usando os getters e setters 
do python. Em caso de problema na validacao de algum dos campos, retornar uma exceção `ValueError`.


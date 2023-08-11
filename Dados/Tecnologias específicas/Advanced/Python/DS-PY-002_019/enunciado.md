Uma empresa de veículos está registrando diferentes tipos de veículos para aluguel e venda, e pediu sua ajuda
para criar um código que os ajude com este trabalho. Após conversar com outras pessoas do time de engenharia
de solução, a ideia selecionada para implementação foi a seguinte:

Criar a função `registrar_veiculo`, que recebe 4 parametros: `qtd_passageiros`; `tipo_negociacao` que
deve receber um dos dois valores: `aluguel` ou `venda`; `condicao`, que deve receber um dos dois valores, 
`novo` ou `usado`; e `placa` com exatos 8 caracteres. Todos os campos devem ser validados no momento da criação 
do objeto, e em qualquer dado incorreto deve retornar uma exceção `ValueError`. A função retorna o objeto criado 
relativo ao veículo. 

Se o veículo registrado for de mais de 5 passageiros, deve criar um objeto `Onibus`, do contrário deve criar um
objeto `Carro`. Ambos devem herdar comportamentos e campos do objeto `Veiculo`.


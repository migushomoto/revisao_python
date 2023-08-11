Uma empresa está começando a criar um cadastro de pessoas que trabalham na empresa, e quer dividir essas pessoas em categorias: `PessoaMensalista`, `PessoaHorista` e `PessoaSemApontamento`. A pessoa mensalista tem um salário fixo por mês, dependendo da quantidade de horas trabalhadas; a pessoa horista recebe por hora trabalhada e a pessoa sem apontamento recebe um salario mensal independente de horas trabalhadas.

Codifique uma estrutura de classes onde a pessoa tem nome e idade, a pessoa mensalista tem `total_horas_trabalhadas` e ` valor_salario`, pessoa horista tem `total_horas_trabalhadas` e `valor_hora`, e pessoa sem apontamento tem `valor_salario`.

As três classes devem ter o método `calcular_salario`, de acordo com as regras:

- Se pessoa mensalista, o valor de salario é proporcional ao numero de horas trabalhadas até 160 horas. Se trabalhou mais de 160, o valor é o teto (ou seja, o valor do salário),
- se pessoa horista, multiplicar o total de horas pelo valor por hora, e
- se pessoa sem apontamento, mostrar o salário como informado.

O retorno do método `calcular_salario` deve ser: 

"A pessoa de nome {nome} tem a receber R$ {salario}"
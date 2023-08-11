Para o cadastro de um cliente (objeto `Cliente`), precisamos dos 
seguintes dados:

- nome_completo
- data_de_nascimento (dd/mm/aaaa)

No momento da criacao do cliente não devemos informar nenhum dado. Posteriormente, ao efetuar o cadastro, devem ser validados os campos
da seguinte forma:

- nome_completo deve ter pelo menos um espaço entre o nome e o sobrenome. No caso de mais de um espaço, tratar  o que vem antes do primeiro espaço como nome e o resto como sobrenome. 
- data_de_nascimento deve ser anterior a hoje

Qualquer erro no processo deve retornar uma exceção `ValueError`

Os seguintes valores devem ser entregues como campo, e não como método

- idade_em_anos: calculada a partir da data_de_nascimento
- nome: mostrar apenas o primeiro nome. 

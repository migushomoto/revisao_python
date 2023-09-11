# Diretrizes para produção de exercícios fechados
 
Como todos sabem, temos a iniciativa de melhorar a vida do instrutor e a escalabilidade de nosso modelo educacional, passando uma carga grande das atividades dos alunos para uma forma assíncrona e autocorrigida. Assim, nossos instrutores podem focar seus esforços na correção de projetos, que nos dão uma visão qualitativa do aluno e são aderentes à metodologia PBL (Problem/Project Based Learning), que usamos.
 
Os exercícios para os sistemas da Ada podem ser feitos em 3 categorias: (a) Múltipla escolha, (b) Verdadeiro ou Falso, (c) Lacunas.
 
Cada formato de exercício tem um arquivo JSON com um formato específico. Esse arquivo nos permitirá subir os exercícios em qualquer sistema da Ada posteriormente.
 
**É muito importante seguir à risca o formato do arquivo e as diretrizes de qualidade para que seus exercícios sejam aceitos na entrega e não haja retrabalho!**
 
# **Diretrizes Normativas:**
 
 ****
 
1. O exercício deve conter as tags referentes aos conceitos a que se destina.
 
2. O exercício deve passar por peer-review de ao menos um outro instrutor do curso.
 
3. O SKU reflete a numeração do exercício e deve ser composto por 6 dígitos no formato apropriado. Como exemplo:
 
> *000001.json* | **000001** indica o número do exercício | **.json** = formato do arquivo

*Para manter a coerência e a sequência adequada dos números dos exercícios, a pessoa conteudista deverá dar continuidade à numeração dos exercícios seguindo as orientações fornecidas pela pessoa responsável da equipe educacional que acompanhará o processo de produção.*
 
4. Os exercícios devem ser entregues pelo github, no repositório que será enviado pela pessoa responsável do time educacional que irá acompanhar suas produções.
 
5. Os exercícios devem ser feitos de acordo com as orientações da pessoa responsável do time educacional e da pessoa coordenadora de área.
 
6. Deve ser criado um arquivo JSON para cada exercício produzido.
 
7. Os tipos de exercícios e o formato deles estão descritos neste arquivo. Cada tipo de exercício contém suas Diretrizes Técnicas.

8. **Cada exercício deve conter, obrigatoriamente, o arquivo com a solução. Veja [este exemplo](https://github.com/educacionalAda/BE-JV-Backend-Java/tree/main/BE-JV-001%20L%C3%B3gica%20de%20Programa%C3%A7%C3%A3o%20I/Exerc%C3%ADcios/BE-JV-001-01) caso tenha dúvidas.**
 
# **Diretrizes Qualitativas:**
 
 ****
 
**1. Contextualize brevemente o exercício**
 
Sempre que possível, opte por fazer uma ou duas linhas de introdução antes da proposta do exercício. Essa linha deve contextualizar o exercício com relação ao seu uso prático.
 
Por exemplo:
 
> Receba 3 números, calcule a média e mostre na tela.
>
 
Poderia ser reescrita como:
 
> Os alunos de um curso estão com dificuldades para calcular suas médias, faça um programa que receba as três notas deles, usando 20%, 30% e 50% como pesos, calcule e mostre na tela a média ponderada.
>
 
**2. Tenha precisão no enunciado**
 
O enunciado deve ser claro, direto e preciso, não dando margem à múltiplas interpretações do que deve ser feito na questão.
 
**3. Evite questões meramente matemáticas**
 
Diferentemente da maioria dos instrutores, nossos alunos nem sempre vem de um background de exatas e podem não ter contato constante com matemática em seus cotidianos.
 
Procure evitar questões que sejam exclusivamente matemáticas (ex. Calcule o 30o termo da progressão geométrica de razão 3 começada em 100).
 
**4. Quando utilizar conceitos matemáticos ofereça as fórmulas.**
 
Por exemplo, a questão:
 
> Solicite os valores de a, b e c e imprima na tela se a função tem duas raízes reais, uma ou nenhuma.
>
 
Poderia ser reescrita como:
 
> O delta de Bhaskara pode ser usado para saber se uma função tem raízes reais ou não. Solicite ao usuário o valor de a, b e c (inteiros) e mostre na tela se a função de tem duas raízes reais [delta>0], uma raiz real [delta=0], ou nenhuma [delta<0]. Sendo delta = b² – 4.a.c.
>
 
Queremos avaliar a capacidade de tradução de aritmética para linguagem de programação e o uso de condicionais, não o conhecimento sobre Bhaskara. Portanto, todas as informações sobre o cálculo são providas.
 
**5. Evite questões de múltipla escolha negativas**
 
As questões de múltipla escolha devem avaliar positivamente e não negativamente, sendo assim evite questões cujo enunciado diga, por exemplo, “qual das alternativas não satisfaz…”, “qual das afirmações é incorreta”. Isso é confuso para o aluno.
 
**6. Evite pegadinhas**
 
Não estamos tentando filtrar nossos alunos, e sim avaliar sua compreensão de um conceito. Evite pegadinhas e alternativas propositalmente confusas. Quando as alternativas tiverem apenas um caractere de diferença (ex. < e ≤) procure fazer o texto o menor possível para que a diferença fique óbvia.
 
**7. Evite alternativas de múltipla escolha do tipo catchAll**
 
Alternativas como “todas as anteriores”, “nenhuma das anteriores”, “NDA” ou qualquer coisa nesse sentido devem ser evitadas.
 
**8. Antes de escrever a questão, enumere os conceitos que espera trabalhar com ela.**
 
Tenha em mente o conceito que deseja trabalhar antes de fazer uma questão. Ao terminar, veja se a questão de fato trabalha o que você esperava.
 
# Múltipla escolha
 
### **Diretrizes Técnicas:**
 
O exercício deve ser apresentado no formato JSON seguindo a seguinte estrutura:
 
 ****
 
```json
{
    "id": string,
    "SKU": "string",
    "interpreter": number,
    "type": "string",
    "language": "string",
    "knowledgeArea": "string",
    "category": "string",
    "subCategory": "string",
    "level": "string", 
    "tagsOrConcepts": "string[]",
    "text": "string[]",
    "alternatives": [ { "id": string, "text" : string[], "feedback": string, "correct": boolean} ]
}
```

**id**: UUID único de identificação da questão
 
**SKU:** número do exercício
 
**interpreter** : deve ser sempre 1
 
**type**: deve ser sempre “MULT”
 
**language**: nome da linguagem (”java | csharp | javascript | typescript | python | kotlin | clojure”)

**knowledgeArea:** área da conhecimento ("Front-End	| Back-End |	Banco de Dados	| DevOps	| Dados")

**category:** categoria à qual o conteúdo pertence (Ex: "Lógica de programação", isso indica que o exercício aborda algum conceito de lógica de programação)

**subCategory:** especifica a subcategoria do conteúdo (Ex: "Variáveis", isso indica que o texto focará em conceitos e práticas relacionadas ao uso de variáveis na programação)

**level**: dificuldade da questão (”Basic | Medium | Advanced )
 
**tagsOrConcepts**: lista de conceitos trabalhados (deve vir dos conceitos listados no planejamento do módulo)
 
**text**: enunciado da questão, optamos por usar uma lista de linhas. Podemos adicionar imagens ao enunciado também, veja no exemplo abaixo. Caso deseje adicionar código, use formatação markdown. Atenção para adicionar uma linha em branco antes de iniciar e após encerrar o bloco de código "```"
 
**alternativas**: devem ser sempre uma lista de 4 objetos

**id**: UUID único de identificação da alternativa
 
**text**: texto da alternativa, optamos por usar uma lista de linhas. Caso deseje adicionar código, use formatação markdown. Atenção para adicionar uma linha em branco antes de iniciar e após encerrar o bloco de código "```"
 
**feedback**: o que o aluno verá se escolher essa alternativa, deve conter um feedback claro do porquê essa alternativa é a certa ou porque é a errada
 
**correct**: Determina a alternativa correta. Apenas uma alternativa deve ter o valor *true*, todas as demais devem ser *false*
 
### **Exemplo:**
 
```json
{
    "id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd",
    "SKU": "000001",
    "interpreter": 1,
    "type": "MULT",
    "language": "javascript",
    "knowledgeArea": "Back-End",
    "category": "Lógica de programação",
    "subCategory": "variáveis",
    "level": "Basic", 
    "tagsOrConcepts":["variáveis", "constantes"],
    "text": [
        "Qual o comando correto para criar uma variável com hoisting? !(link da imagem)"
    ],
    "alternatives": [
        { "id": "cceff8d2-8a48-418a-a9f1-de4308f00800", "text": ["var"], "feedback":"var é a única forma de declaração que permite hoisting", "correct":true },
        { "id": "7f1dce81-6c4d-4a5f-97d9-ff57b173d02e", "text": ["let"], "feedback":"let tem escopo fechado e não faz hoisting", "correct":false },
        { "id": "d0901f9d-cc1f-45e1-9b4c-2de7dae96633", "text": ["const"], "feedback":"const tem escopo fechado e não faz hoisting", "correct":false },
        { "id": "a9ea725b-c7a3-463d-b50b-8b8defe445cc", "text": ["def"], "feedback":"def não existe no JS", "correct":false }
    ]
}
```
 
# Verdadeiro ou Falso
 
### **Diretrizes Técnicas:**
 
O exercício deve ser apresentado no formato JSON seguindo a seguinte estrutura:
 
```json
{
    "id": string,
    "SKU": "string",
    "interpreter": number,
    "type": "string",
    "language": "string",
    "knowledgeArea": "string",
    "category": "string",
    "subCategory": "string",
    "level": "string", 
    "tagsOrConcepts": "string[]",
    "text": "string[]",
    "alternatives": [{"id": string, "text": string[], "feedback":string, "correct":boolean}]
}
```

**id**: UUID único de identificação da questão
 
**SKU**: número do exercício
 
**interpreter**: deve ser sempre 1
 
**type**: deve ser sempre “VF”
 
**language**: nome da linguagem (”java | csharp | javascript | typescript | python | kotlin | clojure”)

**knowledgeArea:** área da conhecimento ("Front-End	| Back-End |	Banco de Dados	| DevOps	| Dados")

**category:** categoria à qual o conteúdo pertence (Ex: "Lógica de programação", isso indica que o exercício aborda algum conceito de lógica de programação)

**subCategory:** especifica a subcategoria do conteúdo (Ex: "Variáveis", isso indica que o texto focará em conceitos e práticas relacionadas ao uso de variáveis na programação)

**level**: dificuldade da questão (”Basic | Medium | Advanced )
 
**tagsOrConcepts**: lista de conceitos trabalhados (deve vir dos conceitos listados no planejamento do módulo)
 
**text**: enunciado da questão, optamos por usar uma lista de linhas. Podemos adicionar imagens ao enunciado também, veja no exemplo abaixo. Caso deseje adicionar código, use formatação markdown. Atenção para adicionar uma linha em branco antes de iniciar e após encerrar o bloco de código "```"
 
**alternatives**: devem ser sempre uma lista de ao menos 4 objetos

**id**: UUID único de identificação da alternativa
 
**text**: texto da alternativa, optamos por usar uma lista de linhas. Caso deseje adicionar código, use formatação markdown. Atenção para adicionar uma linha em branco antes de iniciar e após encerrar o bloco de código "```"
 
**feedback**: o que o aluno verá se escolher essa alternativa, deve conter um feedback claro do porquê essa alternativa é a verdadeira ou porque é falsa
 
**correct**: As alternativas devem ter o valor *true* se forem verdadeiras e *false* se forem falsas
 
### **Exemplo:**
 
```json
{
    "id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd",
    "SKU": "000001",
    "interpreter": 1,
    "type": "VF",
    "language": "javascript",
    "knowledgeArea": "Front-End",
    "category": "Lógica de programação",
    "subCategory": "variáveis",
    "level": "Basic", 
    "tagsOrConcepts":["variáveis", "constantes"],
    "text": [
        "Qual(is) comando(s) correto(s) para criar uma variável sem hoisting? !(link da imagem)"
    ],
    "alternatives": [
        {"id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd", "text": ["var"], "feedback":"var é a única forma de declaração que permite hoisting", "correct":false},
        {"id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd", "text": ["let"], "feedback":"let tem escopo fechado e não faz hoisting", "correct":true},
        {"id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd", "text": ["const"], "feedback":"const tem escopo fechado e não faz hoisting", "correct":true},
        {"id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd", "text": ["def"], "feedback":"def não existe no JS", "correct":false},
        {"id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd", "text": ["#DEF]", "feedback":"#DEF não existe no JS", "correct":false}
    ]
}
```
 
# Questões de lacuna
 
### **Diretrizes Técnicas:**
 
```json
{
    "id": string, 
    "SKU": "string",
    "interpreter": number,
    "type": "string",
    "language": "string",
    "knowledgeArea": "string",
    "category": "string",
    "subCategory": "string",
    "level": "string", 
    "tagsOrConcepts": "string[]",
    "text": "string[]",
    "alternatives": [{ "id": string, "value": string, "hint": string }],
    "gaps": [{"expected": string, "feedbacks": [{ "value": string, "text": string}] }]
}
```
**id**: UUID único de identificação da questão
 
**SKU**: número do exercício
 
**interpreter**: deve ser sempre 1
 
**type**: deve ser sempre “GAP”
 
**language**: nome da linguagem (”java | csharp | javascript | typescript | python | kotlin | clojure”)

**knowledgeArea:** área da conhecimento ("Front-End	| Back-End |	Banco de Dados	| DevOps	| Dados")

**category:** categoria à qual o conteúdo pertence (Ex: "Lógica de programação", isso indica que o exercício aborda algum conceito de lógica de programação)

**subCategory:** especifica a subcategoria do conteúdo (Ex: "Variáveis", isso indica que o texto focará em conceitos e práticas relacionadas ao uso de variáveis na programação)

**level**: dificuldade da questão (”Basic | Medium | Advanced )
 
**tagsOrConcepts**: lista de conceitos trabalhados (deve vir dos conceitos listados no planejamento do módulo)
 
**text**: enunciado da questão, optamos por usar uma lista de linhas, aqui você adiciona o token `{{GAP}}` onde desejar criar uma lacuna. Caso deseje adicionar código, use formatação markdown. Atenção para adicionar uma linha em branco antes de iniciar e após encerrar o bloco de código "```"
 
**alternatives**: devem ser sempre uma lista de objetos, cada um se tornará o botão para o aluno usar para preencher a lacuna:

**id**: UUID único de identificação da alternativa
 
**text**: texto da alternativa. Caso deseje adicionar código, use formatação markdown. Atenção para adicionar uma linha em branco antes de iniciar e após encerrar o bloco de código "```"
 
**hint**: um valor opcional para ajudar o aluno, aparece no mouseOver do botão
 
**gaps**: Uma lista **ordenada na mesma ordem das lacunas** de objetos:
 
**expected**: o valor esperado para a lacuna, deve bater com o `text` de uma das `alternatives`
 
**feedback**: Um objeto contendo uma lista de feedbacks caso uma opção errada seja usada para preencher a lacuna
 
**value**: o valor incorreto que foi colocado na lacuna deve bater com o `text` de uma das `alternatives`
 
**text**: um texto de feedback apontando porque essa não é uma opção correta para a lacuna
 
### **Exemplo:**
 
```json
{
    "id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd",
    "SKU": "000001",
    "interpreter": 1,
    "type": "GAP",
    "language": "javascript",
    "knowledgeArea": "Front-End",
    "category": "Lógica de programação",
    "subCategory": "variáveis",
    "level": "Basic", 
    "tagsOrConcepts":["variáveis", "constantes"],
    "text": [
        "Complete o código a seguir.",
        " ",
        "```js ",
        "{{GAP}} nota1 = parseFloat(prompt('Digite a primeira nota:'));",
        "{{GAP}} nota2 = parseFloat(prompt('Digite a segunda nota:'));",
        "{{GAP}} media = (nota1 + nota2) / 2.0;",
        "console.log(media);",
        "``` ",
        " "
    ],
    "alternatives": [
        { "id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd", "value": "var", "hint": "" },
        { "id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd", "value": "let", "hint": "" },
        { "id": "4ea3c353-cae9-45dc-af54-dbc343bd45cd", "value": "const", "hint": "" }
    ],
    "gaps": [
        {
            "expected": "const", "feedbacks": [
                { "value":"var", "text":"var é pouco usada hoje em dia no JS prefira const ou let"},
                { "value":"let", "text":"nesse caso é preferível o uso de const já que o valor não se altera"}
            ]
        },
        {
            "expected": "const", "feedbacks": [
                { "value":"var", "text":"var é pouco usada hoje em dia no JS prefira const ou let"},
                { "value":"let", "text":"nesse caso é preferível o uso de const já que o valor não se altera"}
            ]
        },
        {
            "expected": "const", "feedbacks": [
                { "value":"var", "text":"var é pouco usada hoje em dia no JS prefira const ou let"},
                { "value":"let", "text":"nesse caso é preferível o uso de const já que o valor não se altera"}
            ]
        }
    ]
}
```
## Ferramenta de validação dos exercícios

Você poderá utilizar [esta ferramenta](https://pedagogico.letscode.com.br/exercise-helper) para validar e garantir que o exercício esteja dentro do padrão utilizado na nossa plataforma.

# Elicitação de requisitos
Etapa para levantar inicialmente os requisitos funcionais, não-funcionais e as regras de negócio junto à equipe do projeto
## Requisitos funcionais
1. O sistema deve permitir que o usuário copie no editor um código em Python 
2. O sistema deve aceitar códigos de até 100 linhas
3. O sistema deve apresentar ao usuário (como saída) o código traduzido em Javascript
4. O sistema deve permitir que o usuário copie o código de saída
5. O sistema deve permitir que o usuário visualize suas últimas 5 traduções (histórico)

## Requisitos não-funcionais
1. O sistema deve ser capaz de converter os códigos em menos de 3 segundos
2. O  sistema deve ser capaz de traduzir o código com precisão e confiabilidade, sem introduzir erros ou problemas que possam afetar a execução do código.
3. O sistema deve ter uma interface intuitiva e clara para qualquer usuário, inclusive iniciantes na programação
4. O sistema deve ser desenvolvido de forma a permitir fácil manutenção e atualização no futuro, incluindo suporte para correção de bugs, novos recursos e atualizações de linguagem.
5. O sistema deve ser desenvolvido na linguagem Python e guardar as últimas cinco interações do usuário a partir do Local Storage

# Especificação de requisitos
RF01: Incluir trecho em Python
RF02: Limitar linhas de códigos
RF03: Mostrar saída em Javascript
RF04: Copiar saída
RF05: Visualizar últimas traduções

NF01: Desempenho (tempo de resposta)
NF02: Confiabilidade
NF03: Usabilidade
NF04: Manutenibilidade
NF05: Software (desenvolvimento e persistência de dados)

# Documento de requisitos 

## 1. Introdução

Este documento apresenta uma descrição detalhada e clara dos requisitos do PY2JS. Assim, por meio deste documento, os stakeholders tomarão conhecimento e auxiliarão na validação das funcionalidades do sistema projetado e os desenvolvedores terão uma noção de como implementar essas funcionalidades. Em outras palavras, o documento visa a compreensão e validação dos requisitos pelos clientes e usuários, além de fornecer aos projetistas e desenvolvedores as informações necessárias para a implementação e também para a realização dos testes e homologação do sistema.

### **1.1. Objetivos e escopo**

Dentre os objetivos deste documento estão o de listar da forma mais clara e objetiva possível os requisitos funcionais e não funcionais do sistema projetado, e especificá-los especialmente para que os desenvolvedores e projetistas possam realizar suas atividades de implementação e testagem. Assim, o documento visa ser utilizado por todos os stakeholders do projeto, desde os clientes e usuários, até a equipe de desenvolvimento do sistema, em detalhes e de forma compreensiva para todos.

### **1.2. Visão geral do documento**

- Seção 2: Descrição geral do sistema (descreve o escopo do sistema e seus usuários de maneira geral)
- Seção 3: Requisitos Funcionais (especifica todos os requisitos funcionais planejados para o sistema)
- Seção 4: Requisitos Não Funcionais (especifica todos os requisitos não funcionais planejados para o sistema)
- Seção 5: Análise dos Requisitos (especifica as prioridades e dependências dos requisitos)
- Seção 6: Glossário (apresenta definições de termos técnicos e relevantes)

### **1.3. Convenções, termos e abreviações**

A correta interpretação deste documento exige o conhecimento de algumas convenções e termos específicos, que são descritos a seguir.

#### *1.3.1. Identificação dos requisitos*

Por convenção, a referência a requisitos é feita através do nome da subseção onde eles estão descritos seguidos do identificador do requisito, de acordo com a especificação a seguir: [nome da subseção. identificador do requisito]
Por exemplo, o requisito funcional [Inserir trecho em Python.RF01] deve estar descrito em uma subseção chamada “Inserir trecho em Python”, em um bloco identificado pelo número [RF01]. Já o requisito não ­funcional [Desempenho. NF01] deve estar descrito na seção de requisitos não ­funcionais de Desempenho, em um bloco identificado por [NF01].
Os requisitos devem ser identificados com um identificador único. A numeração inicia com o identificador [RF01] ou [NF01] e prossegue sendo incrementada à medida que forem surgindo novos requisitos.

#### *1.3.2. Propriedades dos requisitos*

A cada requisito será atribuída uma prioridade. A descrição de cada uma segue abaixo:
**Essencial** é o requisito sem o qual o sistema não entra em funcionamento. Requisitos essenciais são requisitos imprescindíveis, que sem eles o sistema não funcionará, e por isso têm que ser implementados impreterivelmente.
**Importante** é o requisito sem o qual o sistema entra em funcionamento, mas de forma não satisfatória. Requisitos importantes devem ser implementado, mas, se não forem, o sistema poderá se rimplantado e usado.
**Desejável**  é o requisito que não compromete as funcionalidades básicas do sistema, isto é, o sistema pode funcionar de forma satisfatória. Por isso, requisitos desejáveis podem ser deixados para ser implementados por último ou em próximas iterações.

## 2. Descrição geral do sistema

O sistema proposto oferece uma forma simples e prática para converter códigos de uma linguagem para outra, especificamente de Python para Javascript. No contexto atual do desenvolvimento de softwares e sistemas, existem cada vez mais linguagens de programação com suas peculiaridades e seus usos recomendados, mas apesar de trazerem vantagens por serem especializadas e diversificadas, trazem também empecilhos devido à quantidade de linguagens. Para um programador ou desenvolvedor, seria interessante ter uma ferramenta que permita converter seus códigos rapidamente, tanto para fins de aprendizagem quanto profissionais, se for requisitado em seu trabalho o desenvolvimento em uma linguagem de programação específica não tão dominada pelo programador. A partir do sistema aqui projetado, será possível facilitar os desenvolvedores a desempenhar seus trabalhos e demandas do dia a dia, e auxiliar sua aprendizagem em novas linguagens de programação a partir das similaridades com as que ele já domina ou compreende bem. 

### **2.1. Escopo Negativo**

Devido a dimensão que o projeto pode ter, faz-se relevante definir o escopo não apenas dizendo as coisas que serão feitas, mas também deixando claro o que não fará parte do nosso escopo.
Algumas funcionalidades foram tidas pela equipe como aquelas que precisam de uma maior atenção, e são imprescindíveis para atingir os objetivos de forma satisfatória. Sendo assim, este projeto se compromete a desenvolver apenas as funcionalidades citadas. Não fazem parte do escopo desta proposta serviços tais como: 
- Desenvolver outras funcionalidades, como aceitar outras formas de envio de códigos para tradução, no caso de upload de arquivos por exemplo;
- Utilizar um sistema de banco de dados mais abrangente, com necessidade de cadastro de usuários;
- Manter o sistema no ar;
- Traduzir o código de forma contextual, sendo traduzido a partir de suas linhas e chamadas individuais.

## 3. Requisitos Funcionais

### **3.1. Inserir trecho em Python [RF01]**
Prioridade: Essencial
O sistema deve permitir que o usuário copie no editor um código em Python para que possa realizar a sua tradução. Requisito básico para permitir que o usuário insira o trecho de código desejado e decida traduzí-lo. É a principal função do sistema.

### **3.2. Limitar linhas de códigos [RF02]**
Prioridade: Importante
O sistema deve aceitar códigos de até 100 linhas, limitando a quantidade de código a ser traduzida pelo sistema e garantindo o desempenho e a confiabilidade.

### **3.3. Mostrar saída em Javascript [RF03]**
Prioridade: Essencial
O sistema deve apresentar ao usuário (como saída) o código traduzido em Javascript na caixa de texto no canto inferior da tela. Requisito básico para permitir que o usuário tenha acesso ao código que foi traduzido, a partir daquele que foi inserido na caixa de texto no canto superior.

### **3.4. Copiar saída [RF04]**
Prioridade: Importante
O sistema deve permitir que o usuário copie o código de saída, para facilitar que seja transposto do sistema para o lugar desejado ao usuário.

### **3.5. Visualizar últimas traduções [RF05]**
Prioridade: Importante
O sistema deve permitir que o usuário visualize suas últimas 5 traduções, como um histórico das traduções realizadas anteriormente no sistema. O usuário deve ser capaz de visualizar, na aba lateral da tela, as cinco últimas traduções, no caso suas três primeiras linhas para identificação, e voltar à elas, para poder ver o código completo tanto aquele inserido quanto o que foi traduzido, podendo copiá-lo mas não modificá-lo.


## 4. Requisitos Não Funcionais

### **4.1. Desempenho [NF01]**
Prioridade: Importante.
O sistema deve ser capaz de converter os códigos em menos de 3 segundos, para que o tempo de resposta não seja entendido pelo usuário como um erro de sistema.

### **4.2. Confiabilidade [NF02]**
Prioridade: Essencial
O  sistema deve ser capaz de traduzir o código com precisão e confiabilidade, sem introduzir erros ou problemas que possam afetar a execução do código.

### **4.3. Usabilidade [NF03]**
Prioridade: Importante
O sistema deve ter uma interface intuitiva e clara para qualquer usuário, inclusive iniciantes na programação, utilizando para isso padrões e heurísticas do design de interação.

### **4.4. Manutenibilidade [NF04]**
Prioridade: Importante
O sistema deve ser desenvolvido de forma a permitir fácil manutenção e atualização no futuro, incluindo suporte para correção de bugs, novos recursos e atualizações de linguagem. Isso porque as linguagens de promoção estão sempre tendo atualizações, e para prevenir que o sistema fique obsoleto muito rápido, a manutenibilidade é um requisito importante.

### **4.5. Software [NF05]**
Prioridade: Essencial
O sistema deve ser desenvolvido na linguagem Python e também deve guardar as últimas cinco interações do usuário a partir do Local Storage, que é uma forma de ter persistência de dados sem injetar muita complexidade no sistema.


## 5. Análise dos Requisitos (em construção...)


## 6. Glossário (em construção...)


## Anexos

### **Protótipos de baixa fidelidade, wireframes e alta fidelidade**

Link do Figma: https://www.figma.com/file/F8hW93PGV8D4gf63OoLewC/PY2JS?node-id=0-1&t=oR2rAqwLGyKaERb0-0 


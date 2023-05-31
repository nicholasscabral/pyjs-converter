# Elicitação de requisitos

Etapa para levantar inicialmente os requisitos funcionais, não-funcionais e as regras de negócio junto à equipe do projeto

## Requisitos funcionais

1. O sistema deve poder ler um arquivo em python (extensão py)
2. O sistema deve aceitar códigos de até 25 linhas
3. O sistema deve escrever o código em Javascript num arquivo de saída
4. O sistema deve converter apenas códigos em python compiláveis

## Requisitos não-funcionais

1. O sistema deve ser capaz de converter os códigos em menos de 3 segundos
2. O sistema deve ser capaz de traduzir o código com precisão e confiabilidade, sem introduzir erros ou problemas que possam afetar a execução do código.
3. O sistema deve ser desenvolvido de forma a permitir fácil manutenção e atualização no futuro, incluindo suporte para correção de bugs, novos recursos e atualizações de linguagem.
4. O sistema deve ser desenvolvido na linguagem Python

# Especificação de requisitos

RF01: Receber arquivo .py
RF02: Limitar linhas do código de entrada
RF03: Escrever código traduzido em arquivo de saída .js
RF04: Converter códigos compiláveis

NF01: Desempenho (tempo de resposta)
NF02: Confiabilidade
NF03: Manutenibilidade
NF04: Software (desenvolvimento)

# Documento de requisitos

## 1. Introdução

Este documento apresenta uma descrição detalhada e clara dos requisitos do PYJS. Assim, por meio deste documento, os stakeholders tomarão conhecimento e auxiliarão na validação das funcionalidades do sistema projetado e os desenvolvedores terão uma noção de como implementar essas funcionalidades. Em outras palavras, o documento visa a compreensão e validação dos requisitos pelos clientes e usuários, além de fornecer aos projetistas e desenvolvedores as informações necessárias para a implementação e também para a realização dos testes e homologação do sistema.

### **1.1. Objetivos e escopo**

Dentre os objetivos deste documento estão o de listar da forma mais clara e objetiva possível os requisitos funcionais e não funcionais do sistema projetado, e especificá-los especialmente para que os desenvolvedores e projetistas possam realizar suas atividades de implementação e testagem. Assim, o documento visa ser utilizado por todos os stakeholders do projeto, desde os clientes e usuários, até a equipe de desenvolvimento do sistema, em detalhes e de forma compreensiva para todos.

### **1.2. Visão geral do documento**

- Seção 2: Descrição geral do sistema (descreve o escopo do sistema e seus usuários de maneira geral)
- Seção 3: Requisitos Funcionais (especifica todos os requisitos funcionais planejados para o sistema)
- Seção 4: Requisitos Não Funcionais (especifica todos os requisitos não funcionais planejados para o sistema)

### **1.3. Convenções, termos e abreviações**

A correta interpretação deste documento exige o conhecimento de algumas convenções e termos específicos, que são descritos a seguir.

#### _1.3.1. Identificação dos requisitos_

Por convenção, a referência a requisitos é feita através do nome da subseção onde eles estão descritos seguidos do identificador do requisito, de acordo com a especificação a seguir: [nome da subseção. identificador do requisito]
Por exemplo, o requisito funcional [Inserir trecho em Python.RF01] deve estar descrito em uma subseção chamada “Inserir trecho em Python”, em um bloco identificado pelo número [RF01]. Já o requisito não ­funcional [Desempenho. NF01] deve estar descrito na seção de requisitos não ­funcionais de Desempenho, em um bloco identificado por [NF01].
Os requisitos devem ser identificados com um identificador único. A numeração inicia com o identificador [RF01] ou [NF01] e prossegue sendo incrementada à medida que forem surgindo novos requisitos.

#### _1.3.2. Propriedades dos requisitos_

A cada requisito será atribuída uma prioridade. A descrição de cada uma segue abaixo:
**Essencial** é o requisito sem o qual o sistema não entra em funcionamento. Requisitos essenciais são requisitos imprescindíveis, que sem eles o sistema não funcionará, e por isso têm que ser implementados impreterivelmente.
**Importante** é o requisito sem o qual o sistema entra em funcionamento, mas de forma não satisfatória. Requisitos importantes devem ser implementado, mas, se não forem, o sistema poderá ser implementado e usado.
**Desejável** é o requisito que não compromete as funcionalidades básicas do sistema, isto é, o sistema pode funcionar de forma satisfatória. Por isso, requisitos desejáveis podem ser deixados para ser implementados por último ou em próximas iterações.

## 2. Descrição geral do sistema

O sistema proposto oferece uma forma simples e prática para converter códigos de uma linguagem para outra, especificamente de Python para Javascript. No contexto atual do desenvolvimento de softwares e sistemas, existem cada vez mais linguagens de programação com suas peculiaridades e seus usos recomendados, mas apesar de trazerem vantagens por serem especializadas e diversificadas, trazem também empecilhos devido à quantidade de linguagens. Para um programador ou desenvolvedor, seria interessante ter uma ferramenta que permita converter seus códigos rapidamente, tanto para fins de aprendizagem quanto profissionais, se for requisitado em seu trabalho o desenvolvimento em uma linguagem de programação específica não tão dominada pelo programador. A partir do sistema aqui projetado, será possível facilitar os desenvolvedores a desempenhar seus trabalhos e demandas do dia a dia, e auxiliar sua aprendizagem em novas linguagens de programação a partir das similaridades com as que ele já domina ou compreende bem.

### **2.1. Escopo Negativo**

Devido a dimensão que o projeto pode ter, faz-se relevante definir o escopo não apenas dizendo as coisas que serão feitas, mas também deixando claro o que não fará parte do nosso escopo.
Algumas funcionalidades foram tidas pela equipe como aquelas que precisam de uma maior atenção, e são imprescindíveis para atingir os objetivos de forma satisfatória. Sendo assim, este projeto se compromete a desenvolver apenas as funcionalidades citadas. Não fazem parte do escopo desta proposta serviços tais como:

- Desenvolver outras funcionalidades, como aceitar outras extensões de arquivos de envio de códigos para tradução;
- Utilizar um sistema de banco de dados mais abrangente, com necessidade de cadastro de usuários;
- Manter o sistema no ar;
- Traduzir o código de forma contextual, sendo traduzido a partir de suas linhas e chamadas individuais.

## 3. Requisitos Funcionais

### **3.1. Receber arquivos .py [RF01]**

Prioridade: Essencial
O sistema deve permitir que o usuário suba um arquivo com código em Python, extensão py, para que possa realizar a sua tradução. Requisito básico para permitir que o usuário insira o arquivo e decida traduzi-lo. É a principal função do sistema.

### **3.2. Limitar linhas do código de entrada [RF02]**

Prioridade: Importante
O sistema deve aceitar códigos de até 20 linhas, limitando a quantidade de código a ser traduzido pelo sistema e garantindo o desempenho e a confiabilidade.

### **3.3. Escrever código traduzido em arquivo de saída .js [RF03]**

Prioridade: Essencial
O sistema deve apresentar ao usuário o código traduzido em Javascript em um arquivo de saída. Requisito básico para permitir que o usuário tenha acesso ao código que foi traduzido, a partir daquele que foi feito o upload.

### **3.4. Converter códigos compiláveis [RF05]**

Prioridade: Essencial
O sistema deve converter apenas códigos em Python que sejam compiláveis, retornando erro caso não sejam. Requisitos básico para impedir a conversão de códigos não compiláveis e com bugs.

## 4. Requisitos Não Funcionais

### **4.1. Desempenho [NF01]**

Prioridade: Importante.
O sistema deve ser capaz de converter os códigos em menos de 3 segundos, para que o tempo de resposta não seja entendido pelo usuário como um erro de sistema.

### **4.2. Confiabilidade [NF02]**

Prioridade: Essencial
O sistema deve ser capaz de traduzir o código com precisão e confiabilidade, sem introduzir erros ou problemas que possam afetar a execução do código.

### **4.3. Manutenibilidade [NF04]**

Prioridade: Importante
O sistema deve ser desenvolvido de forma a permitir fácil manutenção e atualização no futuro, incluindo suporte para correção de bugs, novos recursos e atualizações de linguagem. Isso porque as linguagens de promoção estão sempre tendo atualizações, e para prevenir que o sistema fique obsoleto muito rápido, a manutenibilidade é um requisito importante.

### **4.4. Software [NF05]**

Prioridade: Essencial
O sistema deve ser desenvolvido na linguagem Python.


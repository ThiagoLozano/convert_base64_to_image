# Project: Conversão Base64 para Imagem & Imagem para Base64

O projeto tem como objetivo receber uma **Imagem** (JPEG, PNG, GIF, etc...) e converter para dados binários do tipo **Base64**. Também sendo capaz de converter os dados do **Base64** para a **Imagem**.

## Índice

- [Visão Geral](#Vião-Geral)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#Instalação)
- [Uso](#uso)
- [Exemplos](#exemplos)



## Visão Geral

O projeto utiliza-se da linguagem **Python** e suas bibliotecas, para integrar e validar as informações da imagem e do Base64. Estruturada em módulos separados onde podem ser declarados entre eles, deixando o projeto mais legível e organizado.

Para converter a **Imagem** em **Base64**, ele deve receber como parâmetro um path que aponta direto para a imagem que será convertida.

Para converter o **Base64** em **Imagem**, ele deve receber como parâmetro um valor binário completo e o **diretório** em que deseja salvar a imagem gerada.



## Pré-Requisitos

### Linguagem

- Python3 ou Superior

### IDE

- Qualquer IDE utilizada pelo DEV, 
- Para esse projeto foi utilizado o **VSCODE**.



## Instalação

1. Clone o repositório:

   ```git
   git clone https://github.com/ThiagoLozano/convert_base64_to_image.git
   ```

2. Instale as Dependências:

   **PIL**

   ```
   pip install pillow
   ```

3. Configure as variáveis de ambiente:

   ```python
   img_path_input  = r'' # Caminho onde fica a imagem de entrada.
   img_path_output = r'' # Caminho onde fica deverá ficar a imagem de saída.
   ```



## Estrutura

O projeto tem a seguinte estrutura:

```she
├───img_input
│   └───imagem.png
├───img_output
├───resources
│   └───__pycache__
│   └───functions.py
│   └───lib.py
│   └───varibales.py
└───unit_tests
│   └───tdd.py
├───main.py
```



### img_input

- Responsável por guardar as **Imagens** onde deseja ser convertido em **Base64**;
- Essa pasta pode ser criada em qualquer lugar, lembrando apenas de mencionar seu caminho nas variáveis.

### img_output

- Responsável por guardar as **Imagens** que foram convertidas de um **Base64**;
- Essa pasta pode ser criada em qualquer lugar, lembrando apenas de mencionar seu caminho nas variáveis.

### Resources

- Responsável por armazenar os módulos do projeto, separando suas responsabilidades em cada arquivo **.py**

#### [Functions.py]

- Responsável por armazenar as funções utilizadas no projeto.

#### [Lib.py]

- Responsável por armazenar as bibliotecas utilizadas no projeto.

#### [Variables.py]

- Responsável por armazenar as variáveis utilizadas no projeto.

### Unit_Test

- Responsável por armazenar os **Testes Unitários** do projeto.

#### [Tdd.py]

- Responsável for gerar testes das funções, passando pelo caminhos positivos e negativos. Importante para testar o projeto em momentos de estresse de atividades e novos ajustes.

### Main.py

- Responsável por iniciar o projeto, é o arquivo principal que chama todas as funções necessárias e executa as conversões necessárias.



### Uso

1. Abra o projeto na sua IDE;

2. Certifique-se de apontar os caminhos corretos no módulo **variables.py**;

3. Abra o arquivo **main.py**

4. Para converter uma imagem em Base64, você deve chamar a função **convert_image_to_base64**()

   4.1 Lembre-se de passar o caminho da imagem, sendo ele obrigatório.

   4.2 Execute o arquivo;

   4.3 Ele irá retornar seus status, sendo ele positivo ou negativo e informará o que ocorreu.

5. Para converter um Base64 em Imagem, você deve chamar a função **convert_base64_to_image()**

   5.1 Lembre-se de passar o objeto **Base64**, sendo ele obrigatório e o nome que você deseja que a imagem receba (caso seja vazio, ela recebe um nome padrão).

   5.2 Execute o arquivo;

   5.3 Ele irá retornar seus status, sendo ele positivo ou negativo e informará o que ocorreu.

6.  Caso você queira apenas que uma da funções execute, você pode remover a outra ou apenas comenta-lá.

   ```python
   convert_image_to_base64(path_image=img_input)
   # convert_base64_to_image(base=base_64)
   
   ========//===================//==================//======================
   
   #convert_image_to_base64(path_image=img_input)
   convert_base64_to_image(base=base_64)
   
   ========//===================//==================//======================
   
   convert_image_to_base64(path_image=img_input)
   convert_base64_to_image(base=base_64)
   
   ```



**Obs:**

- Para esse exemplo, ele recebe apenas uma imagem por vez no parâmetro, mas ele pode facilmente ser ajustado para receber uma série de imagens, seja em listas ou dicionários.
- Certifique-se do projeto estar apontando corretamente para os diretórios corretos da sua máquina.



### Exemplos

1. Chama a função para converter uma **Imagem** em **Base64**.

   ```python
   # =============================
   #  Converte a imagem em Base64
   # =============================
   
   img_input = ivars.img_path_input
   
   conversao_para_base64 = function.convert_image_to_base64(path_image=img_input)
   
   if conversao_para_base64['status'] == 1:
       print(conversao_para_base64['message'])
       base_64 = conversao_para_base64['obj']
   
   elif conversao_para_base64['status'] == -1:
       print(conversao_para_base64['message'])
   
   ```

2. Chama a função para converter o **Base64** em uma **Imagem**:

   ```python
   # =============================
   #  Converte o Base64 em imagem
   # =============================
   
   convercao_para_imagem = function.convert_base64_to_image(base=base_64, name_image='teste')
   
   if convercao_para_imagem['status'] == 1:
       print(convercao_para_imagem['message'])
   
   elif convercao_para_imagem['status'] == -1:
       print(convercao_para_imagem['message'])
   
   ```


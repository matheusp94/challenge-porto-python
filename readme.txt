equipe:

99792 - Matheus Matos Pereira
99554 - Julianny Araújo Pereira
99468 - Karen Vitória Jesus da Silva
99456 - Caio Cesar Arruda

Instruções: Utilizar, se necessário:

pip install pandas
pip install tabulate
não é necessário para json, pois é um modulo buildt-in.

O programa recebe um arquivo csv chamado bancodedados.csv com o seguinte delimitador --> ;
Porém o código aceita outros delimitadores csv.
É importante destacar que, na leitura do csv em excel, o arquivo testado apresenta cada coluna de forma adequada. Isso é importante visto que alguns csv possuem todo o conteúdo em uma unica coluna. É interessante formatar um csv dessa forma se necessário.


'''No excel:
Abra o arquivo no excel;
Clique na guia "Dados";
Clique em "texto para colunas";
Escolha a opção "delimitado" e clique em avançar;
escolha a opção mais indicada (geralmente se trata de virgula) e clique em avançar;
Depois concluir.'''

*Utilize uma coluna id no arquivo para identificar os registros.


Este código Python é um programa de console que interage com um banco de dados em formato CSV e um arquivo JSON. Ele permite realizar operações como adicionar, editar, remover e visualizar registros no banco de dados. Aqui está uma explicação do que cada parte do código faz:

O programa começa importando as bibliotecas necessárias, incluindo pandas para manipulação de dados, json para operações com arquivos JSON e tabulate para tornar o menu mais atraente.

Em seguida, o código tenta ler um arquivo CSV chamado 'bancodedados.csv' usando a biblioteca pandas. Ele verifica se o arquivo existe e se pode ser decodificado corretamente. Se houver algum problema, ele trata as exceções correspondentes e exibe uma mensagem de erro.

Após a leitura bem-sucedida do arquivo CSV, os registros do DataFrame são convertidos em uma lista de dicionários chamada registros.

O código cria um arquivo JSON chamado 'bancodedados.json' a partir dos registros e o salva no disco.

Há duas funções definidas: carregar_json() para carregar o arquivo JSON e salvar_json() para salvar os dados JSON de volta no arquivo.

A função adicionar_registro() permite adicionar um novo registro ao banco de dados, incrementando automaticamente o valor do campo "id".

A função editar_registro() permite editar um registro existente com base no ID.

A função remover_registro() permite remover um registro com base no ID.

A função visualizar_registros() exibe todos os registros na forma de uma tabela formatada.

O programa entra em um loop principal que exibe um menu de opções, permitindo que o usuário escolha entre adicionar, editar, remover, visualizar registros ou sair do programa.

Dependendo da escolha do usuário, o programa chama as funções correspondentes para executar a operação desejada.

O programa continuará a ser executado até que o usuário escolha a opção "Sair".

O objetivo deste código é criar uma interface de linha de comando para gerenciar um banco de dados em formato CSV, permitindo que o usuário realize operações básicas de CRUD (criação, leitura, atualização e exclusão) nos registros do banco de dados.
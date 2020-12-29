# Lugar-Geometrico
Projeto destinado a implementar um algoritmo para construir um LG polígono de "n" lado segundo a recomendação do ONS 

## Fonte
O algoritmo para elaborar este código foi removido da referência:  
**Artigo:** Metodologia para a Representação de Redes Elétricas por Polígono de Adimitâncias para Estudo de Impacto Harmônicos  
**Autores:** Sergio Luis Varricchio e Cristiano de Olibeira Costa  
**Data:** 20/09/2017  
**Apresentado:** XXII SNPTEE  

## Como montar os arquivos que o código irá ler  
O algoritmo utiliza as adimitância (ou impedâncias) na forma retangular, de forma que é necessário salvar os valores relacionados a parte real e imaginária em arquivos sepadaros. Os valores devem ser salvos de maneira sequencial no arquivo, com um valor por linha.  
**IMPORTANTE:** Os valores relacionados a parte real e imaginária da adimitância/impedâncias devem ocupar as mesmas posições em seus respectivos arquivos para que o algoritmo opere corretamente.  

## Com relação à extensão dos arquivos  
Tanto os arquivos que o algoritmo irá ler, quanto os que ele irá salvar, devem possuir a extensão ".txt".  

## Com relação à imagem exportada  
O algoritmo exporta automaticamente uma imagem chamada pnl.png para a pasta onde o código foi salvo. Essa imagem é uma cópia do polígono de "n" lados criado pelo algoritmo.  

## Com relação ao arquivo exportado  
O algoritmo exporta automaticamente um arquivo chamado Vertices.txt para a pasta onde o código foi salvo. Esse arquivo contém os vértices, como par ordenado, que compõem a envoltória do polígono de "n" lados criado pelo algoritmo.  

## Como utilizar o algoritmo  
Para utilizar o algoritmo é necessário indicar para ele quais os arquivos que contêm os valores das partes real e imaginária da adimitância/impedâncias que compõem a nuvem de pontos. Existem duas possibilidades para fazer isso: a primeira é passar o caminho de cada um dos arquivos como parâmetro durante a execução do código, vide o exemplo a seguir; a segunda forma é, caso os caminhos não sejam passados como parâmetro, fornecer para o algoritmo durante a execução, ele irá solicitar automaticamente.  

'''
python3 app.py x.txt y.txt
'''  

**IMPORTANTE:** Ao passar os caminhos como parâmetros é necessário inserir primeiro o arquivo que contém a parte real e, em seguida, o que contém a parte imaginária.
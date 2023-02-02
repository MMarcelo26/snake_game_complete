Breve explicação do script para o Meu Snake Game

Inicialmente importaremos a biblioteca turtle que fornecerá a interface gráfica para o jogo.
L4 -> Criando o objeto tela
L5 -> Definindo largura e altura através do método .setup()
L6 -> Cor de fundo através do método .bgcolor() 
L7 -> Título do jogo através do método .title()
L8 -> método tracer() da classe screen é responsável por gerar um delay entre cada desenho para gerar a sensação de continuidade

L10 -> Lista de tuplas que define a posição inicial dos 3 quadrados que são o corpo inicial da cobra

L14 -> Loop que irá gerar os 3 quadrados
	L15-> Criando o objeto novo_segmento que será um quadrado
	L16-> Definindo a cor do quadrado como branca através do método .color()
	L17-> Eliminando a animação da caneta após o ''movimento'' dos quadrados
	L18-> movimento os quadrados através do método goto()
	L19-> colocando cada objeto na lista segmentos 

L21-> Variável de controle que define se o game está funcionando ou não 

L23-> While que ocorrerá perpetuamente
L25-> Dando um update a cada frame afim de gerar continuidade

L28 -> L31
Essa repetição fara com que o terceiro objeto assuma a posição do segundo e o segundo assuma a posição
do primeiro, de modo que caso a cobra mude de direção, o corpo inteiro segue num movimento contínuo.
Se isso não fosse feito, a uma parte da cobra iria mudar a direção e o resto iria seguir reto.


L48-> Evitar que a tela feche imeditamente após abrir










l
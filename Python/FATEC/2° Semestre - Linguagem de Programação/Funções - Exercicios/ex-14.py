# Crie uma função chamada area_retangulo que aceite dois números como parâmetros (largura e altura) e retorne a área do retângulo. 

def area_retangulo(largura, altura):
    x = largura * altura
    return(x)

print('Área do Retângulo: {}'.format(area_retangulo(largura=int(input('Largura do Retângulo: ')), altura=int(input('Altura do Retângulo: ')))))

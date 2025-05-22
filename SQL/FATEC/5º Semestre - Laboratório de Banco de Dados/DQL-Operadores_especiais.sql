-- Aula 18/03
-- Operadores Especiais

/*
IS NULL: quando não há preenchimento de dados, ou dados são nulos.

Ex.: SELECT * FROM gravadora WHERE endereco IS NULL;
*/

/*
IS NOT NULL: busca informações cadastradas nas tabelas do BD.

Ex.: SELECT * FROM gravadora WHERE contato IS NOT NULL;
*/

/*
BETWEEN (simplificador do operador AND)
- Usado para intervalos fechados com mesma coluna. Valores ou datas.

Ex1.: SELECT * FROM musica WHERE duracao BETWEEN 3 AND 5;

Ex2.: SELECT * FROM cd WHERE year(dtLancto) BETWEEN 1990 AND 1999;
*/

/*
IN (simplificação operador OR)
- Utilizado para retornar valores que existem na amostragem, usa operador relacional (=).

Ex1.: 
  Sintaxe ruim: SELECT * FROM musica WHERE idMusica = 1 OR idMusica = 3 OR idMusica = 3;
  Sintaxe boa: SELECT * FROM musica WHERE idMusica IN (1, 3, 5, 13, 14, 18, 25, 33);

Ex2.: SELECT * FROM autor WHERE nmAutor IN ('a', 'r', 'v');
*/

/*
LIKE (busca por caracter) com auxílio de operadores:
_ (undercore) => 1 posição
% (porcentagem) => 0-n posições

Ex1.: SELECT * FROM gravadora WHERE endereco LIKE 'Rod%';

Ex2.: SELECT * FROM autor WHERE nmAutor LIKE '%a%';
*/

-- DESAFIOS DE OPERADORES LÓGICOS E ESPECIAIS


-- Ex1.:
SELECT * 
FROM musica 
WHERE duracao 
BETWEEN '00:05:00' AND '00:09:00';
go

-- Ex2.:
SELECT *
FROM faixa 
WHERE nroFaixa 
IN (11, 13, 17, 33, 50);
go

-- Ex3.:
SELECT * 
FROM gravadora
ORDER BY nmGravadora ASC;
go

-- Ex4.:
SELECT * 
FROM cdCategoria
WHERE menorPreco > 20 ORDER BY menorPreco ASC;

SELECT *
FROM cdCategoria
WHERE maiorPreco < 40 ORDER BY maiorPreco ASC;
go

-- Qual é a musica?
SELECT count(*)
FROM musica
WHERE nmMusica LIKE '%man%';
go
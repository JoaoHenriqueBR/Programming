/*
Funções de Agregação
- São aplicadas à uma coluna.
  - count(*) -> resultado: qtd de registros na coluna
  - avg(col) -> resultado: média
  - sum(col) -> resultado: soma
  - min(col) -> resultado: valor mínimo
  - max(col) -> resultado: valor máximo
*/


SELECT COUNT(*), idMusica
FROM musicaAutor
GROUP BY idMusica;

SELECT idMusica, COUNT(*) as QtdeAutor
FROM musicaAutor
GROUP BY idMusica;
go

SELECT idAutor, COUNT(*) as idMusica
FROM musicaAutor
GROUP BY idAutor;
go

SELECT COUNT(*)
FROM autor;

SELECT AVG(precoVenda)
FROM cd;

SELECT SUM(cast(datepart(hour, duracao) + (datepart(minute, duracao)) / 60.0 as decimal(5, 2)))
FROM musica;

SELECT MIN(dtLancto)
FROM cd;

SELECT MAX(dtLancto)
FROM cd;

SELECT STDEV(precoVenda)
FROM cd;

SELECT VAR(precoVenda)
FROM cd;

SELECT idCD, COUNT(*) as nroFaixa
FROM faixa
GROUP BY idCD;
go

SELECT idGravadora, COUNT(*) as idCD
FROM cd
GROUP BY idGravadora;
go

SELECT idGravadora, AVG(precoVenda) as idCD
FROM cd
GROUP BY idGravadora;

SELECT MAX(idAutor)
FROM musicaAutor;

-- Qual música têm a maior qtde de autores?
/*
Resolução: primeiro é feito a quantidade de autores em cada música - GROUP BY
depois é feito a procura pelo maior - ORDER BY
*/

SELECT TOP 1 idMusica, COUNT(*) as idAutor
FROM musicaAutor
GROUP BY idMusica
ORDER BY idAutor DESC;

SELECT TOP 1 idGravadora, AVG(precoVenda) as idCD
FROM cd
GROUP BY idGravadora
ORDER BY idGravadora ASC;

/*
GROUP BY - permite que as colunas sejam utilizadas 
como parâmetro para o agrupamento dos dados em 
função das operações de agregação.
*/

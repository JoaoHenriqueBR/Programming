-- DQL - Data Query Language

SELECT idMusica, duracao 
FROM musica;
go

SELECT idCD, nmCD, precoVenda
FROM cd;
go

SELECT *
FROM cdCategoria;
go


-- ORDER BY - Ordernação pelo:
-- ASC (crescente);
-- DESC (decrescente);
-- SINTAXE:

-- Autores em ordem alfabética
SELECT nmAutor 
FROM autor
ORDER BY nmAutor ASC;
go

-- Duração das músicas decrescente
SELECT nmMusica, duracao 
FROM musica
ORDER BY duracao DESC;
go

-- Cd's em ordem de lançamento crescente
SELECT nmCD, dtLancto
FROM cd
ORDER BY dtLancto;

-- Nome das músicas crescente e a duração das músicas decrescente
SELECT nmMusica, duracao
FROM musica
ORDER BY duracao DESC, nmMusica ASC;
go

SELECT idAutor, idMusica 
FROM musicaAutor
ORDER BY idAutor ASC, idMusica DESC;
go

-- WHERE - Filtragem através de condições
-- Condições -> = <> != >= > <= <
-- SINTAXE

SELECT count(*)
FROM gravadora
WHERE idGravadora = 3;
go

SELECT count(*)
FROM musica
WHERE duracao < '00:05:00';

SELECT count(*)
FROM cd
WHERE precoVenda > 20;

SELECT count(*)
FROM cdCategoria
WHERE maiorPreco <= 100;

SELECT count(*)
FROM musicaAutor 
WHERE idAutor >= 2;

SELECT count(*)
FROM autor 
WHERE idAutor >= 2;

SELECT count(*)
FROM faixa
WHERE nroFaixa <> 13;




USE cdFatecManha20251;
GO

--Quais os cadastrados no banco com id e nm

SELECT tabela = 'música', idMusica AS id, nmMusica AS nm
FROM dbo.musica
UNION
SELECT tabela = 'autor', idAutor, nmAutor
FROM dbo.autor
UNION
SELECT tabela = 'gravadora', idGravadora, nmGravadora
FROM dbo.gravadora
UNION
SELECT tabela = 'CD', idCD, nmCD
FROM dbo.cd;

-- Pesquisar quais atores e músicas do cd 1
SELECT Tabela = 'Autor', idAutor AS codigo, nmAutor AS Nome
FROM autor
WHERE idAutor IN 
(
	SELECT idAutor
	FROM musicaAutor
	WHERE idMusica IN 
	(
		SELECT idMusica
		FROM musica
		WHERE idMusica IN
		(
			SELECT idMusica
			FROM faixa
			WHERE idCD = 1
		)
	)
)
UNION ALL
SELECT Tabela = 'Música', idMusica, nmMusica
from dbo.musica
WHERE idMusica IN (SELECT idMusica
				   FROM faixa
				   WHERE idCD = 1);
GO

--INTERSECT (pk x fk) (O que foi usado?)
--Quais as gravadoras que têm cd
SELECT idGravadora
FROM gravadora
INTERSECT
SELECT idGravadora
FROM cd;
GO
--Quais as músicas que têm autor
SELECT idMusica
FROM musica
INTERSECT
SELECT idMusica
FROM musicaAutor;
GO
--Quais autores têm músicas
SELECT idAutor
FROM autor
INTERSECT
SELECT idAutor
FROM musicaAutor;
GO
--Quais cd(s) têm música
SELECT idCD
FROM cd
INTERSECT
SELECT idCD
FROM faixa;
GO
--Quais faixas têm música
SELECT idMusica
FROM faixa
INTERSECT
SELECT idMusica
FROM musica
GO

--Quais as gravadoras que não tem cd
SELECT idGravadora
FROM dbo.gravadora
EXCEPT
SELECT idGravadora
FROM cd;
--Quais os autores que não tem música
--(Inserir 3 autores novos)
INSERT INTO autor (idAutor, nmAutor)
VALUES (8, 'Roberto Carlos'),
	   (9, 'Chorão'),
	   (10, 'Player Tauz');
GO

SELECT idAutor
FROM autor
EXCEPT
SELECT idAutor
FROM musicaAutor;
GO
--Quais os cd(s) que não tem música
SELECT idCD
FROM cd
EXCEPT
SELECT idCD
FROM faixa;
--Quais as músicas que não tem autor
--(Inserir 3 musicas novas)
INSERT INTO musica(idMusica, nmMusica, duracao)
VALUES (31, 'Through the Fire and Flames', '00:05:05'),
	   (32, 'In the End', '00:03:38'),
	   (33, 'Numb', '00:03:07');
GO
SELECT idMusica
FROM musica
EXCEPT
SELECT idMusica
FROM musicaAutor

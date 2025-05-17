INSERT INTO autor
VALUES	(1, 'Renato Russo'),
		(2, 'Tom Jobim'),
		(3, 'Chico Buarque'),
		(4, 'Dado Vila-Lobos'),
		(5, 'Marcelo Bonfá'),
		(6, 'Ico Ouro Preto'),
		(7, 'Vinícius de Moraes');
go

INSERT INTO musica
VALUES (1, 'Será', '00:02:28'),
		(2, 'Ainda é Cedo', '00:03:55'),
		(3, 'Geração Coca-Cola', '00:02:20'),
		(4, 'Eduardo e Mônica', '00:04:32'),
		(5, 'Tempo Perdido', '00:05:00'),
		(6, 'Índios', '00:04:23'),
		(7, 'Que País é Este', '00:03:04'),
		(8, 'Faroeste Caboclo', '00:09:03'),
		(9, 'Há Tempos', '00:03:16'),
		(10, 'Pais e Filhos', '00:05:06'),
		(11, 'Meninos e Meninas', '00:03:22'),
		(12, 'Vento no Litoral', '00:06:05'),
		(13, 'Perfeição', '00:04:35'),
		(14, 'Giz', '00:03:20'),
		(15, 'Dezesseis', '00:05:28'),
		(16, 'Antes das Seis', '00:03:09'),
		(17, 'Meninos, Eu Vi', '00:03:25'),
		(18, 'Eu Te Amo', '00:03:06'),
		(19, 'Piano na Mangueira', '00:02:23'),
		(20, 'A Violeira', '00:02:54'),
		(21, 'Anos Dourados', '00:02:56'),
		(22, 'Olha Maria', '00:03:55'),
		(23, 'Biscate', '00:03:20'),
		(24, 'Retrato em Preto e Branco', '00:03:03'),
		(25, 'Falando de Amor', '00:03:20'),
		(26, 'Pois é', '00:02:48'),
		(27, 'Noite dos Mascarados', '00:02:42'),
		(28, 'Sabiá', '00:03:20'),
		(29, 'Imagina', '00:02:52'),
		(30, 'Bate-Boca', '00:04:41');
go

INSERT INTO musicaAutor
VALUES (1,1), (1,4), (1,5),
		(2,1), (2,4),(2,5),(2,6), 
		(3,1), 
		(4,1), 
		(5,1), 
		(6,1), 
		(7,1), 
		(8,1), 
		(9,1), (9,4),
		(10,1), (10,4), (10,5),
		(11,1), (11,4), (11,5),
		(12,1), (12,4), (12,5),
		(13,1), (13,4), (13,5),
		(14,1), (14,4), (14,5),
		(15,1), (15,4), (15,5),
		(16,1), (16,4), (16,5),
		(17,2), (17,3), 
		(18,2), (18,3), 
		(19,2), (19,3), 
		(20,2), (20,3), 
		(21,2), (21,3), 
		(22,2), (22,3), (22,7),
		(23,2), 
		(24,2), (24,3), 
		(25,2), 
		(26,2), (26,3), 
		(27,3), 
		(28,2), (28,3), 
		(29,2), (29,3), 
		(30,3);
go

INSERT INTO gravadora
VALUES (1, 'EMI', 'Rod. Dutra, km. 29,8', 1155659856, 1198657894, 'emi@emi-music,com.br'),
		(2, 'Polygram', 'Rod. Imigrantes, km. 29,8', 11999659856, 11975957894, 'polygram@music,com.br'),
		(3, 'BMG', 'Rod. Anchieta, km. 289,3', 11999654456, 11975957004, 'bmg@music,com.br'),
		(4, 'Som Livre', 'Av. São José, km. 289,3', 11999657806, 11978957004, 'somlivre@music,com.br'),
		(5, 'EPIC', 'Av. Alda, 89', 11958793321, 11989654789, 'epic@music,com.br');
go

INSERT INTO cd
VALUES (1, 1, 'Mais do Mesmo', 5.00, '1985-02-03', 1),
(2, 3, 'Bate Boca', 15.00, '1999-08-07', 2),
(3, 4, 'Elis Regina - Essa Mulher', 18.00, '1986-05-25', 3),
(4, 3, 'A força que nunca seca', 5.25, '1981-07-15', 4),
(5, 4, 'Perfil', 20.99, '1987-01-02', 5),
(6, 2, 'Barry Manilow Greastest Hits', 25.00, '1958-12-18', 1),
(7, 5, 'Listen Without Prejudice', 28.00, '1975-06-11', 7);
go

INSERT INTO faixa (idCD, nroFaixa, idMusica)
VALUES(1, 1, 1),
(1, 2, 2),
(1, 3, 3),
(1, 4, 4),
(1, 5, 5),
(1, 6, 6),
(1, 7, 7),
(1, 8, 8),
(1, 9, 9),
(1, 10, 10),
(1, 11, 11),
(1, 12, 12),
(1, 13, 13),
(1, 14, 14),
(1, 15, 15),
(1, 16, 16),
(2, 1, 17),
(2, 2, 18),
(2, 3, 19),
(2, 4, 20),
(2, 5, 21),
(2, 6, 22),
(2, 7, 23),
(2, 8, 24),
(2, 9, 25),
(2, 10, 26),
(2, 11, 27),
(2, 12, 28),
(2, 13, 29),
(2, 14, 30);
go

INSERT INTO cdCategoria
VALUES(1, 10, 20),
(2, 20, 40),
(3, 30, 60),
(4, 11, 22),
(5, 15, 30),
(6, 25, 50),
(7, 21, 42),
(8, 22, 44),
(9, 9, 18),
(10, 5, 10);
go
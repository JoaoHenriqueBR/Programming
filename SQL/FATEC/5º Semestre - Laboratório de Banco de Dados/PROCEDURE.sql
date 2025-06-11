/* Cria uma procedure, semelhante a uma função em outras linguagens */
CREATE procedure sp_saudacao as 
	DECLARE @msg VARCHAR(11)
	SET @msg = 'Olá, Mundo!'
	print @msg
GO

EXEC sp_saudacao;
GO

/* Altera a procedure, deve ser executado separadamente */
ALTER procedure sp_saudacao as 
	DECLARE @msg VARCHAR(12)
	SET @msg = 'Hello world!'
	print @msg
GO

EXEC sp_saudacao;
GO

/* Sem parâmetros */
CREATE PROCEDURE sp_soma AS
	-- Declaração de variáveis
	DECLARE @num1 INT
	DECLARE @num2 INT
	DECLARE @result INT

	-- Entrada de valores constantes
	SET @num1 = 365
	SET @num2 = 350

	-- Processamento
	SET  @result = @num1 + @num2

	-- Saída
	PRINT @result;
GO

EXEC sp_soma;
GO

/* Com parâmetros */
ALTER PROCEDURE sp_soma @num1 INT, @num2 INT AS
	-- Declaração de variáveis
	DECLARE @result INT

	-- Processamento
	SET  @result = @num1 + @num2

	-- Saída
	PRINT @result;
GO

EXEC sp_soma 130,124;
GO

/* Passagem de parâmetros (entrada e saída) */
ALTER PROCEDURE sp_soma
						-- Parâmetro de entrada
						@num1 INT, 
						@num2 INT,
						-- Parâmetro de saída
						@result INT OUTPUT
AS

	-- Processamento
	SET  @result = @num1 + @num2;
GO

DECLARE @res INT
EXEC sp_soma 123, 321, @res OUTPUT
PRINT @res;
GO

SELECT nmcd, ABS(precoVenda)preco,
CASE
	WHEN ABS(precoVenda) > 13
		THEN ABS(precoVenda) * 0.9
	WHEN ABS(precoVenda) BETWEEN 10 and 13
		THEN ABS(precoVenda) * 0.8
	ELSE ABS(precoVenda) * 0.7
END VENDA
FROM cd;
GO

UPDATE cd
SET precoVenda =
CASE
	WHEN ABS(precoVenda) > 13
		THEN ABS(precoVenda) * 0.9
	WHEN ABS(precoVenda) BETWEEN 10 and 13
		THEN ABS(precoVenda) * 0.8
	ELSE ABS(precoVenda) * 0.7
END;
GO

SELECT nmCD,
	CASE idGravadora
		WHEN 1 THEN 'EMI'
		WHEN 2 THEN 'BMG'
		WHEN 3 THEN 'SOM LIVRE'
		ELSE 'SONY MUSIC'
	END nmGravadora
FROM cd;
GO

SELECT *
FROM cd;
GO

/* Procedure para DML/DQL */
CREATE PROCEDURE sp_InsereMusica2025
					@cod INT,
					@nome VARCHAR(50),
					@tempo TIME
AS
INSERT INTO musica (idMusica, nmMusica, duracao)
VALUES (@cod, @nome, @tempo);
GO

EXEC sp_InsereMusica2025 31, 'Hino Fatec ZS', '00:02:00';
GO

SELECT *
FROM musica;
GO

CREATE PROCEDURE sp_alteraMusica
					@cod INT,
					@nome VARCHAR(50),
					@tempo TIME
AS
UPDATE musica
SET nmMusica = @nome, duracao = @tempo
WHERE idMusica = @cod;
GO

EXEC sp_alteraMusica 31, 'Hino do São Paulo FC', '00:01:54';
GO

SELECT *
FROM musica;
GO

CREATE PROCEDURE sp_excluiMusica
					@cod INT
AS
DELETE FROM musica
WHERE idMusica = @cod;
GO

EXEC sp_excluiMusica 31;
GO

SELECT *
FROM musica;
GO

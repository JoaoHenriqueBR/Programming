-- Aula 01/04
-- Struct

/*
 O que é? - Tipo de dado em SQL que representa 
 uma coleção de elementos, onde cada elemento 
 pode ser de um tipo de dado diferente.
*/

/*
 Funções de Data e Hora 
 - DAY()
 - MONTH()
 - YEAR()
 - DATEPART(parte, data)
 - DATEADD(parte, valor, data)
 - DATEDIFF(parte, data_inicial, data_final)
 - GETDATE()
 *obs: pode ser : DAY, MONTH, YEAR,
  QUARTER, DAYOFYEAR,
  WEEKDAY, WEEK, HOUR,
  MINUTE, SECOND
*/

-- Exemplo com DAY - MONTH - YEAR


SELECT DAY(dtLancto) as Dia,
       MONTH(dtLancto) as Mês,
       YEAR(dtLancto) as Ano,
       dtLancto
FROM cd;
GO

-- Exemplo com DATEPART

SELECT DATEPART(QUARTER, dtLancto) as Trimestre,
       DATEPART(WEEK, dtLancto) as Semana,
       DATEPART(WEEKDAY, dtLancto) as Dia_da_Semana,
       DATEPART(DAYOFYEAR, dtLancto) as Dia_do_Ano,
       DATEPART(HOUR, dtLancto) as Hora,
       DATEPART(MINUTE, dtLancto) as Minuto,
       DATEPART(SECOND, dtLancto) as Segundo,
       DATEPART(MILLISECOND, dtLancto) as Millesegundo
FROM cd;

DECLARE @DataNasc SMALLDATETIME = '2004-11-16';
DECLARE @Hoje DATE = GETDATE();

-- Exercicio: Quantos anos, meses e dias você têm;
SELECT DATEDIFF(YEAR, @DataNasc, @Hoje) as Anos_de_vida;

SELECT DATEDIFF(MONTH, @DataNasc, @Hoje) AS Meses_de_vida;

SELECT DATEDIFF(DAY, @DataNasc, @Hoje) AS Dias_de_vida;

SELECT DATEPART(WEEKDAY, @DataNasc) as Dia_da_Semana,
       DATEPART(DAYOFYEAR, @DataNasc) as Dia_do_Ano;


/* Manipulação de String */

SELECT	LOWER(nmGravadora) as Nome,
		UPPER(email) as URL,
		endereco
FROM gravadora
WHERE	UPPER(LEFT(endereco,3)) = 'ROD' and
		LOWER(RIGHT(email,2)) = 'br';
go

SELECT  ASCII('j') as 'J', ASCII('o') as O, ASCII('ã') as Ã, ASCII('o') as O,
		SUM(ASCII('j') + ASCII('o') + ASCII('ã') + ASCII('o')) as Total;
go
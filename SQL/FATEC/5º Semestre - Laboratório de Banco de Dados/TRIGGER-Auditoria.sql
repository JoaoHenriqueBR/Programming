-- Criar tabela "Espiã"
CREATE TABLE auditoria(
idAuditoria INT NOT NULL PRIMARY KEY IDENTITY(1,1),
usuario VARCHAR(100) NOT NULL,
acao VARCHAR(20) NOT NULL,
data DATETIME NOT NULL,
tabela VARCHAR(15) NOT NULL,
codigo INT NOT NULL
);
GO

-- Criar trigger para inserir música
CREATE TRIGGER tr_auditaInsereMusica
ON musica FOR INSERT AS
INSERT INTO auditoria (usuario, acao, data, tabela, codigo)
SELECT SUSER_SNAME(),
	   'Cadastrou',
	   GETDATE(),
	   'dbo.musica',
	   idMusica
FROM inserted;
GO

SELECT *
FROM musica;
GO

EXEC sp_InsereMusica20251 42, 'Hino do S�o Paulo', '0:02:20';
GO

EXEC sp_InsereMusica20251 43, 'In the End', '00:03:39';
GO

EXEC sp_InsereMusica20251 44, 'Numb', '00:03:08';
GO

SELECT *
FROM auditoria;
GO

-- Criar trigger para alterar música
CREATE TRIGGER tr_auditaAlteraMusica
ON musica FOR UPDATE AS
INSERT INTO auditoria (usuario, acao, data, tabela, codigo)
SELECT SUSER_SNAME(),
	   'Alterou',
	   GETDATE(),
	   'dbo.musica',
	   idMusica
FROM inserted;
GO

EXEC sp_AlteraMusica20251 42, 'Hino do Brasil', '00:03:29';
GO

SELECT *
FROM musica;
GO

SELECT *
FROM auditoria;
GO

CREATE TRIGGER tr_auditaExcluirMusica
ON musica FOR DELETE AS
INSERT INTO auditoria (usuario, acao, data, tabela, codigo)
SELECT SUSER_NAME(),
	   'Excluiu',
	   GETDATE(),
	   'dbo.musica',
	   idMusica
FROM deleted;
GO

EXEC sp_ExcluirMusica20251 44;
GO
EXEC sp_ExcluirMusica20251 43;
GO
EXEC sp_ExcluirMusica20251 42;
GO

SELECT * FROM musica;
GO

SELECT * FROM auditoria;
GO
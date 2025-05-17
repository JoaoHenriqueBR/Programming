/*
CREATE DATABASE cdFatecManha20251;
go
USE cdFatecManha20251;
go
*/

CREATE TABLE autor(
idAutor INT NOT NULL PRIMARY KEY,
nmAutor VARCHAR(50) NOT NULL
);
GO

CREATE TABLE musica(
idMusica INT NOT NULL PRIMARY KEY,
nmMusica VARCHAR(50) NOT NULL,
duracao TIME(6) NOT NULL 
);
GO

CREATE TABLE musicaAutor(
idMusica INT NOT NULL,
idAutor INT NOT NULL,
FOREIGN KEY(idMusica) REFERENCES musica (idMusica),
FOREIGN KEY(idAutor) REFERENCES autor (idAutor)
);
GO

CREATE TABLE gravadora(
idGravadora INT NOT NULL PRIMARY KEY,
nmGravadora VARCHAR(50) NOT NULL,
endereco VARCHAR(100) NULL,
tel NUMERIC(11,0) NOT NULL,
direto NUMERIC(11,0) NULL,
email VARCHAR(80) NOT NULL
);
GO

CREATE TABLE cd(
idCD INT NOT NULL PRIMARY KEY,
idGravadora INT NOT NULL,
nmCD VARCHAR(50) NOT NULL,
precoVenda DECIMAL(5,2) NOT NULL,
dtLancto SMALLDATETIME NOT NULL,
cdIndicado INT NOT NULL,
FOREIGN KEY(idGravadora) REFERENCES gravadora(idGravadora),
FOREIGN KEY(cdIndicado) REFERENCES cd(idCD)
);
GO

CREATE TABLE faixa(
idCD INT NOT NULL,
idMusica INT NOT NULL,
nroFaixa INT NOT NULL,
PRIMARY KEY(idCD, nroFaixa),
FOREIGN KEY(idCD) REFERENCES cd(idCD),
FOREIGN KEY(idMusica) REFERENCES musica(idMusica)
);
GO

CREATE TABLE itemCd(
idCD INT NOT NULL,
idMusica INT NOT NULL,
nroFaixa INT NOT NULL,
FOREIGN KEY(idMusica) REFERENCES musica(idMusica),
FOREIGN KEY(idCD, nroFaixa) REFERENCES faixa (idCD, nroFaixa)
);
GO

CREATE TABLE cdCategoria(
idCategoria INT NOT NULL PRIMARY KEY,
menorPreco DECIMAL(4,2) NOT NULL,
maiorPreco DECIMAL(5,2) NOT NULL
);
GO

DROP TABLE itemCd;
go

/*
ALTER TABLE faixa 
DROP CONSTRAINT nroFaixa <criptografia da chave primária>;
go
*/
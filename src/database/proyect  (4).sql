CREATE TABLE Usuario (
  id_user serial NOT NULL PRIMARY KEY,
  nombre varchar(25),
  apellido varchar(25),
  foto varchar ,
  comtrasea varchar(200),
  correo varchar(60),
  id_comunidad integer
);

CREATE TABLE Foto (
  id_foto serial NOT NULL PRIMARY KEY,
  titulo varchar(50),
  descripcion varchar(200),
  imagen varchar,
  id_categoria integer,
  id_user serial
);

CREATE TABLE Comunidad (
  id_comunidad serial PRIMARY KEY,
  nombre varchar(25),
  foto varchar
);

CREATE TABLE Categoria (
  id_categoria integer  PRIMARY KEY,
  nombre varchar(25)
);

CREATE TABLE Comentario (
  id_comentario serial  PRIMARY KEY,
  texto char(500),
  id_user serial,
  id_foto serial
);



ALTER TABLE Usuario ADD CONSTRAINT FK_comunidad FOREIGN KEY (id_comunidad) REFERENCES Comunidad (id_comunidad);
ALTER TABLE foto ADD CONSTRAINT FK_foto FOREIGN KEY (id_user) REFERENCES usuario (id_user);
ALTER TABLE Foto ADD CONSTRAINT FK_categoria FOREIGN KEY (id_categoria) REFERENCES Categoria (id_categoria);

ALTER TABLE Comentario ADD CONSTRAINT FK_user_comentario FOREIGN KEY (id_user) REFERENCES Usuario (id_user);

ALTER TABLE Comentario ADD CONSTRAINT FK_foto_comentario FOREIGN KEY (id_foto) REFERENCES Foto (id_foto);
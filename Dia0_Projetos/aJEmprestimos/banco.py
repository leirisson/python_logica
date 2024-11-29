import sqlite3
connection = sqlite3.connect("Dia0_Projetos/aJEmprestimos/ajEMprestimos.db")  
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
   id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS credenciais_usuario (
    id_credencial INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS endereco (
     id_endereco INT AUTO_INCREMENT PRIMARY KEY,
    rua VARCHAR(255) NOT NULL,
    numero VARCHAR(10),
    complemento VARCHAR(255),
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(10) NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario_endereco (
    id_usuario_endereco INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_endereco INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tipo_emprestimo (
    id_tipo INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS emprestimo  (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_tipo INT NOT NULL,
    valor_emprestimo DECIMAL(10, 2) NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_pagamento DATE NOT NULL,
    juros DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_tipo) REFERENCES tipo_emprestimo(id_tipo)
)
""")


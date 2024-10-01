CREATE DATABASE IF NOT EXISTS manifestacoes_db;
USE manifestacoes_db;

CREATE TABLE IF NOT EXISTS manifestacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    tipo ENUM('reclamação', 'elogio', 'sugestão') NOT NULL,
    descricao TEXT NOT NULL,
    data DATETIME NOT NULL
);
CREATE TABLE IF NOT EXISTS analise_documento (
 id_analise INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
 id_usuario INT NOT NULL,
 nome_arquivo VARCHAR(255) NOT NULL,
 tamanho_bytes INT NOT NULL,
 classificacao VARCHAR(100) NOT NULL,
 score_suspeita FLOAT NULL,
 resultado JSON NOT NULL,
 data_analise DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 INDEX idx_analise_usuario_data (id_usuario, data_analise),
 CONSTRAINT fk_analise_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

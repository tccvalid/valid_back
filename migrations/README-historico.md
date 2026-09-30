# Histórico de análises

1. Faça backup do banco de dados.
2. No phpMyAdmin, selecione o banco configurado no `.env` e execute `migrations/criar_tabela_analise.sql` **uma única vez**.
3. Inicie o FastAPI como de costume; os endpoints autenticados estarão em `/analises/`, `/analises/estatisticas` e `/analises/{id}`.
4. Inicie também o Flask OCR (porta 5000) e o front-end Vite. O front-end precisa do token de login para salvar cada nova análise.

O histórico começa vazio; análises antigas não são recuperadas automaticamente. Apenas os resultados JSON são armazenados, não os arquivos enviados nem os PDFs. A média exibida é de **pontuação de suspeita**, não de autenticidade.

As alterações foram publicadas em `feature/historico-analises` para revisão antes da integração na `main`.
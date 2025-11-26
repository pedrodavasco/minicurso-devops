# 1. Imagem base: Python leve (slim) para economizar espaço
FROM python:3.12-alpine

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia apenas o arquivo de dependências primeiro (para usar cache do Docker)
COPY requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o restante do código para dentro do container
COPY . .

# 6. Expõe a porta que o FastAPI usa
EXPOSE 8000

# 7. Comando para rodar a aplicação quando o container iniciar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
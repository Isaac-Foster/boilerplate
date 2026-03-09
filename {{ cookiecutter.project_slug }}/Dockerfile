# apenas um modelo editar conforme a necessidade do projeto

FROM python:3.12-slim

WORKDIR /app

# Logs em tempo real no terminal do Docker (sem buffer)
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PATH="/app/.venv/bin:${PATH}"

# Instala uv (curl só para bootstrap, depois removido)
RUN apt update && apt install -y --no-install-recommends curl \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && apt purge -y curl && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# uv (binário da imagem oficial)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# 1) Copia manifests (camada cacheável)
COPY pyproject.toml uv.lock ./

# 2) Instala deps a partir do lock (reprodutível)
RUN uv sync --frozen --no-dev --no-install-project

# Código 
COPY app ./app

COPY config ./config

EXPOSE 8000

CMD ["uv", "run", "task", "start"]
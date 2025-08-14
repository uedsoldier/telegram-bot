FROM python:3.13-slim

# Instala cron y dos2unix, elimina exim4
RUN apt-get update && apt-get install -y cron dos2unix --no-install-recommends &&\
    apt-get remove -y exim4 exim4-base && \
    apt-get clean && apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Establece directorio de trabajo
WORKDIR /app

# Copia requirements y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto y convierte a LF (formato UNIX)
COPY . .

# Convierte todos los archivos en /app a formato UNIX
RUN find /app -type f -exec dos2unix {} \;

# Healthcheck docker
# HEALTHCHECK --interval=240m --timeout=10s --start-period=5s --retries=3 \
#   CMD python3 /app/src/telegtam_healthcheck.py || exit 1

# Corre script
CMD ["python3", "src/main.py"]

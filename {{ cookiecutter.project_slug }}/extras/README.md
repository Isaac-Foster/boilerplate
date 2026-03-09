#### Obs:

If you're going to use the new relic and don't want unnecessary logs from the /health route, include this to stop logging.

```python

# Não logar GET /health nos access logs do Uvicorn (ex.: health check a cada 30s)
class _HealthCheckFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        return "GET /health " not in msg and " /health HTTP" not in msg


logging.getLogger("uvicorn.access").addFilter(_HealthCheckFilter())
```
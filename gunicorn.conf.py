import multiprocessing

bind = "0.0.0.0:8000"         # Адрес и порт
workers = multiprocessing.cpu_count() * 2 + 1  # Кол-во воркеров
worker_class = "sync"         # Класс воркера (sync, gevent, etc)
timeout = 30                  # Таймаут соединения
graceful_timeout = 30         # Таймаут на завершение
keepalive = 2                 # Keep-alive для соединений
errorlog = "gunicorn-error.log"  # Лог ошибок
accesslog = "gunicorn-access.log"  # Лог запросов
loglevel = "info"             # Уровень логирования: debug/info/warning/error/critical
reload = False                # Перезагрузка при изменении кода (в dev-среде можно True)

# command: gunicorn core.wsgi:application --config gunicorn.conf.py
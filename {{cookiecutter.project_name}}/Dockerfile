# syntax = docker/dockerfile
FROM thuxit/upython:3.10-12 as production-stage
ARG APP_USER=www-data
# RUN \
#   apt-get update \
#   && DEPS=" \
#     libmagic1 \

#   " \
#   && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
#   && apt-get update && apt-get install -y --no-install-recommends $DEPS \
#   && rm -rf /var/lib/apt/lists/* 
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir  -r /requirements.txt

COPY . /code/
WORKDIR /code/

# uWSGI will listen on this port
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=config.settings
ENV ENV=dev
RUN DATABASE_URL='' \
	python /code/manage.py collectstatic --noinput --link \
  # && python /code/manage.py compilemessages \
  && python /code/manage.py check \
  && chown -R ${APP_USER} /code/config/settings \
  && mv uwsgi.ini /etc \
  && gzip --keep --best --force --recursive /code/static/


USER ${APP_USER}:${APP_USER}


# Uncomment after creating your docker-entrypoint.sh
#ENTRYPOINT ["/bin/bash"]

CMD ["uwsgi", "--ini=/etc/uwsgi.ini", "--show-config"]


from django.apps import AppConfig
# python manage.py startapp many_to_many
# many_to_many패키지를 models안으로 이동
# apps.py를 수정
# INSTALLED_APPS에 추가
# models.py작성


class ManyToManyConfig(AppConfig):
    name = 'models.many_to_many'

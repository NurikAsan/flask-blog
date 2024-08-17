from flask import Blueprint

from app.models import Permission

main = Blueprint('main')


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

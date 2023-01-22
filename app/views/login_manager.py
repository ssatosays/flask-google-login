from app import database as db
from app import login_manager
from models import User


@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized", 403


@login_manager.user_loader
def load_user(user_id):
    user = db.get_or_404(User, user_id)
    return user

from models import Log


def insert_log(db, comment, user_id):
    log = Log(comment=comment, user_id=user_id)
    db.session.add(log)
    db.session.commit()

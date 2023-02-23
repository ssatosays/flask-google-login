from models import Log


def insert_log(db, comment):
    log = Log(comment=comment)
    db.session.add(log)
    db.session.commit()

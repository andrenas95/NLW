import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "andrenasMundo@email.com"
    }

    emails_to_invite_repository.registry_email(email_trips_infos)



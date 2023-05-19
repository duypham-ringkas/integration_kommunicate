from sqlalchemy.orm import DeclarativeBase

from integration_kommunicate.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta

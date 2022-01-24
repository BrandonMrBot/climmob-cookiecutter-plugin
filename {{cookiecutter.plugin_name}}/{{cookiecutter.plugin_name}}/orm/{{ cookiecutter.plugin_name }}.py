from climmob.models.meta import Base
from climmob.models import User

from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    ForeignKey,
    INTEGER,
    Unicode,
)

from sqlalchemy.dialects.mysql import MEDIUMTEXT


class ExampleTable(Base):
    __tablename__ = "{{ cookiecutter.plugin_name }}_example"

    example_id = Column(Unicode(64), primary_key=True)
    example_name = Column(Unicode(120))
    example_desc = Column(MEDIUMTEXT(collation="utf8mb4_unicode_ci"))
    example_type = Column(INTEGER)
    example_url = Column(MEDIUMTEXT(collation="utf8mb4_unicode_ci"))
    example_file = Column(Unicode(64))
    example_mimetype = Column(Unicode(120))
    example_owner = Column(ForeignKey("user.user_name"), nullable=False, index=True)
    extras = Column(MEDIUMTEXT(collation="utf8mb4_unicode_ci"))
    tags = Column(MEDIUMTEXT(collation="utf8mb4_unicode_ci"))

    fsuser = relationship("User")

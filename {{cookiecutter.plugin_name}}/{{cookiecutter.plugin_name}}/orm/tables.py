from sqlalchemy import (
    Column,
    ForeignKey,
    INTEGER,
    Unicode,
    String,
    Table,
)

from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import mapper


class ExampleTable(object):
    def __init__(self, *args, **kw):
        pass


def add_{{ cookiecutter.plugin_name }}_tables(metadata):
    """
    This function should be called by a plugin implementing IDatabase using:
        def update_orm(self, metadata):
            add_{{ cookiecutter.plugin_name }}_tables(metadata)
    """
    t_example_item = Table(
        "{{ cookiecutter.plugin_name }}_example",
        metadata,
        Column("example_id", String(64), primary_key=True),
        Column("example_name", Unicode(120)),
        Column("example_desc", MEDIUMTEXT(collation="utf8mb4_unicode_ci")),
        Column("example_type", INTEGER),
        Column("example_url", MEDIUMTEXT(collation="utf8mb4_unicode_ci")),
        Column("example_file", String(64)),
        Column("example_mimetype", String(120)),
        Column("example_user", ForeignKey("user.user_name"), nullable=False, index=True),
        Column("extras", MEDIUMTEXT(collation="utf8mb4_unicode_ci")),
        Column("tags", MEDIUMTEXT(collation="utf8mb4_unicode_ci")),
        mysql_charset="utf8mb4",
        mysql_engine="InnoDB",
        mysql_collate="utf8mb4_unicode_ci",
    )

    mapper(ExampleTable, t_example_item)
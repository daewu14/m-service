"""Create table users

Revision ID: 834aca5b7697
Revises: a1c3953de2ac
Create Date: 2025-02-09 22:39:35.901109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from migrations import utils


# revision identifiers, used by Alembic.
revision: str = '834aca5b7697'
down_revision: Union[str, None] = 'a1c3953de2ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    columns = (
        sa.Column("id", sa.Integer(), nullable=False, index=True, autoincrement=True, primary_key=True),
        sa.Column("uuid", sa.String(length=128), nullable=False),
        sa.Column("name", sa.String(length=32), nullable=True),
        sa.Column("email", sa.String(length=64), nullable=False),
    ) + utils.ColumnTimestamp(soft_delete=False)

    op.create_table("users", *columns)
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass

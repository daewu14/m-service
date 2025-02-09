"""create table users

Revision ID: a1c3953de2ac
Revises: 
Create Date: 2025-02-09 08:21:28.426935

"""
from typing import Sequence, Union, Tuple
from uuid import UUID

from alembic import op
import sqlalchemy as sa
from migrations import utils

# revision identifiers, used by Alembic.
revision: str = 'a1c3953de2ac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

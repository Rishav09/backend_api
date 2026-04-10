"""add content column to posts table

Revision ID: dd45d03f838e
Revises: e10f23f0a4b4
Create Date: 2026-04-10 16:59:31.611496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd45d03f838e'
down_revision: Union[str, Sequence[str], None] = 'e10f23f0a4b4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")

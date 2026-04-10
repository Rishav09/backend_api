"""create post table

Revision ID: e10f23f0a4b4
Revises: 
Create Date: 2026-04-08 21:54:56.104838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e10f23f0a4b4'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("title", sa.String, nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")

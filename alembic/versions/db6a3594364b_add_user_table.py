"""add user table

Revision ID: db6a3594364b
Revises: dd45d03f838e
Create Date: 2026-04-10 17:02:05.597987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db6a3594364b'
down_revision: Union[str, Sequence[str], None] = 'dd45d03f838e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
                    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                    sa.Column('email', sa.String, nullable=False, unique=True),
                    sa.Column('password', sa.String, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')

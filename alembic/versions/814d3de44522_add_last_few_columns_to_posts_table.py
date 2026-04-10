"""add last few columns to posts table

Revision ID: 814d3de44522
Revises: b6e2e20652b2
Create Date: 2026-04-10 17:19:18.508797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '814d3de44522'
down_revision: Union[str, Sequence[str], None] = 'b6e2e20652b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column(
        'published', sa.Boolean, server_default='TRUE', nullable=False
    ))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False
    ))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

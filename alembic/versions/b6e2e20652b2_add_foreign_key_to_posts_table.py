"""add foreign-key to posts table

Revision ID: b6e2e20652b2
Revises: db6a3594364b
Create Date: 2026-04-10 17:08:56.178548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6e2e20652b2'
down_revision: Union[str, Sequence[str], None] = 'db6a3594364b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk', table_name = 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')

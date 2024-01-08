"""add foreign-key to posts table

Revision ID: ef07a34df0b3
Revises: 6d9c5f8a78dd
Create Date: 2023-03-05 21:56:01.082336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef07a34df0b3'
down_revision = '6d9c5f8a78dd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.add_column('posts', 'owner_id ')
    pass

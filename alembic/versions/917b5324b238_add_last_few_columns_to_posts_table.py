"""add last few columns to posts table

Revision ID: 917b5324b238
Revises: ef07a34df0b3
Create Date: 2023-03-05 22:04:48.722042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '917b5324b238'
down_revision = 'ef07a34df0b3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False,
                                     server_default="True"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                     nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

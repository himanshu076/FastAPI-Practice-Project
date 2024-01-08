"""add content column to posts table

Revision ID: def7380934a9
Revises: 6db2a9105672
Create Date: 2023-03-05 21:37:22.443987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'def7380934a9'
down_revision = '6db2a9105672'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
    pass

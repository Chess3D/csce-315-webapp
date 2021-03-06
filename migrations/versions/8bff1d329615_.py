"""empty message

Revision ID: 8bff1d329615
Revises: 955e1b5b17c0
Create Date: 2021-04-24 21:50:48.862850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bff1d329615'
down_revision = '955e1b5b17c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournament', sa.Column('start_at', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tournament', 'start_at')
    # ### end Alembic commands ###

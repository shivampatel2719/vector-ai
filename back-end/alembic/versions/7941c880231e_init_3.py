"""init 3

Revision ID: 7941c880231e
Revises: 
Create Date: 2022-01-25 18:04:56.482699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7941c880231e'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('cards',
    sa.Column('id',sa.Integer,primary_key=True),
    sa.Column('title',sa.String,nullable=False),
    sa.Column('type',sa.String,nullable=False),
    sa.Column('position',sa.Integer,nullable=False))
    sa.Column('url',sa.String,nullable=False)


def downgrade():
    op.drop_table('cards')

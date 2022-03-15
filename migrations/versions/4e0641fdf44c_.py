"""empty message

Revision ID: 4e0641fdf44c
Revises: 
Create Date: 2022-03-14 16:16:34.043171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e0641fdf44c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('num_bed', sa.Integer(), nullable=True),
    sa.Column('num_bath', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('type', sa.String(length=80), nullable=True),
    sa.Column('desc', sa.String(length=300), nullable=True),
    sa.Column('filename', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
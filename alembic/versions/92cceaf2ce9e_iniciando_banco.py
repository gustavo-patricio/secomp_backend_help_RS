"""iniciando banco

Revision ID: 92cceaf2ce9e
Revises: 
Create Date: 2024-06-02 15:55:37.962429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92cceaf2ce9e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collectpoint',
    sa.Column('name_point', sa.String(), nullable=False),
    sa.Column('start_time', sa.String(), nullable=False),
    sa.Column('end_time', sa.String(), nullable=False),
    sa.Column('receiving_donations', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('address',
    sa.Column('street', sa.String(), nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('complement', sa.String(), nullable=False),
    sa.Column('collection_point_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['collection_point_id'], ['collectpoint.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('donationstoreceive',
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('items_type', sa.String(), nullable=False),
    sa.Column('collection_point_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['collection_point_id'], ['collectpoint.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('donationstoreceive')
    op.drop_table('address')
    op.drop_table('user')
    op.drop_table('collectpoint')
    # ### end Alembic commands ###

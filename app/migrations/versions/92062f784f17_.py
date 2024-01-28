"""empty message

Revision ID: 92062f784f17
Revises: 
Create Date: 2024-01-28 18:43:53.396061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92062f784f17'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('birthDay', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('score',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('korean', sa.Integer(), nullable=False),
    sa.Column('english', sa.Integer(), nullable=False),
    sa.Column('math', sa.Integer(), nullable=False),
    sa.Column('history', sa.Integer(), nullable=False),
    sa.Column('name_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['name_id'], ['person.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('score')
    op.drop_table('person')
    # ### end Alembic commands ###
"""16.10.2024 Add Options

Revision ID: 41b9d1807c9e
Revises: be97cd7bc429
Create Date: 2024-10-16 15:04:37.094120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41b9d1807c9e'
down_revision: Union[str, None] = 'be97cd7bc429'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quanti', sa.String(), nullable=False),
    sa.Column('figi', sa.String(), nullable=False),
    sa.Column('instrumental_type', sa.String(), nullable=True),
    sa.Column('date', sa.TIMESTAMP(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operations')
    # ### end Alembic commands ###

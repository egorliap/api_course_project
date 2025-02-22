"""Deleted 'is_user' field from users table

Revision ID: 49f170ef258f
Revises: b3a64cf7f601
Create Date: 2024-11-03 03:26:07.609940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49f170ef258f'
down_revision: Union[str, None] = 'b3a64cf7f601'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_user', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False))
    # ### end Alembic commands ###

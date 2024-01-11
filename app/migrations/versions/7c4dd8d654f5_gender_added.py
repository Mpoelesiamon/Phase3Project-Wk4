"""Gender added

Revision ID: 7c4dd8d654f5
Revises: 93804be97f89
Create Date: 2024-01-11 12:47:59.381312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c4dd8d654f5'
down_revision: Union[str, None] = '93804be97f89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('gender', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'gender')
    # ### end Alembic commands ###
"""added User.confirmed

Revision ID: 001adcdb7624
Revises: 9b8556523492
Create Date: 2020-03-07 15:57:17.734537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001adcdb7624'
down_revision = '9b8556523492'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
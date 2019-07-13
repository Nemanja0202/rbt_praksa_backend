"""empty message

Revision ID: fd460bbf9990
Revises: 5689970c125c
Create Date: 2019-07-09 15:52:37.247175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd460bbf9990'
down_revision = '5689970c125c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('measurments', sa.Column('time_stamp', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('measurments', 'time_stamp')
    # ### end Alembic commands ###

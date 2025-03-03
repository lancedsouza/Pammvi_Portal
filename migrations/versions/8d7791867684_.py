"""empty message

Revision ID: 8d7791867684
Revises: 3115f25bc0cb
Create Date: 2024-03-20 15:39:21.022689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d7791867684'
down_revision = '3115f25bc0cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order', schema=None) as batch_op:
        batch_op.drop_column('total')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total', sa.FLOAT(), nullable=False))

    # ### end Alembic commands ###

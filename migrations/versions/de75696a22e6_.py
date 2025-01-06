"""empty message

Revision ID: de75696a22e6
Revises: 28837cb95fff
Create Date: 2024-02-26 18:20:30.971390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de75696a22e6'
down_revision = '28837cb95fff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_column('date')

    with op.batch_alter_table('purchase_order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order', schema=None) as batch_op:
        batch_op.drop_column('date')

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DATE(), nullable=True))

    # ### end Alembic commands ###

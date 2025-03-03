"""empty message

Revision ID: aa506f072fad
Revises: a428860dd984
Create Date: 2024-02-26 15:43:06.589019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa506f072fad'
down_revision = 'a428860dd984'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('color', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('power', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('label', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('packing', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('supplier_name', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('supplier_address', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('purchase_order', schema=None) as batch_op:
        batch_op.drop_column('supplier_address')
        batch_op.drop_column('supplier_name')
        batch_op.drop_column('packing')
        batch_op.drop_column('label')
        batch_op.drop_column('power')
        batch_op.drop_column('color')

    # ### end Alembic commands ###

"""Initial migration

Revision ID: f5cf34fa504b
Revises: 
Create Date: 2024-02-19 16:23:15.497000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5cf34fa504b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('supplier',
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('supplier_name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('country', sa.String(length=50), nullable=False),
    sa.Column('currency', sa.String(length=50), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('supplier_id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('product_name', sa.String(length=255), nullable=False),
    sa.Column('product_category', sa.String(length=50), nullable=False),
    sa.Column('product_vertical', sa.String(length=20), nullable=False),
    sa.Column('ean_code', sa.String(length=20), nullable=False),
    sa.Column('color', sa.String(length=20), nullable=False),
    sa.Column('power', sa.String(length=20), nullable=False),
    sa.Column('label', sa.String(length=20), nullable=False),
    sa.Column('packing', sa.String(length=20), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.Column('country', sa.String(length=50), nullable=False),
    sa.Column('currency', sa.String(length=50), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.supplier_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase_order',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('serial_number', sa.String(length=50), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Float(), nullable=False),
    sa.Column('net_price', sa.Float(), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.supplier_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('purchase_order')
    op.drop_table('products')
    op.drop_table('supplier')
    # ### end Alembic commands ###

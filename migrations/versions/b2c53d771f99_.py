"""empty message

Revision ID: b2c53d771f99
Revises: f58b97d08e01
Create Date: 2024-10-14 21:34:42.421448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2c53d771f99'
down_revision = 'f58b97d08e01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('maquina', schema=None) as batch_op:
        batch_op.alter_column('mensagemMax',
               existing_type=sa.TEXT(),
               type_=sa.JSON(),
               existing_nullable=True)
        batch_op.alter_column('mensagemMin',
               existing_type=sa.TEXT(),
               type_=sa.JSON(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('maquina', schema=None) as batch_op:
        batch_op.alter_column('mensagemMin',
               existing_type=sa.JSON(),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('mensagemMax',
               existing_type=sa.JSON(),
               type_=sa.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###
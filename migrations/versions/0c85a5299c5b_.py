"""empty message

Revision ID: 0c85a5299c5b
Revises: 6e807dbfe507
Create Date: 2021-01-15 15:15:40.810345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c85a5299c5b'
down_revision = '6e807dbfe507'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clientes', sa.Column('bairro', sa.String(length=40), nullable=True))
    op.add_column('clientes', sa.Column('cep', sa.String(length=40), nullable=True))
    op.add_column('clientes', sa.Column('cidade', sa.String(length=40), nullable=True))
    op.add_column('clientes', sa.Column('data_nascimento', sa.DateTime(), nullable=True))
    op.add_column('clientes', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('clientes', sa.Column('enedereco', sa.String(length=255), nullable=True))
    op.add_column('clientes', sa.Column('estado', sa.String(length=40), nullable=True))
    op.add_column('clientes', sa.Column('observacoes', sa.String(length=255), nullable=True))
    op.add_column('clientes', sa.Column('telefone', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clientes', 'telefone')
    op.drop_column('clientes', 'observacoes')
    op.drop_column('clientes', 'estado')
    op.drop_column('clientes', 'enedereco')
    op.drop_column('clientes', 'email')
    op.drop_column('clientes', 'data_nascimento')
    op.drop_column('clientes', 'cidade')
    op.drop_column('clientes', 'cep')
    op.drop_column('clientes', 'bairro')
    # ### end Alembic commands ###

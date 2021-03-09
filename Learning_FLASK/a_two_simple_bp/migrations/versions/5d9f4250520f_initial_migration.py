"""Initial migration.

Revision ID: 5d9f4250520f
Revises: 
Create Date: 2021-03-09 21:36:31.182025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d9f4250520f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('model', sa.Column('email', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_model_email'), 'model', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_model_email'), table_name='model')
    op.drop_column('model', 'email')
    # ### end Alembic commands ###
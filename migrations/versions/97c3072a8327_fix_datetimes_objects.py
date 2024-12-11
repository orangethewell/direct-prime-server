"""Fix datetimes objects

Revision ID: 97c3072a8327
Revises: a022d0e00921
Create Date: 2024-12-10 09:12:20.972085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97c3072a8327'
down_revision = 'a022d0e00921'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('deliveries', schema=None) as batch_op:
        batch_op.alter_column('receiving_company_user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('sessions', schema=None) as batch_op:
        batch_op.alter_column('last_logged_in',
               existing_type=sa.DATETIME(),
               nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=False)

    with op.batch_alter_table('sessions', schema=None) as batch_op:
        batch_op.alter_column('last_logged_in',
               existing_type=sa.DATETIME(),
               nullable=False)

    with op.batch_alter_table('deliveries', schema=None) as batch_op:
        batch_op.alter_column('receiving_company_user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
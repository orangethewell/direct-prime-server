"""initial migration

Revision ID: 3bad856f6e73
Revises: 
Create Date: 2024-12-11 14:43:44.820444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bad856f6e73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('Courier', 'Company', 'ServiceManager', name='userrole'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('profile_image', sa.String(length=255), nullable=True),
    sa.Column('main_operation_geocode', sa.JSON(), nullable=False),
    sa.Column('average_review_score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('cpf', name=op.f('uq_users_cpf')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email'))
    )
    op.create_table('bike_vehicles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.Enum('Motorbike', 'Bike', name='bikekind'), nullable=False),
    sa.Column('bike_plate', sa.String(length=12), nullable=True),
    sa.Column('bike_color', sa.String(length=255), nullable=False),
    sa.Column('bike_brand', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name=op.f('fk_bike_vehicles_owner_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bike_vehicles'))
    )
    op.create_table('company',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name=op.f('fk_company_owner_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_company'))
    )
    op.create_table('deliveries',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('courier_user_id', sa.Integer(), nullable=False),
    sa.Column('sending_company_user_id', sa.Integer(), nullable=False),
    sa.Column('receiving_company_user_id', sa.Integer(), nullable=True),
    sa.Column('sender_geocode', sa.JSON(), nullable=True),
    sa.Column('receiver_geocode', sa.JSON(), nullable=True),
    sa.Column('product_name', sa.String(length=255), nullable=False),
    sa.Column('product_image', sa.Text(), nullable=True),
    sa.Column('product_details', sa.Text(), nullable=True),
    sa.Column('status', sa.Enum('Pending', 'Assigned', 'OnCourse', 'Failed', 'Completed', name='deliverystatus'), nullable=False),
    sa.ForeignKeyConstraint(['courier_user_id'], ['users.id'], name=op.f('fk_deliveries_courier_user_id_users')),
    sa.ForeignKeyConstraint(['receiving_company_user_id'], ['users.id'], name=op.f('fk_deliveries_receiving_company_user_id_users')),
    sa.ForeignKeyConstraint(['sending_company_user_id'], ['users.id'], name=op.f('fk_deliveries_sending_company_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_deliveries'))
    )
    op.create_table('delivery_messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('delivery_id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('message_content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['delivery_id'], ['deliveries.id'], name=op.f('fk_delivery_messages_delivery_id_deliveries')),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], name=op.f('fk_delivery_messages_sender_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_delivery_messages'))
    )
    op.create_table('delivery_reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('delivery_id', sa.Integer(), nullable=False),
    sa.Column('company_score', sa.Float(), nullable=False),
    sa.Column('courier_score', sa.Float(), nullable=False),
    sa.Column('company_score_comment', sa.String(length=255), nullable=True),
    sa.Column('courier_score_comment', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['delivery_id'], ['deliveries.id'], name=op.f('fk_delivery_reviews_delivery_id_deliveries')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_delivery_reviews'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delivery_reviews')
    op.drop_table('delivery_messages')
    op.drop_table('deliveries')
    op.drop_table('company')
    op.drop_table('bike_vehicles')
    op.drop_table('users')
    # ### end Alembic commands ###

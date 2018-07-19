"""followers

Revision ID: 44509b9edda3
Revises: 2b36db9032a6
Create Date: 2018-07-19 10:52:41.935343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44509b9edda3'
down_revision = '2b36db9032a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###

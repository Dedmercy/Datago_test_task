"""add_transaction_table

Revision ID: a9bd73c59ffc
Revises: e900364a84cf
Create Date: 2023-06-15 16:54:09.307446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9bd73c59ffc'
down_revision = 'e900364a84cf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category', sa.Enum('products', 'restaurants', 'beauty', 'electronics', 'money_transfers', name='transactioncategory'), nullable=False),
    sa.Column('money', sa.Integer(), nullable=False),
    sa.Column('date', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['user_account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    # ### end Alembic commands ###
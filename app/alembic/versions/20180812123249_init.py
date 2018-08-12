"""init

Revision ID: afcf29db4572
Revises: 
Create Date: 2018-08-12 12:32:49.305663

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'afcf29db4572'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('timeseries',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('database_code', sa.String(length=120), nullable=False),
    sa.Column('dataset_code', sa.String(length=120), nullable=False),
    sa.Column('status', sa.String(length=120), nullable=False),
    sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timeseries')
    # ### end Alembic commands ###

"""init_files_table

Revision ID: 622990fafe69
Revises: 546ac6491dde
Create Date: 2019-05-10 20:49:23.580223

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '622990fafe69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
        op.create_table(
        'files',
        sa.Column('file_uuid', UUID, primary_key=True),
        sa.Column('dist', sa.String(1024), nullable=False),
        sa.Column('mimetype', sa.Unicode(50)),
    )


def downgrade():
    op.drop_table('files')

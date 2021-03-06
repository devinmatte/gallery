"""empty message

Revision ID: 915d41989da1
Revises: None
Create Date: 2016-11-17 23:17:34.057500

"""

# revision identifiers, used by Alembic.
revision = '915d41989da1'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('directories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent', sa.Integer(), nullable=True),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('date_uploaded', sa.DateTime(), nullable=False),
    sa.Column('author', sa.Text(), nullable=False),
    sa.Column('thumbnail_uuid', sa.Text(), nullable=False),
    sa.Column('blocked_groups', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['parent'], ['directories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('caption', sa.Text(), nullable=False),
    sa.Column('date_uploaded', sa.DateTime(), nullable=False),
    sa.Column('author', sa.Text(), nullable=False),
    sa.Column('thumbnail_uuid', sa.Text(), nullable=False),
    sa.Column('filetype', sa.Enum('Photo', 'Video', 'Text', name='filetype_enum'), nullable=False),
    sa.Column('exif_data', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['parent'], ['directories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    op.drop_table('directories')
    ### end Alembic commands ###

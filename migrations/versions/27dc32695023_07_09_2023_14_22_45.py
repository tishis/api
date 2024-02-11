"""07.09.2023-14:22:45

Revision ID: 27dc32695023
Revises: 1d8d00cfcff4
Create Date: 2023-09-07 14:22:53.314409

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '27dc32695023'
down_revision: Union[str, None] = '1d8d00cfcff4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag_m2m_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['images.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('image_id', 'tag_id', name='image_tag')
    )
    op.drop_table('image_m2m_tag')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_m2m_tag',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('image_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['images.id'], name='image_m2m_tag_image_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name='image_m2m_tag_tag_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='image_m2m_tag_pkey'),
    sa.UniqueConstraint('image_id', 'tag_id', name='image_tag')
    )
    op.drop_table('tag_m2m_image')
    # ### end Alembic commands ###

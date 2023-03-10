"""empty message

Revision ID: 1416284f5a1a
Revises: 
Create Date: 2023-02-09 18:04:49.020648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1416284f5a1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('attack', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.Column('imageUrl', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('moves', sa.String(), nullable=False),
    sa.Column('encounterRate', sa.Float(), nullable=True),
    sa.Column('catchRate', sa.Float(), nullable=True),
    sa.Column('captured', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('number')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('happiness', sa.Integer(), nullable=True),
    sa.Column('imageUrl', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('pokemonId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemonId'], ['pokemon.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('pokemontypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemontypes')
    op.drop_table('items')
    op.drop_table('pokemon')
    # ### end Alembic commands ###

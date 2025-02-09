import sqlalchemy as sa


def ColumnTimestamp(soft_delete: bool):
    columns = (
        sa.Column('created_at', sa.DateTime(), nullable=False, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(), nullable=False, default=sa.func.now())
    )
    if soft_delete:
        columns = columns + (sa.Column('deleted_at', sa.DateTime(), nullable=True))
    return columns

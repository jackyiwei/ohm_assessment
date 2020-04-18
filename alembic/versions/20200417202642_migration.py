"""migration

Revision ID: 58ad84802470
Revises: 00000000
Create Date: 2020-04-17 20:26:42.256000

"""

# revision identifiers, used by Alembic.
revision = '58ad84802470'
down_revision = '00000000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('''UPDATE user
    	SET point_balance=5000
    	WHERE user_id=1
	''')

	op.execute('''INSERT INTO rel_user
    	 VALUES
            (2, 'LOCATION', 'USA'),
	''')


	op.execute('''UPDATE user
    	SET tier='Silver'
    	WHERE user_id=3
	''')



def downgrade():
    op.execute('''UPDATE user
    	SET point_balance=1
    	WHERE user_id=1
	''')

	op.execute('''DELETE FROM rel_user
    	 WHERE user_id=2
	''')


	op.execute('''UPDATE user
    	SET tier='Carbon'
    	WHERE user_id=3
	''')

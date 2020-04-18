from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from models import _helpers
from models import User


@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    response = _helpers.db.session.execute('''
    	SELECT display_name, tier, point_balance FROM user
    	ORDER BY signup_date
    	DESC LIMIT 5
	''')

    users = [{'display_name': r[0], 'tier': r[1], 'point_balance': r[2]} for r in response]

    return render_template("community.html", users=users)



from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from app.main.test_lotto import lotto

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    _lotto_data = lotto()
    return render_template('/main/index.html', lotto_data=_lotto_data)
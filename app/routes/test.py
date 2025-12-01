from flask import Blueprint, render_template, request
from flask_login import login_required

test_bp = Blueprint('test', __name__, url_prefix='/test')

@test_bp.route('/dropdown')
@login_required
def test_dropdown():
    """Test dropdown functionality"""
    return render_template('test_dropdown.html')

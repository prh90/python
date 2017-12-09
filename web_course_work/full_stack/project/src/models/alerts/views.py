from flask import Blueprint

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    return "This is the alerts index"


@alert_blueprint.route('/new', methods=['POST'])
def create_alert():
    pass


@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert():
    pass


@alert_blueprint.route('/<string:alert_id>')
def get_alert_page():
    pass


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user():
    pass

from flask import Blueprint, render_template

from src.models.alerts.alert import Alert

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
def get_alert_page(alert_id):
    alert = Alert.find_by_id(alert_id)
    return render_template('alerts/alert.html', alert=alert)


@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user():
    pass

# controller/user_controller.py

from flask import Blueprint, request, jsonify
from service.user_service import UserService

account = Blueprint('account', __name__)
user_service = UserService()

@account.route('/', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new user via POST request.
    
    Example:
        Expected JSON format:
        {
            "username": "sampleuser",
            "name": "Sample User",
            "mail": "user@example.com",
            "notification_flag": true,
            "third_party_info": "optional_info"
        }

        Using curl to call endpoint:
            ```bash
            curl -i -X POST http://localhost:5000/api/account \
            -H "Content-Type: application/json" \
            -d '{
                "username": "albert123",
                "name": "albert123",
                "mail": "alber@example.com",
                "notification_flag": true,
                "third_party_info": "optional_info"
                }'
            ```

    Returns:
        JSON response with the created user details or an error message.
    """
    data = request.json
    try:
        user = user_service.create_user(
            username=data['username'],
            name=data['name'],
            mail=data['mail'],
            lock_session=data.get('lock_session'),
            notification_flag=data.get('notification_flag', True),
            third_party_info=data.get('third_party_info')
        )
        return jsonify(user_id=user.id, username=user.username), 201
    except KeyError as e:
        return jsonify(error=f"Missing parameter: {str(e)}"), 400
    except ValueError as e:
        return jsonify(error=str(e)), 409

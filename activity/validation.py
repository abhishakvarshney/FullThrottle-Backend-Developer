from voluptuous import Schema, Required, MultipleInvalid, Any


def validate_add_user(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('realname'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}


def validate_add_user_activity(request):
    """

    @param request:
    @return:
    """
    try:
        data = dict(request.data)
        schema = Schema({
            Required('user_id'): str,
        }, extra=True)
        schema(data)
        return True, {'status': True, 'statusCode': 'Success', 'statusMessage': 'Success', 'response': {}}
    except MultipleInvalid as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}
    except Exception as e:
        return False, {'status': False, 'statusCode': 'ValidationError', 'statusMessage': 'validationError',
                       'response': str(e)}

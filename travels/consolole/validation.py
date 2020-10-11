from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist, ValidationError



def key_alter(key_list):
    new_keylist = []
    for key in key_list:
        new_key = (key.replace("_", " ")).title()
        new_keylist.append(new_key)
    return new_keylist


def error_message(serializer):
    response = {}
    if isinstance(serializer.errors, list):
        invalid_parameter = (key_alter(list(serializer.errors[-1].keys())))
    else:
        invalid_parameter = (key_alter(list(serializer.errors.keys())))
    if len(invalid_parameter) == 1:
        response['message'] = "Following data is invalid or Missing! <br/> - {}".format(invalid_parameter[0])
    elif len(invalid_parameter) > 1:
        parameters = ""
        for value in invalid_parameter:
            parameters = parameters + ' - ' + value + ' <br/>'
        response['message'] = "Following data is invalid or Missing! <br/>{}".format(parameters)
    else:
        response['messsage'] = "Invalid Request"
    return Response(response)

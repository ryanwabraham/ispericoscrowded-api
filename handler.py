import json

import populartimes


def endpoint(event, context):
    api_key = "API_KEY"
    place_id = "ChIJERL3niVAjoARl8XPdDVqQ8U"
    keys = {
        "current_popularity",
        "populartimes",
        "time_wait",
        "time_spent"
    }
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        }
    }

    try:
        data = populartimes.get_id(api_key, place_id)
        response_body = {key: value for key, value in data.items() if key in keys}
        response["body"] = json.dumps(response_body)
    except:
        response["statusCode"] = 500

    return response

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "type": "string",
        "data": {
            "type": "object",
            "properties": {
                "createdAt": {"type": "string"},
                "updatedAt": {"type": "string"},
                "id": {"type": "number"},
                "email": {"type": "string"},
                "username": {"type": "string"},
                "roleId": {"type": "number"},
                "phone": {"type": "string"},
                "role": {
                    "type": "object",
                    "properties": {
                        "createdAt": {"type": "string"},
                        "updatedAt": {"type": "string"},
                        "id": {"type": "number"},
                        "name": {"type": "string"},
                        }},
                "deleted": {"type": "boolean"},
                "onShift": {"type": "boolean"},
                "image": {"type": "string"},
                    }},
      #  "required": ["data.id", "data.phone"],
    },
}

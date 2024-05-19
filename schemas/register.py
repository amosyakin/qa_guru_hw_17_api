post_register = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "additionalProperties": False,
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "token": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "token"
  ]
}

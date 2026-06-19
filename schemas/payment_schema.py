PAYMENT_SCHEMA = {


"type": "object",

"properties": {

    "payment_id": {
        "type": "integer"
    },

    "success": {
        "type": "boolean"
    }

},

"required": [

    "payment_id",

    "success"
]

}

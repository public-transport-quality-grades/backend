from flasgger import Schema, fields


class TimeIntervalSchema(Schema):
    time_description = fields.String(required=True)
    start = fields.Time(required=True)
    end = fields.Time(required=True)


class AvailableGradingSchema(Schema):
    id = fields.Integer(required=True)
    due_date = fields.Date(required=True)
    type_of_day = fields.String(required=True)
    time_interval = fields.Nested(TimeIntervalSchema, required=True)

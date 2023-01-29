from datetime import datetime
from marshmallow import Schema, fields


class PollingUnitSchema(Schema):
    polling_unit_id = fields.Integer(required=True)
    ward_id = fields.Integer()
    lga_id = fields.Integer(required=True)
    uniquewardid = fields.Integer()
    polling_unit_number = fields.String()
    polling_unit_name = fields.String()
    polling_unit_description = fields.String()
    lat = fields.String()
    long = fields.String()
    entered_by_user = fields.String(required=True)
    date_entered = fields.DateTime(load_default=datetime.now())


class PollingUnitResultsSchema(Schema):
    polling_unit_uniqueid = fields.String(required=True)
    party_abbreviation = fields.String(required=True)
    party_score = fields.Integer(required=True)
    entered_by_user = fields.String(required=True)
    date_entered = fields.DateTime(load_default=datetime.now())


class PUandResultsSchema(Schema):
    polling_unit = fields.Nested(PollingUnitSchema, required=True)
    polling_unit_results = fields.Nested(PollingUnitResultsSchema, many=True)

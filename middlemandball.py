from flask import Flask, request
from flask_restful import Resource, Api
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser
import redis

# create a connection to the localhost Redis server instance, by
# default it runs on port 6379
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

app = Flask(__name__)
api = Api(app)

class HW(Resource):
    def get(self):
        return {'Message': 'Hello world'}


class INSERT(Resource):
    args = {
        'table': fields.Str(
            required=True
            # validate=validate.OneOf(['baz', 'qux']),
        ),
        'key': fields.Str(required=True),
        # 'field' : fields.Str(required=True)

        'field0': fields.Str(required=True),
        'field1': fields.Str(required=True),
        'field2': fields.Str(required=True),
        'field3': fields.Str(required=True),
        'field4': fields.Str(required=True),
        'field5': fields.Str(required=True),
        'field6': fields.Str(required=True),
        'field7': fields.Str(required=True),
        'field8': fields.Str(required=True),
        'field9': fields.Str(required=True)

    }

    @use_kwargs(args)
    # def get(self, table, key,*args):
    # return {'Message':table, 'Message2':key,'Message3':field}
    def post(self, table, key, field0, field1, field2, field3, field4, field5, field6, field7, field8, field9):
        # If field0 is not None, then read key and field =from redis...
        redis_fields = {}
        if field0 is not None:
            redis_fields["field0"] = field0
        if field1 is not None:
            redis_fields["field1"] = field1
        if field2 is not None:
            redis_fields["field2"] = field2
        if field3 is not None:
            redis_fields["field3"] = field3
        if field4 is not None:
            redis_fields["field4"] = field4
        if field5 is not None:
            redis_fields["field5"] = field5
        if field6 is not None:
            redis_fields["field6"] = field6
        if field7 is not None:
            redis_fields["field7"] = field7
        if field8 is not None:
            redis_fields["field8"] = field8
        if field9 is not None:
            redis_fields["field9"] = field9
        redis_db.hmset(key, redis_fields)
        print("We're here...")
        return {'Message': table, 'Message2': key, 'Message3': redis_fields}


class READ(Resource):
    args = {
        'table': fields.Str(
            required=True
            # validate=validate.OneOf(['baz', 'qux']),
        ),
        'key': fields.Str(required=True),

        'field0': fields.Str(required=False),
        'field1': fields.Str(required=False),
        'field2': fields.Str(required=False),
        'field3': fields.Str(required=False),
        'field4': fields.Str(required=False),
        'field5': fields.Str(required=False),
        'field6': fields.Str(required=False),
        'field7': fields.Str(required=False),
        'field8': fields.Str(required=False),
        'field9': fields.Str(required=False)

    }

    @use_kwargs(args)
    def get(self, table, key, field0, field1, field2, field3, field4, field5, field6, field7, field8, field9):
        # If field0 is not None, then read key and field =from redis...
        redis_fields = {}
        if field0 is not None:
            redis_fields["field0"] = field0
        if field1 is not None:
            redis_fields["field1"] = field1
        if field2 is not None:
            redis_fields["field2"] = field2
        if field3 is not None:
            redis_fields["field3"] = field3
        if field4 is not None:
            redis_fields["field4"] = field4
        if field5 is not None:
            redis_fields["field5"] = field5
        if field6 is not None:
                redis_fields["field6"] = field6
        if field7 is not None:
            redis_fields["field7"] = field7
        if field8 is not None:
            redis_fields["field8"] = field8
        if field9 is not None:
            redis_fields["field9"] = field9
        return {'Message': redis_db.hgetall(key)}
        # return {'Message1': table,'Message2': key,'Message3': redis_fields}


class DELETE(Resource):
    args = {
        'table': fields.Str(
            required=True
            # validate=validate.OneOf(['baz', 'qux']),
        ),
        'key': fields.Str(required=True),

    }


    @use_kwargs(args)
    def get(self, table, key, *args):
        redis_db.hdel(table, key)
        return {'Message': table, 'Message2': key}


class UPDATE(Resource):
    args = {
        'table': fields.Str(
            required=True
            # validate=validate.OneOf(['baz', 'qux']),
        ),
        'key': fields.Str(required=True),

        'field': fields.Str(required=True)
    }

    @use_kwargs(args)
    def get(self, table, key, field):
        redis_db.hmset(keys,redis_fields)
        return {'Message': table}

class SCAN(Resource):
    args = {
        'table': fields.Str(
            required=True
            # validate=validate.OneOf(['baz', 'qux']),
        ),
        'key': fields.Str(required=True),

        'field': fields.Str(required=False)
    }

    @use_kwargs(args)
    def get(self, table, key, field):
        return {'Message': redis_db.hgetall(key)}

api.add_resource(HW, '/healthcheck')
api.add_resource(INSERT, '/insert')
api.add_resource(READ, '/read')
api.add_resource(DELETE, '/delete')
api.add_resource(UPDATE, '/update')
api.add_resource(SCAN, '/scan')

if __name__ == '__main__':
    app.run()

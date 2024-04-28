from functools import wraps
from flask import request, jsonify, abort
from databases import UserDatabase
import jwt
from config import jwt_key, algorithm

user_database = UserDatabase()


def token_required():
    def _token_required(f):
        @wraps(f)
        async def __token_required(*args, **kwargs):
            authorization_header = request.headers
            try:
                token = authorization_header["Authorization"].split(" ")[1]
            except:
                return (
                    jsonify({"message": "authorization header is missing or invalid"}),
                    401,
                )
            try:
                user = jwt.decode(token, jwt_key, algorithms=[algorithm])
            except jwt.exceptions.DecodeError:
                return (
                    jsonify({"message": "authorization token is invalid"}),
                    401,
                )
            else:
                if result := await user_database.get(
                    "login", username=user["username"], password=user["password"]
                ):
                    return await f(*args, **kwargs)
                return (
                    jsonify({"message": "authorization invalid"}),
                    401,
                )

        return __token_required

    return _token_required

from app.model.user import Users
from app import response,app
from flask import request
from app import db

import datetime

#@jwt_required # mengamankan Index/Method
def index():
    try:
        # print(get_jwt_identity())
        # user_token = get_jwt_identity()
        # print(user_token)
        # for key,value in user_token.items():
        #     print(f"{key} : {value}")

        users = Users.query.all()
        data  = transform(users)
        return response.ok(data,"Data user ditemukan..")
    except Exception as e:
        print(e)

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([],"Empty...")
        
        data = singleTransform(users)
        return response.ok(data,"Berhasil temukan data User")
    except Exception as e:
        print(e)
        
def store():
    try:
        full_name   = request.json['full_name']
        username    = request.json['username']
        email       = request.json['email']
        password    = request.json['password']
        role        = request.json['role']

        users = Users(full_name=full_name, username=username, email=email, role=role)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok('', 'Successfully create User!')
    except Exception as e:
        print(e)

# @jwt_required
def update(id):
    try:
        full_name   = request.json['full_name']
        username    = request.json['username']
        email       = request.json['email']
        password    = request.json['password']
        role        = request.json['role']

        user            = Users.query.filter_by(id=id).first()
        user.email      = email
        user.username   = username
        user.full_name  = full_name
        user.role       = role
        user.setPassword(password)

        db.session.commit()

        return response.ok('','Successfully update Userr!')
    except Exception as e:
        print(e)

# @jwt_required
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([],"Empty....")
        
        db.session.delete(user)
        db.session.commit()

        return response.ok('','Successfully delete User!')
    except Exception as e:
        print(e)
        
def transform(users):
    array = []
    for i in users:
        array.append(singleTransform(i))
    return array

def singleTransform(users):
    data = {
        'id'   : users.id,
        'full_name' : users.full_name,
        'username' : users.username,
        'email': users.email,
        'role': users.role
    }

    return data


# def login():
#     try:
#         email = request.json['email']
#         password = request.json['password']

#         user = Users.query.filter_by(email=email).first()
#         if not user:
#             return response.badRequest([], 'Empty....')

#         if not user.checkPassword(password):
#             return response.badRequest([], 'Your credentials is invalid')

#         data = singleTransform(user, withProdi=False)
#         expires = datetime.timedelta(days=1)
#         expires_refresh = datetime.timedelta(days=3)
#         access_token = create_access_token(data, fresh=True, expires_delta=expires)
#         refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

#         return response.ok({
#             "data": data,
#             "token_access": access_token,
#             "token_refresh": refresh_token,
#         }, "")

#     except Exception as e:
#         print(e)

# @jwt_refresh_token_required
# def refresh():
#     try:
#         user = get_jwt_identity()
#         new_token = create_access_token(identity=user, fresh=False)

#         return response.ok({
#             "token_access": new_token
#         }, "")

#     except Exception as e:
#         print(e)
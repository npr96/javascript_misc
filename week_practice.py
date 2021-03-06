from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy, BaseQuery
from flask_marshmallow import Marshmallow
import os



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
        'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=False)
    password = db.Column(db.String(144), unique=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class GuideSchema(ma.Schema):
    class Meta:
        fields = ('username', 'password')


guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)
db.create_all()


@app.route('/guide', methods=['POST'])
def add_guide():
    username = request.json['username']
    password = request.json['password']
    new_guide = Guide(username, password)
    db.session.add(new_guide)
    db.session.commit()
    guide = Guide.query.get(new_guide.id)
    return guide_schema.jsonify(guide)

@app.route('/guide', methods=['GET'])
def get_guides():
    all_users = Guide.query.all()
    result = guides_schema.dump(all_users)
    return jsonify(result)


if __name__ == '__main__':
    app.run()

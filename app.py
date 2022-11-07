from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Init app
app = Flask(__name__)
# Init api
api = Api(app)
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song_database.db'
# Init db
db = SQLAlchemy(app)

#Song database Model
class SongModel(db.Model):
    id_key = db.Column(db.Integer, primary_key=True)
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    key = db.Column(db.Integer)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    speechiness = db.Column(db.Float)
    acousticness = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.FLOAT)
    valence = db.Column(db.Float)
    tempo = db.Column(db.Float)
    type = db.Column(db.String)
    id = db.Column(db.String)
    uri = db.Column(db.String)
    track_href = db.Column(db.String)
    analysis_url = db.Column(db.String)
    duration_ms = db.Column(db.Integer)
    time_signature = db.Column(db.Integer)


    def __repr__(self,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,type,id,uri,track_href,analysis_url,duration_ms,time_signature):
        return f"Song(danceability = {danceability}, energy= {energy}, key= {key}, loudness= {loudness}, mode= {mode}, speechiness= {speechiness}, acousticness= {acousticness}, instrumentalness= {instrumentalness}, liveness= {liveness}, valence= {valence}, tempo= {tempo}, type= {type}, id= {id}, uri= {uri}, track_href= {track_href}, analysis_url= {analysis_url}, duration_ms= {duration_ms}, time_signature= {time_signature})"

#creating the database locally.
with app.app_context():
    db.create_all()

#Init Request Parser for putting the data into the database
song_put_args = reqparse.RequestParser()
song_put_args.add_argument("danceability", type=float, help="danceability of the song is required")
song_put_args.add_argument("energy", type=float, help="energy of the song is required")
song_put_args.add_argument("key", type=int, help="key of the song is required")
song_put_args.add_argument("loudness", type=float, help="loudness of the song is required")
song_put_args.add_argument("mode", type=int, help="mode of the song is required")
song_put_args.add_argument("speechiness", type=float, help="speechiness of the song is required")
song_put_args.add_argument("acousticness", type=float, help="acousticness of the song is required")
song_put_args.add_argument("instrumentalness", type=float, help="instrumentalness of the song is required")
song_put_args.add_argument("liveness", type=float, help="liveness of the song is required")
song_put_args.add_argument("valence", type=float, help="valence of the song is required")
song_put_args.add_argument("tempo", type=float, help="tempo of the song is required")
song_put_args.add_argument("type", type=str, help="type of the song is required")
song_put_args.add_argument("id", type=str, help="id of the song is required")
song_put_args.add_argument("uri", type=str, help="uri of the song is required")
song_put_args.add_argument("track_href", type=str, help="track_href of the song is required")
song_put_args.add_argument("analysis_url", type=str, help="analysis_url of the song is required")
song_put_args.add_argument("duration_ms", type=int, help="duration_ms of the song is required")
song_put_args.add_argument("time_signature", type=int, help="likes of the song is required")

#Init Request Parser for updating the data into the database
song_update_args = reqparse.RequestParser()
song_update_args.add_argument("danceability", type=float, help="danceability of the song is required")
song_update_args.add_argument("energy", type=float, help="energy of the song is required")
song_update_args.add_argument("key", type=int, help="key of the song is required")
song_update_args.add_argument("loudness", type=float, help="loudness of the song is required")
song_update_args.add_argument("mode", type=int, help="mode of the song is required")
song_update_args.add_argument("speechiness", type=float, help="speechiness of the song is required")
song_update_args.add_argument("acousticness", type=float, help="acousticness of the song is required")
song_update_args.add_argument("instrumentalness", type=float, help="instrumentalness of the song is required")
song_update_args.add_argument("liveness", type=float, help="liveness of the song is required")
song_update_args.add_argument("valence", type=float, help="valence of the song is required")
song_update_args.add_argument("tempo", type=float, help="tempo of the song is required")
song_update_args.add_argument("type", type=str, help="type of the song is required")
song_update_args.add_argument("id", type=str, help="id of the song is required")
song_update_args.add_argument("uri", type=str, help="uri of the song is required")
song_update_args.add_argument("track_href", type=str, help="track_href of the song is required")
song_update_args.add_argument("analysis_url", type=str, help="analysis_url of the song is required")
song_update_args.add_argument("duration_ms", type=int, help="duration_ms of the song is required")
song_update_args.add_argument("time_signature", type=int, help="likes of the song is required")

#Intitializing the recourse fields format for return.
resource_fields= {
    'id_key': fields.Integer,
    'danceability': fields.Float,
    'energy': fields.Float,
    'key': fields.Integer,
    'loudness': fields.Float,
    'mode': fields.Integer,
    'speechiness': fields.Float,
    'acousticness': fields.Float,
    'instrumentalness': fields.Float,
    'liveness': fields.Float,
    'valence': fields.Float,
    'tempo': fields.Float,
    'type': fields.String,
    'id': fields.String,
    'uri': fields.String,
    'track_href': fields.String,
    'analysis_url': fields.String,
    'duration_ms': fields.Integer,
    'time_signature': fields.Integer
}

#Definening class for basic features
class Song(Resource):
    @marshal_with(resource_fields)
    #retrieve request
    def get(self,song_id):
        result = SongModel.query.filter_by(id_key=song_id).first()
        if not result:
            abort(404, message='Could not find song with that id')
        return result

    @marshal_with(resource_fields)
    #upload request
    def put(self,song_id):
        args = song_put_args.parse_args()
        result = SongModel.query.filter_by(id_key=song_id).first()
        if result:
            abort(409, message='Song id taken...')
        
        song = SongModel(id_key=song_id, danceability=args['danceability'], energy=args['energy'], key=args['key'], loudness=args['loudness'], mode=args['mode'], speechiness=args['speechiness'], acousticness=args['acousticness'], instrumentalness=args['instrumentalness'], liveness=args['liveness'], valence=args['valence'], tempo=args['tempo'], type=args['type'], id=args['id'], uri=args['uri'], track_href=args['track_href'], analysis_url=args['analysis_url'], duration_ms=args['duration_ms'], time_signature=args['time_signature'])
        db.session.add(song)
        db.session.commit()
        return song, 201

    @marshal_with(resource_fields)
    #update request
    def patch(self, song_id):
        args = song_update_args.parse_args()
        result = SongModel.query.filter_by(id_key=song_id).first()
        if result == None:
            abort(404, message="Song doesn't exist, cannot update")
        if args['danceability']:
            result.danceability = args['danceability']
        if args['energy']:
            result.energy = args['energy']
        if args['key']:
            result.key = args['key']
        if args['loudness']:
            result.loudness = args['loudness']
        if args['mode']:
            result.mode = args['mode']
        if args['speechiness']:
                result.speechiness = args['speechiness']
        if args['acousticness']:
                result.acousticness = args['acousticness']
        if args['instrumentalness']:
                result.instrumentalness = args['instrumentalness']
        if args['liveness']:
                result.liveness = args['liveness']
        if args['valence']:
                result.valence = args['valence']
        if args['tempo']:
                result.tempo = args['tempo']
        if args['type']:
                result.type = args['type']
        if args['id']:
                result.id = args['id']
        if args['uri']:
                result.uri = args['uri']
        if args['track_href']:
                result.track_href = args['track_href']
        if args['analysis_url']:
                result.analysis_url = args['analysis_url']
        if args['time_signature']:
                result.time_signature = args['time_signature']


        db.session.commit()
        return result

    #delete request
    def delete(self, song_id):
        result = SongModel.query.filter_by(id_key=song_id).first()
        if result:
            db.session.delete(result)
            db.session.commit()
            return "Song deleted from the database"
        else:
            return "Song not present in the database"

#Definening class for full database
class Song_db(Resource):
    @marshal_with(resource_fields)
    #retrieve request
    def get(self):
        result = SongModel.query.all()
        if not result:
            abort(404, message='Database is empty.')
        return result
    #delete request
    def delete(self):
        result = SongModel.query.delete()
        if result:
            #for r in result:
                #db.session.delete(result)
            db.session.commit()
            return "All entries of Song deleted from the database."
        else:
            return "Database is already empty."
            
#adding recources to the api
api.add_resource(Song, "/song/<int:song_id>")
api.add_resource(Song_db, "/song_db/")

# Run Server
if __name__ == "__main__":
    app.run(debug=True)

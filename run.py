from app import create_app, db
from app.models import User, DormBuilding, DormRoom, DormImage

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'DormBuilding': DormBuilding,
        'DormRoom': DormRoom,
        'DormImage': DormImage
    }

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
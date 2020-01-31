from flask_restful import Api
from flask import Flask
from pessoa_controller.controller_pessoa import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa')

@app.route('/')
def inicio():
    return '''<h1>Hallowed Be Thy Name</h1><br>
<h3>Iron Maiden</h3><br>
I'm waiting in my cold cell when the bell begins to chime<br>
Reflecting on my past life and it doesn't have much time<br>
'Cause at 5 o'clock, they take me to the Gallows Pole<br>
The sands of time for me are running low, yeah!<br>
When the priest comes to read me the last rites<br>
I take a look through the bars at the last sights<br>
Of a world that has gone very wrong for me<br>
Can it be that there's some sort of error<br>
Hard to stop the surmounting terror<br>
Is it really the end, not some crazy dream?<br>
Somebody please tell me that I'm dreaming<br>
It's not easy to stop from screaming<br>
The words escape me when I try to speak<br>
Tears flow, but why am I crying<br>
After all I'm not afraid of dying<br>
Don't I believe that there never is an end<br>
As the guards march me out to the courtyard<br>
Somebody cries from a cell "God be with you"<br>
If there's a God then why has he let me go?<br>
As I walk all my life drifts before me<br>
And though the end is near I'm not sorry<br>
Catch my soul, it's willing to fly away<br>
Mark my words, believe my soul lives on<br>
Don't worry now that I have gone<br>
I've gone beyond to seek the truth<br>
When you know that your time is close at hand<br>
Maybe then you'll begin to understand<br>
Life down here is just a strange illusion<br>
Yeah, hallowed be thy name<br>
Yeah, hallowed by thy name<br>
Yeah<br>'''

app.run(debug=True)

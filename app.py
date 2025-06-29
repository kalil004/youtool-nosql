from flask import Flask, request, render_template
from transcript_extractor import get_transcript
from database import save_transcript

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = None
    error = None

    if request.method == 'POST':
        video_id = request.form['video_id']
        result = get_transcript(video_id)
        if 'error' in result:
            error = result['error']
        else:
            transcript = result
            save_transcript(video_id, transcript)

    return render_template('index.html', transcript=transcript, error=error)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/analyze')
def analyze():
    f_name = request.args.get('file_name')
    return render_template('analyze.html',media_name = f_name)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def serverproblem(e):
    return render_template('404.html'), 500

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/figureskating ')
def figureskating():
    return render_template('figureskating.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            ch = CloudHandler()
            #BUCKET_NAME = 'synchronized_skating'
            BUCKET_NAME = 'dance-images'
            ch.upload_blob(BUCKET_NAME,filename,filename)
            return redirect(url_for('analyze',file_name = filename))
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',
             #                       filename=filename))
    return render_template('UploadPage.html')

if __name__ == '__main__':
    app.run(debug=True)

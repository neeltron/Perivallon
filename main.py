from flask import Flask, render_template, request, make_response, redirect, url_for



app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/')
def index():
  return render_template('index.html')



# File Uploads (needs an HTML Form)
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    file.save('uploads/'+file.filename)
    return file.filename
  return "not here yet"
  


# Redirects
@app.route('/redirect')
def redirec():
  return redirect(url_for('index'))



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )

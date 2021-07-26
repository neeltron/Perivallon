from flask import Flask, render_template, request, make_response, redirect, url_for
import os
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cognitio-7378d-dc91500811d5.json"

def detect(img):
  from google.cloud import vision
  client = vision.ImageAnnotatorClient()
  file_name = os.path.abspath(img)
  with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
  image = vision.Image(content=content)
  response = client.label_detection(image=image)
  labels = response.label_annotations
  return str(labels[0].description)

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
    file.save('uploads/' + file.filename)
    labels = detect('uploads/' + file.filename)
    file.close()
    newf = open('data.csv', 'a')
    newf.write(file.filename + ", " + labels + "\n")
    newf.close()
    return labels
    
  return "not here yet"



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )

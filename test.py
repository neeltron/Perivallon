import os
import io

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cognitio-7378d-dc91500811d5.json"

def detect(img):
  from google.cloud import vision
  client = vision.ImageAnnotatorClient()
  file_name = os.path.abspath(img)
  with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
  image = vision.Image(content=content)
  response = client.label_detection(image=image)
  labels = response.label_annotations
  return labels

labels = detect('uploads/altsight0.png')
print(labels)

for i in labels:
  print(i.description)

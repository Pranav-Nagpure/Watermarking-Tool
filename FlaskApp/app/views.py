from app import app
from flask import request, render_template
from PIL import Image
import numpy as np
import cv2
import os

app.config['GENERATED_FILE'] = 'app/static/generated'

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        # Get Uploaded Image
        img = Image.open(request.files['img_upload'])
        img = np.array(img.convert('RGB'))
        img_h, img_w, _ = img.shape

        if request.form['options'] == 'image_watermark':
            # Get Uploaded image to Watermark with
            wm_img = Image.open(request.files['wm_img_upload'])
            wm_img = np.array(wm_img.convert('RGB'))

            # Find Region of Interest in original Image
            wm_img_h, wm_img_w, _ = wm_img.shape

            top_y = int(img_h / 2) - int(wm_img_h / 2)
            left_x = int(img_w / 2) - int(wm_img_w / 2)
            bottom_y = top_y + wm_img_h
            right_x = left_x + wm_img_w

            roi = img[top_y: bottom_y, left_x: right_x]

            # Replace ROI with Watermark
            wm_img = cv2.addWeighted(roi, 1, wm_img, 1, 0)
            img[top_y: bottom_y, left_x: right_x] = wm_img
        
        elif request.form['options'] == 'text_watermark':
            # Get Input Text
            txt = request.form['wm_txt_upload']

            # Generate results
            cv2.putText(img, text=txt, org=(img_w - 95, img_h - 10), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,0), thickness=2, lineType=cv2.LINE_4)
        
        # Return results
        img = Image.fromarray(img)
        filepath = os.path.join(app.config['GENERATED_FILE'], 'image.jpg')
        img.save(filepath)
        return render_template('index.html', result = 'static/generated/image.jpg')
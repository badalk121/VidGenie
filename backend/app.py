from flask import Flask, request, jsonify
from manim import *
import os

app = Flask(__name__)

class CustomScene(Scene):
    def construct(self):
        user_text = request.form['text']
        image_path = request.files['image'].filename
        position = [float(coord) for coord in request.form['position'].split(',')]
        
        if len(position) == 2:
            position.append(0.0)
        
        text = Text(user_text)
        text.to_edge(UP)
        
        image = ImageMobject(image_path)
        image.move_to(position)
        
        self.add(text, image)
        self.wait(2)

@app.route('/generate', methods=['POST'])
def generate_video():
    try:
        text = request.form['text']
        image = request.files['image']
        position = request.form['position']

        media_dir = 'media'
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
        
        image_path = os.path.join(media_dir, image.filename)
        image.save(image_path)

        config.media_width = "50%"
        config.output_file = "output_video.mp4"
        
        scene = CustomScene()
        scene.render()

        return jsonify({'videoUrl': '/path/to/output_video.mp4'})
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

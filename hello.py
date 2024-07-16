#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "div><h1>STORY</h1><br><p>Once upon a time, in a small village by the sea, lived a young girl named Lily. She loved exploring the woods and playing by the shore. One sunny day, while walking along the beach, she found a strange, shimmering stone. It was unlike anything she had seen before, glowing softly in her hand. Curious, she took it to the village elder, a wise old woman named Mae. Mae looked at the stone and smiled. She told Lily that it was a magical stone that could grant one wish.Excited and a little scared, Lily thought long and hard about her wish. She wished for the village to always have enough food so no one would ever go hungry. Mae nodded approvingly and told Lily to place the stone in the center of the village. As soon as she did, the stone glowed brightly and disappeared. The villagers were amazed to find their crops growing faster and healthier than ever before. From that day on, the village never faced hunger again. Lily was hailed as a hero, not just for her discovery, but for her selfless wish that brought happiness and prosperity to everyone. And so, the village thriv</p></div"
if __name__=='__main__':
    app.run(debug=True)
from flask import Flask, request, render_template
import pickle
import spacy
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

models_dir = "models"
model_files = [f for f in os.listdir(models_dir) if f.endswith(".sav")]
models = {}

for model_file in model_files:
    model_name = model_file.split(".sav")[0]
    models[model_name] = pickle.load(open(os.path.join(models_dir, model_file), 'rb'))

nlp = spacy.load("xx_ent_wiki_sm")

@app.route('/')
def home():
    return render_template('index.html', model_names=models.keys(),
                           default_model="Atbalsta vektora mašīna (TF-IDF) bez priekšapstrādes_0.9746")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        text = request.form['text']
        model_name = request.form['model']

        if not text:
            raise ValueError("Norādīts nepilnīgs raksta saturs.")

        if model_name not in models:
            raise ValueError("Izvēlētais modeļa fails nav pieejams.")

        prediction = models[model_name].predict([text])
        return render_template('index.html', prediction_text='Ziņu kategorija: {}'.format(prediction[0]),
                               model_names=models.keys(), input_text=text, selected_model=model_name)
    except Exception as e:
        error_message = f"Kļūda: {str(e)}"
        return render_template('index.html', error_message=error_message, model_names=models.keys(),
                               input_text=text, selected_model=model_name)


if __name__ == '__main__':
    app.run(debug=True)
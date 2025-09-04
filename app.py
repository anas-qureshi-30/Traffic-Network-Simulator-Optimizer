import os
from flask import Flask, request, render_template, redirect, session
import pandas as pd
import data_preprocessing,plotting

app = Flask(__name__)

app.secret_key = 'secret_key' 


UPLOAD_FOLDER = './uploads' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/datainput.html', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        
        file = request.files["file_input"]
        
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            session['file_path'] = file_path  
            df = data_preprocessing.dataProcessing(file_path)
            return redirect('/listing.html')

    return render_template("datainput.html")

@app.route('/listing.html', methods=['GET', 'POST'])
def listing_page():
    file_path = session.get('file_path', None)

    if file_path:
        error=False
        df = data_preprocessing.dataProcessing(file_path)
        session["sourceSet"] = list(set(df["source_node"]))
        session["desSet"] = list(set(df["destination_node"]))
        df_list = df.to_dict(orient='records')
        return render_template("listing.html", df=df_list,error=error)
    else:
        error=True
        return render_template("listing.html",error=error)
    
@app.route('/userInteraction.html', methods=['GET', 'POST'])
def user_interact():
    sourceSet = session.get("sourceSet", [])
    desSet = session.get("desSet", [])
    graph_generated = False

    if request.method == 'POST':
        source = request.form['sourceNode']
        destination = request.form['destinationNode']
        plotting.plotting_graph(source, destination)
        graph_generated = True

    return render_template("userInteraction.html", sourceSet=sourceSet, desSet=desSet, graph_generated=graph_generated)


if __name__ == '__main__':
    app.run(debug=True)

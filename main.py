from flask import Flask, render_template, request, redirect

app = Flask(__name__)

nom = ""
llistaNoms = []

@app.route("/")
@app.route("/inici")
def inici():
    #return "<h1>Hola</h1>"
    nomAula = "Info3"
    return render_template("inici.html", nom=nomAula)

@app.route("/ArtistTF")
def ArtistTF():
    #return "<h1>Hola</h1>"
    nomAula = "Info4"
    return render_template("ArtistTF.html")

@app.route("/info")
def informacio():
    paramRebut = request.args.get("param1")# http://127.0.0.1:5000/info?param1=valor1
    param2 = request.args.get("param2")

    print("---------")
    print(nom)
    return render_template("info.html", paramRebut=paramRebut, param2=param2, nomPost=nom, llistaNoms=llistaNoms)

@app.route("/registrar", methods=["POST"])
def registrar():
    # Si és un mètode post, ha de ser un .form, no un .args.
    nom = request.form.get("nom")
    print("Ruta registrar: nom=" + nom)
    llistaNoms.append(nom)
    #return nom
    #return render_template("info.html", nom=nom)
    return redirect("/info")



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template  # type: ignore

app = Flask(__name__)

#place all routes here


# CATEGORIES 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/landandsea")
def get_cat1():
    return render_template("land_and_sea.html")

@app.route("/landandseainfo")
def get_cat11():
    return render_template("land_and_sea_pg2.html")

@app.route("/wildlifeandsealife")
def get_cat2():
    return render_template("wildlife_and_sealife.html")

@app.route("/wildlifeandsealifeinfo")
def get_cat22():
    return render_template("wildlife_and_sealife_pg2.html")

@app.route("/hawaiilifestyle")
def get_cat3():
    return render_template("hawaii_lifestyle.html")

@app.route("/hawaiilifestyleinfo")
def get_cat33():
    return render_template("hawaii_lifestyle_pg2.html")

@app.route("/community")
def get_cat4():
    return render_template("community.html")

@app.route("/communityinfo")
def get_cat44():
    return render_template("community_pg2.html")

@app.route("/visitinghawaii")
def get_cat5():
    return render_template("visiting_hawaii.html")

@app.route("/visitinghawaiiinfo")
def get_cat55():
    return render_template("visiting_hawaii_pg2.html")

@app.route("/laws")
def get_cat6():
    return render_template("laws.html")

@app.route("/lawsinfo")
def get_cat66():
    return render_template("laws_pg2.html")

#TABS 

@app.route("/aboutus")
def get_about():
    return render_template("about.html")

@app.route("/contact")
def get_contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)


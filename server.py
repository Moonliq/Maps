from flask import Flask, render_template

# from python_org_news import get_python_news
# from weather import weather_by_city


app = Flask(__name__)# pass the name of the current file

@app.route('/') # decorator
def index():#function name is view
    title = "Map"
    # weather  = weather_by_city("Moscow,Russia")
    # news_list = get_python_news()
    discricts =  {"cfo": '#000000',
      "szfo": '#54cbba',
      "yfo": '#f9768e',
      "skfo": '#9a5597',
      "pfo": '#30cb05',
      "urfo": '#bac1cc',
      "sfo": '#16acdb',
      "dfo": '#fbc520',
      'bel': '#54cbba',
      'bry': '#54cbba',
      'vla': '#54cbba',
      'vor': '#54cbba',
      'iva': '#54cbba',
      'klu': '#54cbba',
      'kos': '#54cbba',
      'krs': '#54cbba',
      'lip': '#54cbba',
      'mos': '#54cbba',
      'mow': '#54cbba',
      'orl': '#54cbba',
      'rya': '#54cbba',
      'smo': '#54cbba',
      'tam': '#54cbba',
      'tve': '#54cbba',
      'tul': '#54cbba',
      'yar': '#54cbba',
      'ark': '#54cbba',
      'vlg': '#54cbba',
      'kgd': '#54cbba',
      'kr': '#54cbba',
      'ko': '#54cbbv',
      'len': '#54cbba',
      'mur': '#54cbba',
      'nen': '#54cbba',
      'ngr': '#54cbba',
      'psk': '#54ccba',
      'spe': '#54cbba',
      'ad': '#54cbba',
      'ast': '#55b9da',
      'vgg': '#54cbba',
      'kl': '#54cbba',
      'kda': '#54cbba',
      'sev': '#54cbba',
      'kry': '#54crra',
      'ros': '#54cbba',
      'da': '#54cbba',
      'in': '#54cbba',
      'kb': '#54cbba',
      'kc': '#54cbba',
      'se': '#54cbba',
      'sta': '#54cbba',
      'ce': '#54cbba',
      'ba': '#54cbba',
      'kir': '#54cbba',
      'me': '#54cbba',
      'mo': '#54cbba',
      'niz': '#54cbba',
      'ore': '#54cbba',
      'pnz': '#54cbba',
      'per': '#54cbba',
      'sam': '#54cbbb',
      'sar': '#54cbbb',
      'ta': '#54cbbb',
      'ud': '#54cbbb',
      'uly': '#54cbbb',
      'cu': '#54cbbb',
      'kgn': '#54cbbb',
      'sve': '#54cbbb',
      'tyu': '#54cbbb',
      'khm': '#54cbbb',
      'che': '#54cbbb',
      'yan': '#54cbbb',
      'alt': '#54cbbb',
      'al': '#54cbbb',
      'bu': '#54cbbb',
      'zab': '#54cbbb',
      'irk': '#54cbbb',
      'kem': '#54cbbb',
      'kya': '#54cbbb',
      'nvs': '#54cbbb',
      'oms': '#54cbbb',
      'tom': '#54cbbb',
      'ty': '#54cbbb',
      'kk': '#54cbbb',
      'amu': '#54cbbb',
      'yev': '#54cbbb',
      'kam': '#b9da55',
      'mag': '#ac97b4',
      'pri': '#0cee6c',
      'sa': '#e33617',
      'sak': '#d8122f',
      'kha': '#da7655',
      'chu': '#101010'
    }
    
    return render_template('index.html', page_title = title, districts=discricts)# handle html and its variables
    #return render_template('index.html', page_title = title, weather = weather, news_list = news_list)# handle html and its variables

if __name__ == "__main__":
    app.run(debug=True)
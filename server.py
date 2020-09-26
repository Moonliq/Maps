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
      "dfo": '#fbc520'
    }
    return render_template('index.html', page_title = title, districts=discricts)# handle html and its variables
    #return render_template('index.html', page_title = title, weather = weather, news_list = news_list)# handle html and its variables

if __name__ == "__main__":
    app.run(debug=True)
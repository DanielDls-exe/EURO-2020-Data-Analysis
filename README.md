# Euro 2020 Data Analysis

![myimagen](/img/euro2020.jpg)

## Beginning 🚀

To get started you need to have Python installed

### Installation 🔧

Clone the repository

```
git clone https://github.com/DanielDls-exe/mid-project-euro2020.git
```
Use the command in the box below to install the project dependencies

```
cd midproject
pip install -r requirements.txt
```

Now install Jupyter-notebook

```
cd midproject
conda install -c conda-forge jupyterlab
```

#Run it locally.
Go to the "data" folder

```
cd data
jupyter notebook
```

## Running ⚙️

Execute the API

```
cd midproject/api 
uvicorn main:app --reload
```

Executes the Streamlit

```
cd midproject/streamlit 
streamlit run main.py
```

## Endpoints ⚙️

```
/players --> shows us the data of all the players of Euro 2020
/player/{name} --> The data of a specific player is obtained
/players/name/all --> All players names
/player/{name}/goals --> The goals of a specific player are obtained
/player/{name}/asssit --> The assistance of a specific player are obtained
/player/{name}/cards --> Returns the cards of a specific player, you have to pass a web parameter color = [red, yellow].
/teams --> shows us the data of all the teams of Euro 2020
/team/{team} --> The data of a specific team is obtained
/team/{team}/shots -->
/team/{team}/possession --> 
/team/{team}/goals/scored --> Goals scored by a specific team
/team/{team}/goals/received --> Goals received by a specific team
/team/{team}/goals/penaltys --> Goals scored (penaltys) by a specific team
/team/name/all --> All teams names
l```


## Built with 🛠️

Python 3.9, Jupyter-notebook, pandas, numpy, matplotlib.

## Author ✒️

* **Daniel Alvarado** - [danieldls-exe](https://github.com/DanielDls-exe)


## License 📄

This project is under the MIT License.

---
⌨️ with ❤️ by [danieldls-exe](https://github.com/DanielDls-exe) 😊
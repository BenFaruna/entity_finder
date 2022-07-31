# entity_finder

Entity finder is a web app built using Test Driven Development (TDD) Approach following [Wes Doyle](https://www.youtube.com/watch?v=eAPmXQ0dC7Q&t=7s) tutorial on TDD using flask and spacy.
Entity finder uses SpaCy, a popular Natural language processing (NLP) library, check it out [here](https://www.spacy.io).
The web app takes a sentence and displays a table showing the class of the words contained in the sentence.

## Setting up environment
Create a virtual environment and activate the environment using the commands below

```
$ python -m venv venv
$ venv\Scripts\activate
```
This is done to isolate the packages used for the project from external packages, to help maintain a clean working environment and avoid dependency conflicts.
This project uses flask, spacy, selenium and pytest. Run the command below to install the packages in your virtual environment.

```
(venv) $ pip install flask spacy selenium pytest
```

The command below downloads the language model used for this web application

```
(venv) $ python -m spacy download en_core_web_sm
```

The environment is ready to run the application. To start up the application, run the command
```
(venv) $ python app.py
```

To test the application, open another terminal, navigate to the test folder of the application, activate your virtual environment using the steps above and run the command
```
(venv) $ python -m pytest
```

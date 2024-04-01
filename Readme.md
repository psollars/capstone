# MADS-RAG: A Helpful Chatbot for Master’s of Applied Data Science Students at the University of Michigan

### SIADS 699 Capstone (Winter 2024)

### Team 28: Patrick Sollars, Aaron Newman, and Tawfiq Zureiq

Throughout our time as Masters of Applied Data Science (MADS) students, we have relied on communications tools like Slack to answer questions about classes and the overall program. Fortunately, there are faculty, staff, fellow students, and alumni who are usually willing to lend their expertise. Our team thought that it would be nice to use Artificial Intelligence techniques to answer some of those frequently asked questions - the types of questions where the answer can probably be found in course syllabi or perhaps the student handbook.

## Using This Repo

- `00_archive` A graveyard for old unpolished work, we’ll remove this for the final submission
- `01_loading` This has relevant code to load and split the documents, run document_loader.ipynb with a fresh repo to get started
- `02_evaluation` Working in here to test out different retrieval strategies and models, the notebooks should have some report or visualization at the end about the performance
- `03_visualization` Ad hoc notebooks to create viz for the report
- `04_chatbot` Any notebooks/code/configuration relevant to the UI or “productionizing” the finished product

## Environment

This repo uses [pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies.

If you don't already have it installed you can do so with:

```sh
$ pip install --user pipenv
# -or-
$ brew install pipenv
```

Or, view the complete [installation documentation](https://pipenv.pypa.io/en/latest/installation.html).

Then navigate to the repo and run these commands to install project dependencies.

```sh
# Recommended to keep the venv local to the repository
export PIPENV_VENV_IN_PROJECT=1

pipenv shell

pipenv install --dev
```

> **NOTE:** You might also prefer to set `PIPENV_VENV_IN_PROJECT=1` in your .env or .bashrc/.zshrc (or other shell configuration file) for creating the virtualenv inside your project’s directory.

## Secrets

Some notebooks require API keys to run, these should be stored in the .gitignored file, `secrets.py`, in the root of this repo.

```
OPENAI_API_KEY = "your_secret_key"
NGROK_AUTH_TOKEN = "your_secret_key"
```

## Data Access

All syllabus documents used in this project are publicly accessible through the [Master of Applied Data Science Curriculum page](https://www.si.umich.edu/programs/master-applied-data-science/curriculum/mads-courses).

Additional source documents are referenced below:

- [MADS Student Handbook](https://docs.google.com/document/d/1YEOcpdONdme5kmpNEnZpdbJeVFhEIw1pS0wq16QdH1I/edit)
- [MADS Academic Advising FAQ](https://docs.google.com/document/d/1A3zdTF0AYQY_zzD2-OlpSHeDxnWqFVEhXl446SyT_pA/edit)

Proprietary transcripts from MADS course lectures were pulled from Coursera using [`coursera-dl`](https://github.com/coursera-dl/coursera-dl).

Quantized large language models were sourced from public HuggingFace repositories:

- https://huggingface.co/TheBloke/Llama-2-7B-GGUF
- https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF
- https://huggingface.co/TheBloke/Starling-LM-7B-alpha-GGUF

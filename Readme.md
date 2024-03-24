# MADS RAG Pipeline LLM (Team 28)

## TODO

- A README file that documents how to run your code
- Code that generates results and figures in your report
- Cleaned code: unused code blocks and files removed, absolute file paths converted to relative paths, and personal keys (e.g. API) removed.
- In-line code attributions for any code segments your team did not write or received external assistance to create. If code is reused from an open source project, licenses are respected.

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

## Data Access

All syllabus documents used in this project are publicly accessible through the [Master of Applied Data Science Curriculum page](https://www.si.umich.edu/programs/master-applied-data-science/curriculum/mads-courses).

Additional source documents are referenced below:

- [MADS Student Handbook](https://docs.google.com/document/d/1YEOcpdONdme5kmpNEnZpdbJeVFhEIw1pS0wq16QdH1I/edit)
- [MADS Academic Advising FAQ](https://docs.google.com/document/d/1A3zdTF0AYQY_zzD2-OlpSHeDxnWqFVEhXl446SyT_pA/edit)

**TODO: A data access statement indicating how to access the data or explaining who owns the data. Licenses for data use and redistribution are respected.**

**TODO: add attribution for our quantized models... https://huggingface.co/TheBloke/Llama-2-7B-GGUF**

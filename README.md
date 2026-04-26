# great-example

Example project to demonstrate an [issue](https://github.com/posit-dev/great-docs/issues/141) with great-docs not being able to
render an inherited docstring. The project contains two classes, `foo` and `bar`.
`foo` supplies method `a` and `bar` supplies method `b`.
Class `bar` inherits from `foo`, thus method `a` is inherited by `bar`. 
The docstring of method `a` is only rendered in the reference docs for `foo`, 
but not for `bar`, even when explicitly listed as a member of `bar` in `great-docs.yml`.
quartodoc, on the other hand, renders the docstring of method `a` for both `foo` and `bar`.

Setup:

```bash
git clone https://github.com/goergen95/great-example.git
cd great-example
uv venv
source .venv/bin/activate
uv pip install -e .
```

Commands used to build the site with great-docs (note that we have to clean up 
the any generated files before building, otherwise we might build on top of the 
generated files from quartodoc):

```bash
# clean up first
rm -rf reference/ _site/ great-docs/
# build
great-docs build
# preview
great-docs preview
```

Commands used to build the site with quartodoc (note that we have to clean up 
the any generated files before building, otherwise we might build on top of the 
generated files from great-docs):

```bash
# clean up first
rm -rf reference/ _site/ great-docs/
# build reference docs
quartodoc build
# preview reference docs
quarto preview
```

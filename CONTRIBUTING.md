Contributing to blat
======================

## Setup for local development

1. Fork the `blat` repo on GitHub.
2. Clone your fork locally:

   ```bash
   git clone git@github.com:your_username_here/blat.git
   ```
3. Install your local copy into a virtualenv.
   ```bash
   cd blat/
   virtualenv venv
   ./venv/Scripts/activate
   pip install -e .
   ```
4. Create a branch for local development:
   ```bash
   git checkout -b name-of-your-bugfix-or-feature
   ```
    Now you can make your changes locally.
5. When you're done making changes, check that your changes pass the tests and lint check:
   ```bash
   pip install tox
   tox
   ```
   Please note that tox runs lint checks automatically.
   If you feel like running only the lint environment, please use the following command:
   ```bash
   tox -e lint
   ```
6. Ensure that your feature or commit is fully covered by tests. Check the report after a regular tox run.
7. Commit your changes and push your branch to GitHub:
   ```bash
   git add .
   git commit -m "Your detailed description of your changes."
   git push origin name-of-your-bugfix-or-feature
   ```
8. Submit a pull request through the GitHub website.

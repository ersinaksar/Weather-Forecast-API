# Weather Forecast API

An API for retrieving weather forecasts, developed for Seita's data engineering assignment. Provides endpoints for temperature, wind speed, and irradiance forecasts.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Quick Start
- Download [docker desktop](https://www.docker.com/products/docker-desktop/).
- Define local variables in .envs/.local file. For that create in .envs/.local location create .django and .postgres files
- Add these to .django file. .django-example variable
- Add these to .postgres file. .postgres-example variable
- Build the Stack:
    ```bash
    docker compose -f docker-compose.local.yml build
    ```
- Run the Stack:
    ```bash
    docker compose -f docker-compose.local.yml up
    ```
- After running these commands stop containers.
- Execute Management Commands:
    ```bash
    docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
    docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
    ```
- Download [postman](https://www.postman.com/downloads/).
- Run the Stack Again:
    ```bash
    docker compose -f docker-compose.local.yml up
    ```
- Set postman Requests like in pictures/ folder. Please make sure doin all steps in order of pictures number.
- After 1 and 2 steps you can test the api. For that firstly you should the authentication token like 3.1. Becarefull Auth type should be **API Key** and Value should be something like that. ***Token <your aut token from picture 2>*** . Becareful the is a space between Token and <key>. Add to  should be **Header**
- For test /api/forecasts/ endpoint ou can check 3.2 picture. Add the Authorization as key and Token <your aut token from picture 2> as value.
- Set the params like 3.3 picture
- After these settings press send button. You should see something like 3.4
- For api endpoind test check 4.1, 4.2 and 4.3 pictures.


## Further Reading About Cookiecutter

## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy weather_api

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally.html#using-webpack-or-gulp).

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).

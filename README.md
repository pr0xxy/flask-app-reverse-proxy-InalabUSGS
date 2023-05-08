# Simple Flask App

This is a Python Flask application that greets users with a simple message.

## Goal

The main objectives of this project were:

- To "dockerize" the application by providing an image and a configuration for running locally with Docker Compose.
- To provide a script that retrieves data from an API and performs basic parsing.
- To provide a reverse proxy configuration.

## Docker Exercise

To achieve the above objectives, the following steps were taken:

- A `Dockerfile` was created to build and run the application.
- The application was modified to replace _Hello, World!_ with an optional string set using an environment variable, and defaulting to _Hello, World!_ or _Hello, inalabgroup!_ if the environment variable `APP_NAME` is set to `inalabgroup`.
- A `docker-compose.yml` file was provided to run the application and set a custom string using an environment variable.

This should result in the ability to navigate to <http://localhost:5000/> and see the custom greeting.

## Scripting Exercise

A script was provided to parse the data returned from <http://localhost:5000/data> and create a file in a `files/` sub-directory named `<id>.txt` with the _name_ as the contents of the file.
E.g. `files/3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3.txt`

Note: The SHA256 sum of each file's contents (`<name>`) should match the `<id>`.

## Reverse Proxy Configuration

A minimal reverse proxy configuration was provided for the application. The Nginx Docker image was used and ran from the same Docker Compose file as the application.

## Submittal

The solution was pushed to a personal repository on GitHub: https://github.com/jamesnotoma/flask-app-reverse-proxy-InalabUSGS.

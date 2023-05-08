# Flask App Reverse Proxy

This is a simple Flask web application that retrieves data from an API and performs basic parsing. It also includes a reverse proxy configuration using Nginx.

## Features

- Retrieves data from an API and creates files with parsed data
- Reverse proxy configuration with Nginx

## Installation

1. Clone the repository
2. Install the required packages with `pip install -r requirements.txt`
3. Start the application with `docker-compose up`

## Usage

The application will be running at http://localhost:5000.

## Reverse Proxy Configuration

The Nginx reverse proxy configuration is included in the `nginx.conf` file. It forwards requests to the Flask application running on port 5000.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Please contact James Notoma (james_notoma@hotmail.com) for any questions or feedback.

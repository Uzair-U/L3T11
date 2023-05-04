# L3T11
This repo serves to hold my Level 3 task 11 assignment

## Running the Application

To run the application, you will need to have Docker installed on your machine.

1. Clone this repository to your local machine.
2. Open a terminal and navigate to the root directory of the project.
3. Build the Docker image by running the following command:

docker build -t semantic-similarity .

Run the Docker container by running the following command:

docker run -p 8000:8000 semantic-similarity

Open a web browser and go to `http://localhost:8000` to view the application.

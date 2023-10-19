# ETL_DataAnalysis_YellowTaxi


### This project demonstrates how to build an ETL (Extract, Transform, Load) pipeline using Docker containers and Python. The pipeline extracts data from a PostgreSQL database, cleans and analyzes the data, and returns the cleaned data to the database. The project also includes visualization of the yellow taxi data using Matplotlib and Seaborn, as well as data manipulation with Pandas. SQLAlchemy is used for connecting to the PostgreSQL database.

#### Install python : Python packages: Install the required Python packages by running the following command :
```

pip install -r requirments.txt

```

### Project Structure
1. DockerFile: containing the specifications of the image building to prepare to ingest the data to postgres
2. Yaml file : containing the environments used in to build containers
3. Ingest script : python file to ingest the taxi data to postgres DB
4. Data analysis notebook : contains every command run in the analysis project and transformed into python script

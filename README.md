# logs_analysis
Udacity FSND Project 3-1 Logs Analysis

### Files
* logs_analysis.py
* Result.txt
* README.md

### Installation
The following software is requred to run this program.
* VirtualBox: https://www.virtualbox.org/wiki/Downloads
* Vargrant: https://www.vagrantup.com/downloads.html

### Cloning the source repository
Fork the repository below to your GitHub then clone it to your local computer.

https://github.com/udacity/fullstack-nanodegree-vm

### Download newsdata.sql file
First, Download the file from the link below.
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Second, unzip the file and save 'newsdata.sql' file to FSND-Virtual-Machine/vagrant/

### Save python file
Save the "logs_analysis.py" to FSND-Virtual-Machine/vagrant/

### Run Vargrant virtual machine
Commit the command below to run Vagrant VM on vagurant directory.

```
 $ vagrant up
 $ vagrant ssh
```
### Run the database
First, change diretory to the vagrant
```
 $ cd /vagrant/
```
Second, initialize the tournament database.
```
 $ psql -d news -f newsdata.sql
```

### Create views
First, connect to the news database.
```
psql news
```
Second, copy and paste the following three commands to create views.

```
create view error_count as select cast(time as date), count(*) as error from log where status not like '%200%' group by cast(time as date) order by cast (time as date) desc;

create view log_status as select cast(time as date), count(*) as error from log group by cast(time as date) order by cast(time as date) desc;

create view load_error as select log_status.time, round(((error_count.error * 100.) / log_status.error), 1) as error from log_status, error_count where log_status.time = error_count.time order by log_status.time asc;
```
Third, close database.
```
\q
```

### Run the logs_analysis.py
Run tournament_test.py file to see the results.
```
 $ python log_analysis.py
```

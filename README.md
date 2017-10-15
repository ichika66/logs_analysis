# logs_analysis
Udacity FSND Project 3-1 Logs Analysis

create view error_count as select cast(time as date), count(*) as error from log where status not like '%200%' group by cast(time as date) order by cast (time as date) desc;

create view log_status as select cast(time as date), count(*) as error from log group by cast(time as date) order by cast(time as date) desc;

create view load_error as select log_status.time, round(((error_count.error * 100.) / log_status.error), 1) as error from log_status, error_count where log_status.time = error_count.time order by log_status.time asc;

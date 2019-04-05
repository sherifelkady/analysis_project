# Project : logs analysis
### by Sherif Elkady
## Description
internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Requirements
* Python 3
* Vagrant
* VirtualBox
* Git

## Getting Started
1 - Download and install VirtualBox and vagrant
2 - Download [Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3 - Download this [folder](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
4 - Open folder Directory by using GitBash then type vagrant up
5 - Use vagrant ssh to log in 
3 - Back to the Database folder and Run python log_analysis.py to extract Logs Analysis report

## Create Views

### First view 
create view all_view as select time::date as times, count(*) 
as views from log group by times 
order by times;

### Second view
create view all_error as select time::date as times, count(*) as errors 
from log where status like '%404%' 
group by times order by times;

### Third view
create view error_per as select all_view.times, (100.0*all_error.errors/all_view.views) as percentage 
from all_view, all_error 
where all_view.times = all_error.times 
order by all_view.times;


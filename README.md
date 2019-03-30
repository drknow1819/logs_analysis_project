
# Project 1: _**Logs Analysis**_

Logs analysis program is a simple [**python**](https://www.python.org/shell) code using the `psycopg2` module to connect to the database.
It works as a reporting tool, which use information from a newspaper's database to retrieve many things
such as_"what kind of articles the readers like"_, and **much more**.

### The database
**News** database has lots of information, it includes three tables:
* **Log** - Which contains columns has the timestamp and timezone of each reader
requested an article, his ip address and HTTP status (OK or NOT FOUND).
* **Articles** - Has data about articles names, brief description of each article
and article's author id.
* **Authors** - Includes authors names, each author biography and thier ids
in the newspaper database.

_You can use a number of special `psql` commands to get information about the database
and make configuration changes when you finish the installation and configuration
process at the below section._
* `news=> \dt` — list all the tables in the database.
* `news=> \d table_name` — list all the columns in this table.
* `news=> \dt+` — list tables plus additional information.
* `news=> \H` — switch between printing tables in plain text vs. HTML.

### Usage
To run this program, you'll need database software(provided by a Linux virtual machine)
and the **news** database. **Don't worry** all links supported below.
##### Terminal
_"If you are using a Mac or Linux system, your regular terminal program will do just fine.
On Windows, recommended to use the Git Bash terminal that comes with the Git software.
If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/downloads)."_
##### Download and Install Virtual Machine
I recommend using tools called [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) to install and manage the VM.

*** _**Ubuntu users:** 
If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu
Software Center instead. Due to a reported bug, installing VirtualBox
from the site may uninstall other software you need._

**VirtualBox** is the software that actually runs the virtual machine.
Install the platform package for your operating system.
You do not need the extension pack or the SDK.
You do not need to launch VirtualBoxafter installing it; Vagrant will do that.

**Vagrant** is the software that configures the VM and lets you share
files between your host computer and the VM's filesystem.

*** **_Windows users:_** 
The Installer may ask you to grant network permissions to Vagrant or make
a firewall exception. Be sure to allow this.
##### Configure your VM
First create a folder in your desired directory and from your terminal `cd`
into this folder. For example, I've created a folder titled **logs_analysis** on my
desktop.

I executed the following command in Terminal to `cd` to my folder:
```
$ cd ~/desktop/logs_analysis
```
To start configuring **vagrant** paste the following command in your terminal.
```
vagrant init bento/ubuntu-16.10 \  --box-version 2.3.5
```
**Note:** If you are using Windows OS excute the following commad insted of
the previous one.
```
vagrant init bento/ubuntu-16.04-i386 \  --box-version 201812.27.0
```
You can access all the other [Boxes](https://app.vagrantup.com/bento) if you want to install diffrent environment.

* **Congratulation ... You have created "VAGRANTFILE"**


##### Start the virtual machine
After you created **vagrantfile** in the previous step, now run the command `vagrant up`.
This will cause Vagrant to download the Linux operating system and install it.
This may take quite a while (many minutes) depending on how fast your Internet connection is.

When `vagrant up` is finished running, you will get your shell prompt back.
At this point, you can run `vagrant ssh` to login to your newly installed Linux VM!

##### Running the database
You can use Github to fork and clone the repository [https://github.com/drknow1819/logs_analysis_project.git](https://github.com/drknow1819/logs_analysis_project.git) to the directory
(_ex:_**logs_analysis**) early created.

Also you need to download and unzip the **news** database into the **vagrant** directory.
[Please, click here to download news database!](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

The PostgreSQL database server will automatically be started inside the VM.
You can use the `psql` command-line tool to access it and run SQL statements.
* `psql` — the PostgreSQL command line program
* `-d news` — connect to the database named news which has been set up for you
* `-f newsdata.sql` — run the SQL statements in the file newsdata.sql

To load the data, `cd` into the **vagrant** directory and use the command
`psql -d news -f newsdata.sql`

To connect `psql` to a newspaper database, you need to give it the command:
`$ psql news`
##### Running the code
Now `cd` into the directory containig the program.
Your terminal shoud look like this:
```
vagrant@vagrant:/vagrant/logs_analysis_project-master$
````
To lunch the program paste the below command in your terminal then hit **enter** kye :
```
python project_logs_analysis.py
```

After running the program you will be able to get accurate answers for some questions
like:
* **What are the most popular three articles of all time?**
* **Who are the most popular article authors of all time?**
* **On which days did more than 1% of requests lead to errors?**

###### Note:
* This program makes it easy to work around, it includes *Shebang* 
`#!/usr/bin/env python` which using the operating system env command,
to locate and execute Python by searching the PATH environment variable.







### Techniques

Although it's a simple `code` but it includes alot of relations and techniques,
let me mention some of them:

- Joining tables
- The `select` ...`where` statement
- Select clauses
- Operators
- Aggregate() functions
- Concat() function
- Cast() function
- TO_CHAR() function
- Round()function
- Group by, Having and Order by clauses 
- Subquery

### Usefull Links

- [PostgreSQL: Documentation](https://www.postgresql.org/docs/)
- [PostgreSQL Tutorial](www.postgresqltutorial.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
- [Tutorialspoint](https://www.tutorialspoint.com/)

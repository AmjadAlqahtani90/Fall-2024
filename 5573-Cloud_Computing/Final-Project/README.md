Submission Structure

1. Logs Directory:
	Contains detailed experiment output logs.

2. Report.pdf:
	This is the main document of the project.
	It includes background, methodology, results, and conclusions.

3. Experiment-Details:
	A step-by-step guide to reproduce the experiments.
	It includes prerequisites, setup instructions, and commands to run.

4. Plots_Code Directory:
	Contains code for generating the figures presented in the project.
	
5. Output_Figures Directory:
	Includes latency and throughput figures.

6. Presentation Slides:
	A PDF summarizing the key points of the project for presentations.
	Designed to be concise and visually appealing.

7. Recorded Video and Demo:
	A video demonstrating the project's functionality and outcomes.

7. Member-Contribution:
	Details contribution for each member in the project.

8. Demo.txt
	It has the demo vidoe link. The video is uploaded on the onedrive.


Steps and environment for reproducing our results:


Clone the YCSB on your local machine.
1- clone YCSB https://github.com/mongodb-labs/ycsb
2- cd YCSB-Mongodb/ycsb-mongodb

Go and create an account (free) on MongoDB atlas
3- Create your cluster. This step will give you three instances: one primary and two secondary
4- Connect to your server. There are many options, but we use VC code: mongodb+srv://amjadalqahtani:<db_password>@cluster0.k7tll.mongodb.net/



Testing instrcution 
https://github.com/mongodb-developer/service-tests/blob/master/performance-benchmarks/ycsb.md


Coomand to YCSB Load:
./bin/ycsb load mongodb -s -P workloads/workloada -p "mongodb.url=mongodb+srv://amjadalqahtani:Julia2017@cluster0.k7tll.mongodb.net/test"


Command to run YCSB A:
./bin/ycsb run mongodb -s -P workloads/workloada -p "mongodb.url=mongodb+srv://amjadalqahtani:Julia2017@cluster
0.k7tll.mongodb.net/ycsb" > outputWorkloadA.txt

Command to run YCSB B:
./bin/ycsb run mongodb -s -P workloads/workloadb -p "mongodb.url=mongodb+srv://amjadalqahtani:Julia2017@cluster
0.k7tll.mongodb.net/ycsb" > outputWorkloadB.txt

Command to run YCSB C:
./bin/ycsb run mongodb -s -P workloads/workloadc -p "mongodb.url=mongodb+srv://amjadalqahtani:Julia2017@cluster
0.k7tll.mongodb.net/ycsb" > outputWorkloadC.txt

Command to run YCSB D:
./bin/ycsb run mongodb -s -P workloads/workloadd -p "mongodb.url=mongodb+srv://amjadalqahtani:Julia2017@cluster
0.k7tll.mongodb.net/ycsb" > outputWorkloadD.txt

Command to run YCSB E:
./bin/ycsb run mongodb -s -P workloads/workloade -p "mongodb.url=mongodb+srv://amjadalqahtani:Julia2017@cluster
0.k7tll.mongodb.net/ycsb" > outputWorkloadE.txt

Command to run YCSB F:
./bin/ycsb run mongodb -s -P workloads/workloadf -p "mongodb.url=mongodb+srv://amjadalqahtani:Julia2017@cluster
0.k7tll.mongodb.net/ycsb" > outputWorkloadF.txt





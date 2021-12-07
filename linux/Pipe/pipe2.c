#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<signal.h>
#define maxline 100

void sig_handler(char *command);

int main(int argc, char *argv[]){

	if(argc != 3){
		fprintf(stderr, "usage: %s alarm_time command", argv[0]);
		exit(1);
	}
	
	int time = 0;
	time = atoi(argv[1]);
	
	void alarmHandler(){
		sig_handler(argv[2]);
	}
	
	signal(SIGALRM, alarmHandler);
	alarm(time);
	
	int cnt=1;
	while(1){
		sleep(1);
		printf("%d sec\n", cnt);
		cnt++;	
	}

	return 0;
}

void sig_handler(char *command){

	char line[maxline];
	FILE *fpin;
	
	if((fpin = popen(command, "r")) == NULL){
		perror("popen error");
		exit(0);
	}
	
	while(fgets(line, maxline, fpin)){
		fputs(line, stdout);
	}
	pclose(fpin);
	exit(1);		
}	
	

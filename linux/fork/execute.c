#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

int main(int argc, char *argv[]){


	int child, pid, status;
	pid = fork();
	if(pid == 0){
		execvp(argv[1], &argv[1]);
		fprintf(stderr, "%s error\n", argv[1]);
	}else{
		child = wait(&status);
		printf("end code : %d \n", status>>8);
	}



	return 0;
}


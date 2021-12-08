#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<errno.h>
#include<unistd.h>

int system(const char *cmdstring);

int main(int argc, char *argv[]){
	
	int status;
	
	if(argc != 2){
		fprintf(stderr, "usage: %s command", argv[0]);
		return 0;
	}
	
	if((status = system(argv[1])) < 0){
		perror("system error\n");
	}
	printf("End Code : %d\n", WEXITSTATUS(status));
	return 0;
}

int system(const char *cmdstring){
	pid_t pid;
	int status;
	
	if(cmdstring == NULL){ return 1;}
	if((pid=fork()) < 0){
		status = -1;
	}else if(pid ==0){
		execl("/bin/sh", "sh", "-c", cmdstring , NULL);
		_exit(127);
	}else{
		while(waitpid(pid, &status, 0) < 0){
			if(errno != EINTR){
				status = -1;
				break;
			}
		}
	
	}
	return(status);
}

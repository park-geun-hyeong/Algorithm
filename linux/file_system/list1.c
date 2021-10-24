#include<sys/types.h>
#include<sys/stat.h>
#include<dirent.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char **argv){
	
	int closedir();
	DIR *dp;
	char *dir;
	struct dirent *d;
	struct stat st;
	char path[BUFSIZ+1];
	
	
	if(argc==1){
		dir=".";
	}
	else dir = argv[1];
	
	if((dp = opendir(dir)) == NULL){
		perror(dir);
	}
	
	while((d=readdir(dp)) != NULL){
		printf("%s \n", d->d_name);
	}
	
	closedir(dp);
	exit(0);

	return 0;

}


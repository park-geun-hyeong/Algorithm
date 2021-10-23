#include<sys/types.h>
#include<sys/stat.h>
#include<sys/time.h>
#include <utime.h>
#include<stdio.h>
#include<stdlib.h>


// ./cptime file1 file2
// file1 : File that has final changing time
// file2 : File that i want to change

int main(int argc, char *argv[]){

	struct stat buf;
	struct utimbuf time;
	
	
	if(argc<3){
	
		fprintf(stderr, "method : cptime file1 file2\n");
		exit(1);
	}
	
	if(stat(argv[1], &buf) < 0){
	
		perror("stat()");
		exit(-1);
	}
	
	
	time.actime = buf.st_atime;
	time.modtime = buf.st_mtime;
	
	if(utime(argv[2], &time))
		perror("utime");
	else
		exit(0);

	return 0;
}

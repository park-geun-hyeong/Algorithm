#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#define DEFAULT_PROTOCOL 0
#define MAXLINE 100

toUpper(char* in, char* out){
	int i;
	for(i =0; i < strlen(in); i++){
		out[i] = NULL;	
		if(islower(in[i])){out[i] = toupper(in[i]);}
		else{out[i] = in[i];}
	
		}
}

readLine(int fd, char* str){

	int n;
	do{
		n = read(fd, str,1);
	}while(n > 0 && *str++ != NULL);
	return(n>0);
}

int main(){

	int listenfd, connfd, clientlen;
	char inmsg[MAXLINE], outmsg[MAXLINE];
	struct sockaddr_un serverUNIXaddr, clientUNIXaddr;
	
	
	signal(SIGCHLD, SIG_IGN);
	clientlen = sizeof(clientUNIXaddr);
	
	listenfd = socket(AF_UNIX, SOCK_STREAM, DEFAULT_PROTOCOL);
	serverUNIXaddr.sun_family = AF_UNIX;
	
	strcpy(serverUNIXaddr.sun_path, "convert");
	unlink("convert");
	bind(listenfd, &serverUNIXaddr, sizeof(serverUNIXaddr));

	listen(listenfd, 5);
	
	while(1){
	
		connfd = accept(listenfd, &clientUNIXaddr, &clientlen);
		if(fork() == 0){
		
			readLine(connfd, inmsg);
			toUpper(inmsg, outmsg);
			write(connfd, outmsg, strlen(outmsg) + 1);
			close(connfd);
			exit(0);
		
		} else {close(connfd);}	
	}
}


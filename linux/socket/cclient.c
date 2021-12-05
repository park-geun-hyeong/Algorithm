#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<sys/un.h>
#define DEFAULT_PROTOCOL 0
#define MAXLINE 100

int main(){

	int clientfd, result;
	char inmsg[MAXLINE], outmsg[MAXLINE];
	struct sockaddr_un serverUNIXaddr;
	
	clientfd = socket(AF_UNIX, SOCK_STREAM, DEFAULT_PROTOCOL);
	serverUNIXaddr.sun_family = AF_UNIX;
	strcpy(serverUNIXaddr.sun_path, "convert");
	
	do{
		result = connect(clientfd, &serverUNIXaddr, sizeof(serverUNIXaddr));
		if(result == -1){sleep(1);}

	}while(result == -1);
	
	printf("input string : \n");
	fgets(inmsg, MAXLINE, stdin);
	write(clientfd, inmsg, strlen(inmsg) + 1);
	
	readLine(clientfd, outmsg);
	printf("%s -> %s\n",inmsg, outmsg);
	close(clientfd);
	exit(0);
	
}

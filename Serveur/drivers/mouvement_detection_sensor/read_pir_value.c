/*H**********************************************************************
* FILENAME :        pir.c
*
* DESCRIPTION :
*       this a programme to read the state of the pir sensor
*
* AUTHOR :    Mansouri Anas        START DATE :   10 Sep 2020
*
*H*/
#include<stdio.h>
#include<string.h>
#include"pir.h"

int main(){

pir p_sensor ;
strcpy(p_sensor.file_path,"./pir");
char value =read_value(&p_sensor);
printf("%c",value);
}
#include<stdio.h>
#include<string.h>
#include"pir.h"

int main(){

pir p_sensor ;
strcpy(p_sensor.file_path,"./file");
char value =read_value(&p_sensor);
printf("%c",value);

}
 /*H**********************************************************************
* FILENAME :        pir.h
*
* DESCRIPTION :
*       this a pir sensor driver of the raspberry pi 3 B+
*
* AUTHOR :    Mansouri Anas        START DATE :    2 Sep 2020
*
*H*/

#ifndef PIR_H_
#define PIR_H_

#include<stdbool.h>

struct pir {
    char file_path[50];
    char value;
};
typedef struct pir pir;

char read_value(pir* pir_sensor);


#endif /*PWM_H_*/
 /*H**********************************************************************
* FILENAME :        pir.c
*
* DESCRIPTION :
*       this a pir driver of the raspberry pi 3 B+
*
* AUTHOR :    Mansouri Anas        START DATE :    2 Sep 2020
*
*H*/

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<stdbool.h>
#include "pir.h"

/* ********************************** */
/* read pir sensor value                     */
/*      */
/* ********************************** */
char read_value(pir* pir_sensor)
{
    FILE *p_pir_file;
    if ((p_pir_file = fopen(pir_sensor->file_path, "r")) == NULL)
    {
        printf("Cannot open pir file.\n");
        exit(1);
    }
    rewind(p_pir_file);
    char value;
    fscanf(p_pir_file,"%c",&value);
    fclose(p_pir_file);
    return value;
}


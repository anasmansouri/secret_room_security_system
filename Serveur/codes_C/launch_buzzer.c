#include<stdio.h>
#include<stdlib.h>
#include "../drivers/pwm/pwm.h"

int main(int argc, char **argv){


if(argc !=3){
printf("please enter the period and the duty cycle ");
exit(1);
}

pwm_channel pwm;
load_pwm_channel(&pwm,"0");

char * period = argv[1];
char * duty_cycle = argv[2];
set_pwm_period(&pwm, period);
set_pwm_duty_cycle(&pwm, duty_cycle);
set_pwm_polarity(&pwm, "normal");
enable_pwm_channel(&pwm);

}

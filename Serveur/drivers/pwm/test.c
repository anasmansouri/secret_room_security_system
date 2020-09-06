#include<stdio.h>
#include "pwm.h"
#include<stdlib.h>

int main(){
pwm_channel pwm;
load_pwm_channel(&pwm,"0");
set_pwm_period(&pwm, 500000);
set_pwm_duty_cycle(&pwm, 70000);
set_pwm_polarity(&pwm, "inversed");
enable_pwm_channel(&pwm);


// getting pwm infos
char * polarity = get_pwm_polarity(pwm);
printf("\npolarity :%s",polarity);
long unsigned int period =get_pwm_period(pwm);
printf("period %lu",period);
long unsigned int duty_cycle =  get_pwm_duty_cycle(pwm);
printf("duty cycle %lu",duty_cycle);
free(polarity);
}
#include<stdio.h>
#include "pwm.h"


int main(){
pwm_channel pwm;
load_pwm_channel(&pwm,"0");
set_pwm_period(&pwm, 500000);
set_pwm_duty_cycle(&pwm, 70000);
set_pwm_polarity(&pwm, "inversed");
enable_pwm_channel(&pwm);

}
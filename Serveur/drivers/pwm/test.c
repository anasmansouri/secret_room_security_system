#include<stdio.h>
#include "pwm.h"


int main(){
pwm_channel pwm;
load_pwm_channel(&pwm,"0");
set_pwm_period(&pwm, 10000);
// set_pwm_polarity(&pwm, "inversed");
}
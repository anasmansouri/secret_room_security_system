#include "../drivers/pwm/pwm.h"

int main(){


pwm_channel pwm;
load_pwm_channel(&pwm,"0");
set_pwm_period(&pwm, 160000000);
set_pwm_duty_cycle(&pwm, 70000000);
set_pwm_polarity(&pwm, "normal");
enable_pwm_channel(&pwm);

}
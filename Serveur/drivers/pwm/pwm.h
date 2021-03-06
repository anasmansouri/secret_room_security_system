 /*H**********************************************************************
* FILENAME :        pwm.h
*
* DESCRIPTION :
*       this a pwm driver of the raspberry pi 3 B+
*
* AUTHOR :    Mansouri Anas        START DATE :    2 Sep 2020
*
*H*/

#ifndef PWM_H_
#define PWM_H_

#include<stdbool.h>

struct pwm_channel {
    char channel_id[4];
    char polarity[10];
    long unsigned int period;
    long unsigned int duty_cycle;
    bool enable;
};
typedef struct pwm_channel pwm_channel;


int load_pwm_channel(pwm_channel *pwm, char channel_id[4] );
int set_pwm_polarity(pwm_channel *pwm, char* polarity);
int set_pwm_period(pwm_channel *pwm, char* period);
int set_pwm_duty_cycle(pwm_channel *pwm, char* duty_cycle);
int enable_pwm_channel(pwm_channel *pwm);
int disable_pwm_channel(pwm_channel *pwm);

char * get_pwm_polarity(pwm_channel pwm);
long unsigned int get_pwm_period(pwm_channel pwm);
long unsigned int get_pwm_duty_cycle(pwm_channel pwm);
#endif /*PWM_H_*/
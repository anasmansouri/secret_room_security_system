#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<stdbool.h>
#include "pwd.h"

/* ********************************** */
/* LOAD_PWM_CHANNEL                     */
/* Initialisation of a PWM channel      */
/* ********************************** */
int load_pwm_channel(pwm_channel *pwm, char channel_id[4])
{
    FILE *p_pwm_export;
    /* Exporting pwm channel */
    if ((p_pwm_export = fopen("/sys/class/pwm/pwmchip0/export", "w")) == NULL)
    {
        printf("Cannot open export file.\n");
        exit(1);
    }
    rewind(p_pwm_export);
    strcpy(pwm->channel_id, channel_id);
    fwrite(&pwm->channel_id, sizeof(char), 1, p_pwm_export);
    fclose(p_pwm_export);
    return 0;
}

/* ****************************************** */
/* SET_PWM_POLARITY                         */
/* Sets the polarity (normal/inversed) of a pwm channel */
/* ****************************************** */
int set_pwm_polarity(pwm_channel *pwm, char polarity[10])
{
    FILE *p_pwm_polarity;
    char pwm_polarity_file_path[40];
    sprintf(pwm_polarity_file_path, "/sys/class/pwm/pwmchip0/pwm%s/polarity", pwm->channel_id);

    
    if ((p_pwm_polarity = fopen(pwm_polarity_file_path, "w+")) == NULL)
    {
        printf("Cannot open polarity file.\n");
        exit(1);
    }
    rewind(p_pwm_polarity);
    // TODO you have to test for errors if the polarity is not normal or inversed
    fputs(p_pwm_polarity,polarity);
    fclose(p_pwm_polarity);
    return 0;
}

/* ****************************************** */
/* SET_PWM_PERIOD                         */
/* Sets the period  of a pwm channel */
/* ****************************************** */
int set_pwm_period(pwm_channel *pwm, long unsigned int period)
{
    FILE *p_pwm_period;
    char pwm_period_file_path[38];
    sprintf(pwm_period_file_path, "/sys/class/pwm/pwmchip0/pwm%s/period", pwm->channel_id);

    
    if ((p_pwm_period= fopen(pwm_period_file_path, "w+")) == NULL)
    {
        printf("Cannot open period file.\n");
        exit(1);
    }
    rewind(p_pwm_period);
    char period_string [20];
    fprintf(period_string, "%lu", period); 
    fputs(p_pwm_period,period_string);
    fclose(p_pwm_period);
    return 0;
}

/* ****************************************** */
/* SET_PWM_DUTY_CYCLE                         */
/* Sets the duty cycle  of a pwm channel */
/* ****************************************** */
int set_pwm_duty_cycle(pwm_channel *pwm, long unsigned int duty_cycle)
{
    FILE *p_pwm_duty_cycle;
    char pwm_duty_cycle_file_path[41];
    sprintf(pwm_duty_cycle_file_path, "/sys/class/pwm/pwmchip0/pwm%s/duty_cycle", pwm->channel_id);

    if ((p_pwm_duty_cycle= fopen(pwm_duty_cycle_file_path, "w+")) == NULL)
    {
        printf("Cannot open duty cycle file.\n");
        exit(1);
    }
    rewind(p_pwm_duty_cycle);
    char duty_cycle_string [20];
    fprintf(duty_cycle_string, "%lu", duty_cycle);
    fputs(p_pwm_duty_cycle,duty_cycle_string);
    fclose(p_pwm_duty_cycle);
    return 0;
}

/* ********************************** */
/* ENABLE_PWM_CHANNEL                     */
/*       */
/* ********************************** */
int enable_pwm_channel(pwm_channel *pwm)
{
    FILE *p_pwm_enable;
    char pwm_enable_file_path[38];
    sprintf(pwm_enable_file_path, "/sys/class/pwm/pwmchip0/pwm%s/enable", pwm->channel_id);

    if ((p_pwm_enable= fopen(pwm_enable_file_path, "w+")) == NULL)
    {
        printf("Cannot open enable file.\n");
        exit(1);
    }
    rewind(p_pwm_enable);
    fputs(p_pwm_enable,"1");
    fclose(p_pwm_enable);
    return 0;
}

/* ********************************** */
/*  DISABLE_PWM_CHANNEL                    */
/*       */
/* ********************************** */
int disable_pwm_channel(pwm_channel *pwm)
{
    FILE *p_pwm_enable;
    char pwm_enable_file_path[38];
    sprintf(pwm_enable_file_path, "/sys/class/pwm/pwmchip0/pwm%s/enable", pwm->channel_id);

    if ((p_pwm_enable= fopen(pwm_enable_file_path, "w+")) == NULL)
    {
        printf("Cannot open enable file.\n");
        exit(1);
    }
    rewind(p_pwm_enable);
    fputs(p_pwm_enable,"0");
    fclose(p_pwm_enable);
    return 0;
}




/* ****************************************** */
/* GET_PWM_POLARITY                              */
/* Gets polarity of a pwm channel                  */
/* ****************************************** */
char * get_pwm_polarity(pwm_channel *pwm){
    FILE *p_pwm_polarity;
    char pwm_polarity_file_path[40];
    sprintf(pwm_polarity_file_path, "/sys/class/pwm/pwmchip0/pwm%s/polarity", pwm->channel_id);
    /* Getting polarity */
    if ((p_pwm_polarity = fopen(pwm_polarity_file_path, "w+")) == NULL)
    {
        printf("Cannot open polarity file.\n");
        exit(1);
    }
    char polarity[10];
    rewind(p_pwm_polarity);
    fgets(polarity,10,p_pwm_polarity);
    fclose(p_pwm_polarity);
    return polarity;
}

/* ****************************************** */
/* GET_PWM_PERIOD                         */
/* Gets the period  of a pwm channel */
/* ****************************************** */
char * get_pwm_polarity(pwm_channel *pwm)
{
    FILE *p_pwm_period;
    char pwm_period_file_path[38];
    sprintf(pwm_period_file_path, "/sys/class/pwm/pwmchip0/pwm%s/period", pwm->channel_id);

    /* Getting period */
    if ((p_pwm_period= fopen(pwm_period_file_path, "w+")) == NULL)
    {
        printf("Cannot open period file.\n");
        exit(1);
    }
    rewind(p_pwm_period);
    long unsigned int period;
    fread(&period,sizeof(period),1,p_pwm_period);
    fclose(p_pwm_period);
    return period;
}


/* ****************************************** */
/* GET_PWM_DUTY_CYCLE                         */
/* Gets the duty cycle  of a pwm channel */
/* ****************************************** */
long unsigned int get_pwm_duty_cycle(pwm_channel *pwm)
{
    FILE *p_pwm_duty_cycle;
    char pwm_duty_cycle_file_path[41];
    sprintf(pwm_duty_cycle_file_path, "/sys/class/pwm/pwmchip0/pwm%s/duty_cycle", pwm->channel_id);

    if ((p_pwm_duty_cycle= fopen(pwm_duty_cycle_file_path, "w+")) == NULL)
    {
        printf("Cannot open duty cycle file.\n");
        exit(1);
    }

    rewind(p_pwm_duty_cycle);
    long unsigned int duty_cycle;
    fread(&duty_cycle,sizeof(duty_cycle),1,p_pwm_duty_cycle);
    fclose(p_pwm_duty_cycle);
    return duty_cycle;
}
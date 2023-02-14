import time
import pandas as pd
import numpy as np

Name_of_City = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
        
    city = input('Enter the city you want see data for Chicago , New York City or Washington : ')
    city = city.lower()
    while city not in Name_of_City:
        city = input('Invalid city name.Please Try Again!')
        city = city.lower()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Enter the month from January to June OR Enter "all" for no month filter : ')
    month = month.lower()
    if month == 'january':
        ind = 0 
    elif month == 'february':
        ind = 1
    elif month == 'march':
        ind = 2
    elif month == 'april':
        ind = 3
    elif month == 'may':
        ind = 4
    elif month == 'june':
        ind = 5
    else : 
        ind=0
    while month not in months:
        month = input('Invalid month name. Please Try Again!: ')
        month = month.lower()
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Enter the day from Sunday to Suterday OR Enter "all" for no day filter : ')
    day = day.lower()
    while day not in days:
        day = input('Invalid day name.Please Try Again!')
        day = day.lower()

    print('-'*50)
    return city, month, day, ind


def load_data(city, month, day):
   
    df = pd.read_csv(Name_of_City[city])    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, ind):    


    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month 
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Popular Month:', months[df['month'].mode()[0]-1])
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most Popular Day:', days[df['day_of_week'].mode()[0]])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()
    print('Most Popular Start Hour:', popular_hour)
    print('-'*55)


def station_stats(df):
    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('Most Popular Start Station: \n', df['Start Station'].mode()[0])
    print('Most Popular End Station: \n', df['End Station'].mode()[0])
    print('Most Frequent Combination of Start and End Station Trips:\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))
    print('-'*55)


def trip_duration_stats(df):

    print('Calculating Trip Duration...\n')
    start_time = time.time()
    print('Total Trip Duration:', df['Trip Duration'].sum())
    print('Mean Trip Duration:', df['Trip Duration'].mean())
    print('-'*55)


def calculator(df):

    print('Calculating User Stats \n')
    start_time = time.time()
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')
    if 'Gender' in df.columns:    
        gender = df['Gender'].value_counts()
        print(gender,'\n')
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])

    print('-'*55)

def main():
    city, month, day, ind = get_filters()
    df = load_data(city, month, day)
    time_stats(df,ind)
    station_stats(df)
    trip_duration_stats(df)
    calculator(df)

if __name__ == "__main__":
	main()
#adding comments 
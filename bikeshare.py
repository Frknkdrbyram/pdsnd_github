import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    
    """Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("Hello! Let's explore some US bikeshare data!")
    
    # Get user input for city (chicago, new york, washington). Use a while loop to handle invalid inputs.
   
    city_condition=True

    while city_condition:
        city =input("Please choose one of the given cities you want to see trasportation data for: Chicago, New York,or Washington:\n").lower()
        if city in cities:
            city_condition= False
        else:
            print('Please enter the city name correctly(Chicago, New York,or Washington)\n.')
            
    # Get user to filter by month, day, or none.
    while True:
        option = input("Would you like to filter the data by month or day, if you dont want to filter you can choose No:\n ").lower()
        if option == 'month':
            month = input("Please enter the month you want to learn data (options: All, January, February, March, April, May, June):\n").lower()
            day = 'all'
            if month in months:
                break
            else:
                print('Please enter the month name correctly(All, January, February, March, April, May, June).')
        elif option == 'day':
            day = input("Please enter the day you want to learn data (options:All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)").lower()
            month = 'all'
            if day in days:
                break
            else:
                print('Please enter the day name correctly (All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)')
        elif option == 'no':
            month = 'all'
            day = 'all'
            break
    
  
    return city, month, day

def multiply(x,y):
    return x*y

def refactoring():
    print('Refactoring')
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    

    # extract month and day of week from Start Time to create required columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all': 
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Popular Times of Travel...\n')
    start_time = time.time()

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month from start time column to create month column 
    popular_month = df['month'].mode()[0]
    
        
    # Change number to months
    if popular_month == 1:
        popular_month = "January"
    elif popular_month == 2:
        popular_month = "February"
    elif popular_month == 3:
        popular_month = "March"
    elif popular_month == 4:
        popular_month = "April"
    elif popular_month == 5:
        popular_month = "May"
    elif popular_month == 6:
        popular_month = "June"
    print('Most Common Month: \n', popular_month)
    
    # Display the most common day of the week
   
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:\n', popular_day)



    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour 
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: \n', popular_hour, ':00' )

    print("This process took {} seconds.".format (time.time() - start_time))
    
def station_stats (df):        
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station: \n", popular_start_station)
    
    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Common End Station: \n", popular_end_station)
    
    # Display most frequent combination of start station and end station trip
    combination_station = df['Start Station'] + " to " +  df['End Station']
    common_combination_station = combination_station.mode()[0]
    print("Most Common Trip from Start to End:\n {}".format(common_combination_station)) 
    
    print("This process took {} seconds.".format (time.time() - start_time))
    
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print("The Total Travel Time is {} Hours, {} Minutes, and {} Seconds.".format(hour, minute, second))

    # Display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    second=average_duration%60 
    minute=int(average_duration/60)
    
    if minute> 60:
        hour, minute = divmod(minute, 60)
        print('The Average Travel Time is {} Hours, {} Minutes, and {} seconds.'.format(hour, minute, second))
    else:
        print('The Average Trip Duration is {} Minutes and {} Seconds.'.format(minute, second))
        
    print("This process took {} seconds.".format (time.time() - start_time))
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of Each User Type:\n", user_types)

    # Display counts of Gender_Types
    try:
        gender_types = df['Gender'].value_counts()
       
        print('\nGender Types:\n',gender_types)
      
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
      
    # Display Earliest_Year,Most_Recent_Year, and Most_Common year of birth
    try:
        Earliest_Year = df['Birth Year'].min() #Oldest birth year
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.\n")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")
    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")
            
    print("This process took {} seconds.".format (time.time() - start_time))


def individual_data(df):
    # Show 5 row of  individual trip data.
    start_loc = 0
    view_data = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n")
    while True:
        
        if view_data.lower() == 'yes':
            print("\nDisplaying only 5 rows of data.\n")
            print(df.iloc[start_loc:(start_loc+5)])
            start_loc += 5
            view_data = input("\nDo you wish to continue? Enter 'yes' or 'no'.\n")
            
        elif view_data.lower()=='no':
            break  
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
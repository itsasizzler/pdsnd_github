import time
import pandas as pd
import numpy as np

<<<<<<< HEAD
## Source data for the script identified below. Currently being gitignored.
=======
#City data derived from online resources including city APIs.
>>>>>>> refactoring
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\nWould you like to see data for chicago, new york city, or washington?\n')
        if city in CITY_DATA:
            break
        else:
            print('\nSorry that\'s not a valid city!')

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("Please enter 'all' or the full name of a month (January through June):").lower()
        if month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Please enter a different month")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Enter a day of the week or 'all':").lower()
        if day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Enter a valid day of the week.")
        else:
            break

    print('-' * 40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = {'january':1,'february':2,'march':3,'april':4,'may':5,'june':6}
        month = months[month]
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].value_counts().idxmax()
    print("The most popular month:",popular_month)
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].value_counts().idxmax()
    print("The most popular day:",popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print("The most popular hour:",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("Most common start station:",start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("Most common end station:",end_station)

    # TO DO: display most frequent combination of start station and end station trip
    route = df.groupby('Start Station')['End Station'].value_counts().idxmax()
    print("Most common route:",route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print("Total travel time:",trip_duration)
    # TO DO: display mean travel time
    trip_average = df['Trip Duration'].mean()
    print("Average travel time:",trip_average)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Types of users:",user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("Counts by gender:",gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        popular_year = df['Birth Year'].value_counts().idxmax()
        print("Oldest user:",earliest)
        print("Youngest user:",recent)
        print("Most common birth year:",popular_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    #Presents raw dataframe data five rows at a time to the user of the script
def raw_data(df):
    more_data = input('Would you like to see the raw data? Please enter yes or no:').lower()
    if more_data in ('yes'):
        i = 0
        while True:
            if (i + 5) > len((df.index) -1):
                print(df.iloc[i:len(df.index)])
                print('You\'ve reached the end of the data')
            else:
                print(df.iloc[i:i+5])
                i += 5
                even_more_data = input('Would you like to see five more rows of raw data? Please enter yes or no:').lower()
                if even_more_data not in ('yes'):
                    break

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

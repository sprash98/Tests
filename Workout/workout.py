
import pickle
import re
from collections import OrderedDict


def validate_numeric_params(type,*max):
    if re.match("Age",type,re.I) :
        units = "yrs"
    elif re.match("Duration",type,re.I) :
        units = "minutes"
    elif re.match("Weight",type,re.I) :
        units = "Kgs/Lbs"
    else :
        units = "levels"

    while True:
        try:
            value = input("Please enter your %s in %s  : " %(type,units))
            value = int(value)
            if value <= 0 :
                raise ValueError
            if max:
                if value > max[0] :
                    raise ValueError
        except (TypeError, ValueError) :
            if max :
                print("Please enter a positive non-zero integer value for %s "
                      "lesser than or equal to %d %s" % (type,max[0],units))
            else :
                print("Please enter a positive non-zero integer value for %s" %type)

        else :
            break

    return value



class Workout():
    """ Class containing the workout details

    Identifiers:
        title - Name of the workout
        duration - duration of workout, in minutes
        intervals - Total number of workout intervals
        settinga - An ordered dictionary where the keys are the timestamps corresponding
                to the intervals, and the value is a dictionary where the keys
                are Intensity, Workout level and Incline

    """


    # Set bounds for numeric values
    max_duration = 120
    max_level = 10
    max_intensity = 10
    max_incline = 12

    def __init__(self):

        """ Add a workout to the list of user workouts
        :return: 1
        """

        # Add workout information
        self.title = input("Enter a name for the workout: ")
        self.duration = validate_numeric_params("duration",Workout.max_duration)
        self.intervals = validate_numeric_params("intervals")
        self.settings = OrderedDict()


        # If workout is on a treadmill, toggle the is_treadmill flag
        while True :
            self.is_treadmill = input("Is this a treadmill workout? (Y/N)?")
            if not re.search("Y|N",self.is_treadmill,re.I) :
                print("Please enter a Y or a N for the answer")
            else :
                if re.search("Y",self.is_treadmill,re.I) :
                    self.is_treadmill = 1
                else :
                    self.is_treadmill = 0
                break


        # Obtain the list of timestamps as an array
        times = self.process_intervals(self.duration,self.intervals)

        # Create the settings for each timestamp as an ordered dictionary
        # where the keys are the timestamps and the values are a dictionary
        # containing the level, intensity and incline values
        for time in times :
            print("Interval at time %d seconds" %time)
            intensity = validate_numeric_params("intensity",Workout.max_intensity)
            level = validate_numeric_params("level",self.max_level)
            if self.is_treadmill :
                incline = validate_numeric_params("incline",Workout.max_incline)
            else:
                incline = 0
            self.settings[time] = {"Intensity": intensity, "WorkoutLevel": level, "Incline":incline}


    def process_intervals(self,duration,intervals):

        """
        :param duration: Total time duration of workout
        :param intervals: Total number of time intervals
        :return: A list containing the timestamps corresponding to
                 the time duration and intervals
        """

        time_per_interval = self.duration*60//self.intervals
        spillover = self.duration*60%self.intervals

        dur = self.duration
        timestamps = []
        current_time = 0

        while intervals >0 :
            timestamps.append(current_time)
            current_time += time_per_interval
            intervals -= 1

        return timestamps




class User() :
    """ Class containing user information
        Fieklds :

            name - Name of user
            gender: Gender of user
            weight: Weight of the user
            unitweight: 1 for Kgs, 2 for Lbs
            max_count: Maximum no of workouts per user
            workouts: List of Workout objects
    """

    workout_count = 0
    workouts = []
    max_count = 10
    max_age = 110

    def __init__(self):
        """ Supply user information
        :return:
        """

        self.name = input("Please enter your name: ")
        self.age = validate_numeric_params("age",User.max_age)


        while True:
            self.gender = input("Please enter your gender (M/F): ")
            if re.search("M|F",self.gender,re.I) :
                break
            else:
                print("Please enter one of 'M' or 'F' for gender")

        self.weight = validate_numeric_params("weight")
        while True :
            try:
                self.unitWeight = input("Please select the unit for weight (1 for KGs/2 for Lbs) :")
                self.unitWeight = int(self.unitWeight)
            except ValueError:
                print("Please select 1 for Kg or 2 for Lb")
            else:
                if self.unitWeight == 1 or self.unitWeight == 2 :
                    break


    def update_user_workouts(self,workout):

        """  If there are max no of workouts, it deletes the first workout
             and adds a new one as the last entry in the list
        :return: 1
        """

        # Pop the first/oldest entry in the list
        print("Deleting the first workout...")
        self.workouts.pop(0)
        self.workout_count -+ 1

        # Adding the new workout to the end of the list
        print("Adding new workout...")
        self.workouts.append(workout)
        self.workout_count += 1
        return 1

    def delete_user_workout(self,key):

        """
        :param selfself:
        :param key: Number or title of workout
        :return: 1, for successful deletion
                 0, if operation is unsuccessful


        """

        # If key is specified as a number, pop that element from the list
        # else if key is specified as a title, remove the element matching
        # the tilte name.

        is_deleted = 0
        workout = self.get_user_workout(key)
        if workout == None :
            print("Unable to delete workout. Workout specified not found. Aborting...")
        else :
            self.workouts.remove(workout)
            self.workout_count -=1
            print("Workout deleted!")
            is_deleted += 1

        return is_deleted


    def add_user_workout(self):

        """ Add a workout to the list of user workouts
        :return: Workout object, if object is successfully added
                 None, otherwise
        """


        is_added = 0
        workout = Workout()
        # If the number of workouts is less than max, append the workout to the list
        if self.workout_count < self.max_count :
            self.workouts.append(workout)
            self.workout_count +=1
            is_added +=1
        else :
            # If the list of workouts is full, prompt before appending new workout
            while True:
                overwrite = input("All records are full. Would you like to delete"
                        "the oldest workout and add the new one? (Y/N)")

                choice = re.compile("Y|N",re.I)
                if not choice.search(overwrite) :
                    print("Please enter a Y or a N for the answer")
                else :
                    if re.search('y',overwrite,re.I) :
                        self.update_user_workouts(workout)
                        is_added +=1
                    else :
                        print("Workout %s not added to workout list" %workout.title)
                    break


        if is_added :
            return workout
        else :
            return None




    def print_user_workout(self,key):

        """ Print the details of a user workout
        :param selfself:
        :param key:
        :return:1
        """

        workout = self.get_user_workout(key)
        if workout == None :
            print("Workout %s not found for printing." %key)
        else :
            for time in workout.settings.keys() :
                print("Intensity at time %d seconds is %d" %(time,workout.settings[time]["Intensity"]))
                print("Workout level at time %d seconds is %d" %(time,workout.settings[time]["WorkoutLevel"]))
                if workout.is_treadmill :
                    print("Incline at time %d seconds is %d" %(time,workout.settings[time]["Incline"]))

        return 1


    def get_user_workout(self,key):
        """
         Return  workout with specified title/index
        :param key: Title of workout to be returned
        :return: Workout object, if successful
                 None, if failure
        """

        is_found = 0

        # Check if supplied key is the index to the list of workouts
        try :
            key = int(key)
            if key <1  or key > len(self.workouts):
                print("Invalid key specified for printing workout.")
            else :
                workout = self.workouts[key-1]
                is_found +=1

        # If supplied key is a string, compare it to the titles of the saved workouts
        except ValueError:
            pattern = re.compile(key,re.I)
            for workout in self.workouts :
                if pattern.search(workout.title) :
                    is_found += 1
                    break

        # If workout is found, return the object else return None
        if not is_found:
            workout = None

        return workout

    def check_user_workout(self,title):
        """
        Verify that a workout of the specified title is present
        :param selfself:
        :param key:
        :return: 1, if successful
                 0, if unsuccessful
        """

        if not self.get_user_workout(title) :
            return 0
        else :
            return 1











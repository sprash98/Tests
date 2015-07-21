from workout import *
from time import *
import re

def bulk_workouts_test(user) :

    """
    :param user: User object
    :return:
    """

    print("Adding the first %d workouts" %(user.max_count))
    for i in range(0,user.max_count):
        print("Creating workout %d" %(i+1))
        workout = user.add_user_workout()
        if not workout :
            print("ERROR: Something went wrong. Aborting...")
            return 0

        # Verify that the workout is saved
        if not user.check_user_workout(workout.title) :
            print("ERROR: Unable to find workout %s " %workout.title)
            return 0

        # Print workout
        user.print_user_workout(workout.title)


    flag = 1
    while flag :
        oldest_workout = user.workouts[0].title
        workout = user.add_user_workout()
        if workout :
            if user.check_user_workout(oldest_workout) :
                print("ERROR:Oldest workout %s still exists" %oldest_workout)
                return 0
            else :
                print("Oldest workout %s no longer found" %oldest_workout)

            if not user.check_user_workout(workout.title) :
                print("ERROR: Unable to find workout %s" %workout.title)
            else:
                print("Workout %s found for user %s" %(workout.title,user.name))

        else :
            if not user.check_user_workout(oldest_workout) :
                print("ERROR: Unable to find oldest workout %s" %oldest_workout)
                return 0
            else :
                print(" Oldest workout %s found!" %oldest_workout)


        while True:
            flag = input("Do you want to continue adding workouts? (y/n)")
            choice = re.compile("Y|N",re.I)
            if not choice.search(flag) :
                print("Please enter y or n to continue")
            else :
                if re.match("n",flag,re.I) :
                    flag = 0
                break

    return 1


def main() :
    user= User()
    print("Let's add a single workout and verify it's contents before deleting it")
    sleep(3)
    workout = user.add_user_workout()
    if not user.print_user_workout(workout.title) :
        print("FAIL: Printing operation failed. Aborting...")
        return 0
    print("Now deleting the workout %s" %user.workouts[0].title)
    sleep(3)
    if not user.delete_user_workout(workout.title) :
        print("FAIL: Deletion operation failed. Aborting...")
        return 0
    if not user.print_user_workout(workout.title) :
        print("SUCCESS: Deletion successful!")

    print("Now let's add workouts in bulk...")
    sleep(3)
    if not bulk_workouts_test(user) :
        print("FAIL: Unable to verify addition of workouts in bulk")
        return 0
    else :
        print("SUCCESS: Bulk addition of workouts successful")

if __name__ == "__main__" :
    main()





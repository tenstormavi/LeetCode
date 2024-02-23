"""
We are writing software to collect and manage data on how fast racers can complete obstacle courses. An obstacle course
is a series of difficult physical challenges (like walls, hurdles, and ponds) that a racer must go through.

Each course consists of multiple obstacles. The software stores how long it takes for racers to finish each obstacle,
and provides useful statistics based on those times.

Definitions:
* A "run" is a particular attempt to complete an entire obstacle course
* A "run collection" is a group of runs on a particular course by the user.
* An "obstacle" is a portion of a course. We track how long it takes to finish each portion of the course

For example, here are some times for an obstacle course with four obstacles:

 Obstacles:    O1  O2  O3  O4
    Run 1:      3   4   5   6    (total: 18 seconds)
    Run 2:      4   4   4   5    (total: 17 seconds)
    Run 3:      5   5   3        (13 seconds, but run is incomplete)

All of these runs for one obstacle course (including the incomplete run) make up a run collection.

To begin with, we present you with two tasks:
1-1) Read through and understand the code below. Please take as much time as necessary, and feel free to run the code.
1-2) The test for RunCollection is not passing due to a bug in the code. Make the necessary changes to RunCollection
to fix the bug.

2) We would like to implement a new function in RunCollection called "best_of_bests". This is a measure of how fast
a run could be if everything went perfectly, and is determined by taking the fastest times for each obstacle across
all runs (even incomplete ones) and summing them.

Implement this function, and add a test to verify that it works.
"""

import unittest


class Course:
    """ Data about a particular course. """

    def __init__(self, title, obstacle_count):
        self.title = title  # String, the name of the obstacle course
        self.obstacle_count = obstacle_count  # int, the number of obstacles
        #      in the course

    def __eq__(self, other):
        if not isinstance(other, self.__class__): return False
        return (self.title == other.title and
                self.obstacle_count == other.obstacle_count)


class Run:
    """Data and methods about a single run of a course."""

    def __init__(self, course):
        self.course = course  # a Course object saying what course this is a run for
        self.complete = False  # a boolean, True if the run is a full run of the
        # course. This may be False if a run is in progress or aborted
        self.obstacle_times = []  # list of int, the times it took to complete each obstacle

    def add_obstacle_time(self, obstacle_time):
        # When an obstacle is completed, add the time to the current run.
        # obstacle_time: int, the time in seconds it took to complete the obstacle
        if self.complete:
            raise ValueError("Cannot add obstacle to complete run")
        self.obstacle_times.append(obstacle_time)
        if len(self.obstacle_times) == self.course.obstacle_count:
            self.complete = True

    def get_run_time(self):
        # Returns the total time this run has taken.
        # If the run is not complete, it returns the time the run has taken so far.
        return sum(self.obstacle_times)


class RunCollection(object):
    """
        Data for a number of runs of a particular course, and methods for getting
        useful statistics about all runs of a course.
    """

    def __init__(self, course):
        self.runs = []  # list of Run objects, the runs for this particular course
        self.course = course  # course, the Course this RunCollection is for

    def get_num_runs(self):
        """Returns the number of Runs in this Collection"""
        return len(self.runs)

    def add_run(self, run):
        """Adds a Run to this RunCollection."""
        if run.course != self.course:
            raise ValueError("Run's Course is not the same as the RunCollection's")
        self.runs.append(run)

    def personal_best(self):
        """Return the best time achieved in this RunCollection."""
        return min(run.get_run_time() for run in self.runs if len(run.obstacle_times) == run.course.obstacle_count)

    def best_of_bests(self):
        res = [float('inf')] * self.course.obstacle_count
        for run in self.runs:
            for idx, time in enumerate(run.obstacle_times):
                if time < res[idx]:
                    res[idx] = time
        return sum(res)


class TestSuite(unittest.TestCase):
    """
        This is not a complete test suite, but tests some basic functionality of
        the above code and shows some about how to use the code.
    """

    def test_run(self):
        """Test basic Run functionality"""
        test_course = Course("Test course", 2)
        test_run = Run(test_course)
        test_run.add_obstacle_time(3)
        self.assertFalse(test_run.complete)
        test_run.add_obstacle_time(5)
        self.assertTrue(test_run.complete)
        self.assertEqual(test_run.obstacle_times, [3, 5])
        self.assertEqual(test_run.get_run_time(), 8)
        with self.assertRaises(ValueError):
            test_run.add_obstacle_time(4)

    def make_run_collection(self, course, obstacle_data):
        """
            Create a new RunCollection for test purposes.

            course: The Course object this RunCollection is for
            obstacle_data: a list of lists. Each list represents obstacle times for
                           a single run of the course.
        """
        run_collection = RunCollection(course)
        for run_data in obstacle_data:
            run = Run(course)
            for obstacle_time in run_data:
                run.add_obstacle_time(obstacle_time)
            run_collection.add_run(run)
        return run_collection

    def test_run_collection(self):
        """Test basic RunCollection functionality"""

        """
        Obstacles: O1  O2  O3  O4
        Run 1:      3   4   5   6    (total: 18 seconds)
        Run 2:      4   4   4   5    (total: 17 seconds)
        Run 3:      5   5   3        (13 seconds, but run is incomplete)
        """
        obstacle_data = [
            [3, 4, 5, 6],
            [4, 4, 4, 5],
            [5, 5, 3]
        ]
        test_course = Course("Test course", 4)
        run_collection = self.make_run_collection(test_course, obstacle_data)
        self.assertEqual(run_collection.best_of_bests(), 15)
        self.assertEqual(run_collection.get_num_runs(), len(obstacle_data))
        self.assertEqual(run_collection.personal_best(), 17)


if __name__ == '__main__':
    unittest.main()
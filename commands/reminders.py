from commands.viewpoints import ViewPoints
import datetime

class Reminders:
    """
        This class handles the Create Reminder functionality.
    """
    def createReminder(self):
        #Method to create reminder
        #Fetch pending task list
        vp = ViewPoints(progress=0.0)
        pending_tasks = vp.get_list()
        print(pending_tasks)

        # # dictionary
        # task_details = {}
        # for task in pending_tasks:
        #     taskid = task[0]
        #     taskname = task[4]
        #     taskdate = task[5]
        #
        #     # I am assuming that taskdate is in str
        #     curr_date = datetime.date.today()
        #     tomorrow = str(curr_date + datetime.timedelta(days=1))
        #
        #     if taskdate == tomorrow:
        #         task_details[taskid] = taskname
        #
        # print(task_details)

        # return task_details, tomorrow

    def reminder_msg(self):
        # This method creat

        pending_tasks, tomorrow = self.createReminder()
        msg = ''
        for task in pending_tasks:
            task_name = pending_tasks[task]
            msg += """ Task ID: {task} ({taskname}) [Deadline is {tomorrow_date}]./n""".format(
                task=task, tomorrow_date=tomorrow)

        return msg
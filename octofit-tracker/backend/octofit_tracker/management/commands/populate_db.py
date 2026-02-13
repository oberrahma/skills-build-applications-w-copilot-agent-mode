from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        users = [
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Batman', email='batman@dc.com', team='DC'),
            User(name='Superman', email='superman@dc.com', team='DC'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        activities = [
            Activity(user='Iron Man', type='Running', duration=30),
            Activity(user='Batman', type='Cycling', duration=45),
            Activity(user='Spider-Man', type='Swimming', duration=25),
        ]
        for activity in activities:
            activity.save()

        leaderboard = [
            Leaderboard(user='Iron Man', points=100),
            Leaderboard(user='Batman', points=90),
            Leaderboard(user='Superman', points=80),
        ]
        for entry in leaderboard:
            entry.save()

        workouts = [
            Workout(name='Push Ups', description='Do 20 push ups'),
            Workout(name='Squats', description='Do 30 squats'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))

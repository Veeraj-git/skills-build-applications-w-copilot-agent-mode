from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel', super_power='Genius, Suit'),
            User(email='captain@marvel.com', name='Captain America', team='Marvel', super_power='Super Soldier'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel', super_power='Spider Sense'),
            User(email='batman@dc.com', name='Batman', team='DC', super_power='Detective, Gadgets'),
            User(email='superman@dc.com', name='Superman', team='DC', super_power='Flight, Strength'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', super_power='Amazonian Warrior'),
        ]
        User.objects.bulk_create(users)

        # Activities
        activities = [
            Activity(user='Iron Man', activity_type='Running', duration=30, date='2026-03-17'),
            Activity(user='Captain America', activity_type='Cycling', duration=45, date='2026-03-16'),
            Activity(user='Spider-Man', activity_type='Jumping', duration=20, date='2026-03-15'),
            Activity(user='Batman', activity_type='Martial Arts', duration=60, date='2026-03-14'),
            Activity(user='Superman', activity_type='Flying', duration=120, date='2026-03-13'),
            Activity(user='Wonder Woman', activity_type='Lifting', duration=50, date='2026-03-12'),
        ]
        Activity.objects.bulk_create(activities)

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=95)
        Leaderboard.objects.create(team='DC', points=90)

        # Workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity interval training for heroes', difficulty='Hard'),
            Workout(name='Power Yoga', description='Yoga for strength and flexibility', difficulty='Medium'),
            Workout(name='Speed Run', description='Running workout for speed', difficulty='Easy'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

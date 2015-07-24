# -*- coding: iso-8859-1 -*-
import csv
from clubs.models import Club
import re
from athletes.models import Athlete, ClubForAthlete

from django.core.management.base import BaseCommand, CommandError

from django.utils.translation import ugettext as _
from meetings.models import Meeting
from races.models import Race, Result

from unicodedata import normalize


class Command(BaseCommand):
    help = _(u'Add results')

    def add_arguments(self, parser):
        parser.add_argument('file', nargs=1, type=str)

    def handle(self, *args, **options):
        #print options.get('file')[0]
        file_name = options.get('file')[0]
        try:
            is_csv = self.is_csv_file(file_name, delimiter=';')

            if len(is_csv) == 0:
                with open(file_name, 'rbU') as csvfile:
                    reader = csv.reader(csvfile, delimiter=';')
                    race = ""
                    csv_num_line = 0
                    for row in reader:
                        csv_num_line += 1
                        try:
                            if row == ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']:
                                continue
                            if row[1] == 'Atleta':
                                continue

                            dict_line = self.line_to_dict(row)

                            if dict_line.get('athlete') == '' or race == '':
                                race = self.get_race(dict_line)
                                #print race
                                continue
                            else:
                                # We get the athlete
                                athlete = self.get_athlete(dict_line)
                                if dict_line.get('club'):
                                    self.add_athlete_to_club(athlete, dict_line.get('club'), dict_line.get('season'))
                                self.add_result(athlete, race, dict_line)
                        except Exception, e:
                            print csv_num_line, ':', e.message

            else:
                print 'Not a valid csv'
        except Exception, e:
            raise CommandError(e)

    def is_csv_file(self, filename, delimiter):
        errors = []
        try:
            csv_fileh = open(filename, 'rb')
            # Perform various checks on the dialect (e.g., lineseparator, delimiter) to make sure it's sane
            dialect = csv.Sniffer().sniff(csv_fileh.read(), delimiter)
            # Don't forget to reset the read position back to the start of the file before reading any entries.
            csv_fileh.seek(0)
            csv_fileh.close()
        except csv.Error as e:
            errors.append(e)
        except (IOError, OSError) as e:
            errors.append(e)
        return errors

    def line_to_dict(self, line):
        return {
            "position": line[0],
            "athlete": unicode(line[1].decode('iso-8859-1')),
            "club": line[2],
            "record": line[3],
            "race": line[4],
            "category": line[5],
            "round": line[6],
            "event": line[7].decode('iso-8859-1'),
            "event_shorten": line[8].decode('iso-8859-1'),
            "date": line[9],
            "season": line[10],
            "city": line[11],
            "meeting_type": line[12],
            "media": line[13],
            "comments": line[14]
        }

    def read_line(self, line):
        # Columns
        # 0: Posición
        # 1: Atleta
        # 2: Club
        # 3: Marca
        # 4: Prueba
        # 5: Cat
        # 6: Fase
        # 7: Evento
        # 8: Evento Resumido
        # 9: Fecha
        # 10: Año
        # 11: Ciudad
        # 12: Meeting type
        # 13: Vídeo
        # 14: Observaciones
        position = line[0]
        athlete = Athlete.get_by_name(line[1])

    def get_race(self, line_dict):
        #print line_dict

        meeting_data = {
            'name': line_dict.get('event'),
            'sort_name': line_dict.get('event_shorten'),
            'date': line_dict.get('date'),
            'season': line_dict.get('season'),
            'city': line_dict.get('city'),
            'type': line_dict.get('meeting_type')
        }

        meeting = self.get_meeting(meeting_data)
        #print meeting

        type = 'TT' if 'm' in line_dict.get('race') else 'LE'
        try:
            return Race.objects.get(type=type, category=line_dict.get('category'), round=line_dict.get('round'),
                                    meeting=meeting)
        except Race.DoesNotExist:

            race = Race()
            race.type = 'TT' if 'm' in line_dict.get('race') else 'LE'
            race.category = line_dict.get('category')
            race.event = line_dict.get('race')
            race.round = line_dict.get('round')
            race.meeting = meeting
            race.save()

        return race

    def get_meeting(self, data):
        try:
            return Meeting.objects.get(name__icontains=data.get('name'), date=data.get('date'))
        except:
            meeting = Meeting(**data)
            meeting.save()
            return meeting

    def get_athlete(self, dict_line):
        try:
            return Athlete.objects.get(slug=self.slugify(dict_line.get('athlete')))
        except Athlete.DoesNotExist:
            athlete = Athlete()
            athlete.name = dict_line.get('athlete')
            athlete.slug = self.slugify(dict_line.get('athlete'))
            athlete.save()
            return athlete

    def slugify(self, text, delim=u'-'):
        """Generates an slightly worse ASCII-only slug."""
        _punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
        result = []
        for word in _punct_re.split(text.lower()):
            word = normalize('NFKD', word).encode('ascii', 'ignore')
            if word:
                result.append(word)
        return unicode(delim.join(result))

    def add_athlete_to_club(self, athlete, club_abbreviation, season):
        try:
            club = Club.objects.get(abbreviation=club_abbreviation)
        except Club.DoesNotExist:
            club = Club()
            club.name = club_abbreviation
            club.abbreviation = club_abbreviation
            club.save()

        try:
            ClubForAthlete.objects.get(athlete=athlete, club=club, season=season)
        except ClubForAthlete.DoesNotExist:
            clubForAthlete = ClubForAthlete(athlete=athlete, club=club, season=season)
            clubForAthlete.save()

    def add_result(self, athlete, race, dict_line):

        try:
            result = Result.objects.get(athlete=athlete, race=race)
        except Result.DoesNotExist:
            result = Result()
            result.race = race
            result.athlete = athlete

        result.set_record(dict_line.get('record'))
        result.position = dict_line.get('position') if dict_line.get('position') != "" else None
        result.save()
